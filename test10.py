#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: anchen
# @Date:   2022-09-30 13:06:26
# @Last Modified by:   anchen
# @Last Modified time: 2022-10-20 13:55:46
#  79AD2FC8 79640000 492FC8

from __future__ import print_function
import frida
import sys


def on_message(message, data):
    if message['type'] == 'send':
        # print(message)
        # print(message['payload']['resource'])
        print(message['payload']['xml'])
        # print(message['payload']['xml1'])
        # print(data)
        # base = message['payload']['wxid']
        # size = int(message['payload']['text'])
        # print(hex(base), size)
    elif message['type'] == 'error':
        print(message)
        # for i in message:
        #     if i == "type":
        #         print("[*] %s" % "error:")
        #         continue
        #     if type(message[i]) is str:
        #         print("[*] %s" %
        #               i + ":\n    {0}".format(message[i].replace('\t', '    ')))
        #     else:
        #         print("[*] %s" %
        #               i + ":\n    {0}".format(message[i]))
    else:
        print(message)


# F为公众号消息
def main(target_process):
    session = frida.attach(target_process)
    print("公众号")
    script = session.create_script("""
        var ModAddress = Process.findModuleByName('wechatwin.dll');
        var hookAddress = ModAddress.base.add('0x5BECF2');
        console.log('kaishi');
        Interceptor.attach(hookAddress , {
            onEnter:function(args) {
                var esp = this.context.esp;
                console.log('hookchenggong');
                var msgUni = Memory.readPointer(esp.add('0x24'));
                var msg = Memory.readPointer(msgUni.add('0x70'));
                var xml = Memory.readUtf16String(msg);
            
              
                send({'xml':xml});
            }
        } );
        """)
    script.on('message', on_message)
    script.load()
    print("[!] Ctrl+D on UNIX, Ctrl+Z on Windows/cmd.exe to detach from instrumented program.\n\n")
    sys.stdin.read()
    session.detach()


if __name__ == '__main__':
    main('WeChat.exe')
