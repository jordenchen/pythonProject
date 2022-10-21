#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: anchen
# @Date:   2022-09-30 13:06:26
# @Last Modified by:   anchen
# @Last Modified time: 2022-10-20 13:55:46
#  [edi]
#   hook偏址5AD8ECED  - 5A7D0000 = 5BECED  微信运行报错

from __future__ import print_function
import frida
import sys


def on_message(message, data):
    if message['type'] == 'send':
        print(message)
        print(message['payload']['xml'])
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


def main(target_process):
    session = frida.attach(target_process)
    script = session.create_script("""
        var ModAddress = Process.findModuleByName('WeChatWin.dll');
        var hookAddress = ModAddress.base.add('0x5BECED');
        Interceptor.attach(hookAddress , {
            onEnter:function(args) {
                var ebx = this.context.ebx;
                var xmlPro = Memory.readPointer(ebx.add('0x28'));
                var xmlPro2 = Memory.readPointer(xmlPro)
                var xml = Memory.readUtf16String(xmlPro2.add('0x70'));
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
