import frida
from PyQt5.QtCore import QThread, pyqtSignal


class RunThread(QThread):
    # 输出信号
    finishSignal = pyqtSignal(str)

    def __init__(self, parent=None):
        super(RunThread, self).__init__(parent)

    def run(self):
        self._attach()

    def _attach(self):
        source = open('./js/hook_759654.js', 'r', encoding='utf8').read()
        session = frida.attach("wechat.exe")
        script = session.create_script(source)
        script.on('message', self.on_message)
        script.load()

    def on_message(self, message, data):
        if message['type'] == 'send':
            self.finishSignal.emit(message['payload']['xml'])

        elif message['type'] == 'error':
            self.finishSignal.emit(message)
