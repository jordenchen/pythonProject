import sys

import frida
from PyQt5.QtCore import QThread, pyqtSignal


class logthread(QThread):
    finishSignal = pyqtSignal(str)

    def __int__(self, parent=None):
        super(QThread, self).__init__(parent)

    def on_message(self, message, data):
        if message['type'] == 'send':
            print(message['payload']['xml'])
            self.finishSignal.emit(message['payload']['xml'])

        elif message['type'] == 'error':
            print(message)
            self.finishSignal.emit(message)
        else:
            print(message)
            self.finishSignal.emit(message)

    def run(self):
        session = frida.attach("wechat.exe")
        print("启动成功")
        script = session.create_script("""
                    var ModAddress = Process.findModuleByName('wechatwin.dll');
                    var hookAddress = ModAddress.base.add('0x5bec6e');
                    Interceptor.attach(hookAddress , {
                        onEnter:function(args) {
                            var edi1= this.context.edi;
                            var xmlPro1 = Memory.readPointer(edi1);
                            var xml = Memory.readUtf16String(Memory.readPointer(xmlPro1.add('0x70')));
                            send({'xml':xml});
                        }
                    } );
                    """)
        script.on('message', self.on_message)
        # self.finishSignal.emit(message)
        script.load()
        # print("[!] Ctrl+D on UNIX, Ctrl+Z on Windows/cmd.exe to detach from instrumented program.\n\n")
        # sys.stdin.read()
        # session.detach()
