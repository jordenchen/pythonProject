#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: anchen
# @Date:   2022-09-30 13:06:26
# @Last Modified by:   anchen
# @Last Modified time: 2022-10-20 13:55:46
#  [edi]
# 基址 78A1EC6E   hook偏址5AF29654  - 5A7D0000 = 759654

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
        var ModAddress = Process.findModuleByName('wechatwin.dll');
        var hookAddress = ModAddress.base.add('0x759654');
        Interceptor.attach(hookAddress , {
            onEnter:function(args) {
                var esi= this.context.esi;
                var xmlPro = Memory.readPointer(esi);
                var xml = Memory.readUtf16String(Memory.readPointer(xmlPro.add('0x70')));
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
    main('wechat.exe')
