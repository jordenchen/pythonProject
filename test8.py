#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: anchen
# @Date:   2022-09-30 13:06:26
# @Last Modified by:   anchen
# @Last Modified time: 2022-10-20 13:55:46
#  610A0000  6165EC6E  5BEC6E

from __future__ import print_function

from xml.dom.minidom import parseString

import frida
import sys


def on_message(message, data):
    if message['type'] == 'send':
        # print(message['payload']['resource'])
        # print(message['payload']['xml'])
        print(message['payload']['xml_li'])
        for msg in message['payload']['xml_li']:
            if msg.strip().startswith("<msg>"):
                dom = parseString(msg)
                name = dom.getElementsByTagName('appname')[0].childNodes[0].nodeValue.strip()
                print(name)
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
        var ModAddress = Process.findModuleByName('WeChatWin.dll');
        var hookAddress = ModAddress.base.add('0x5FE9C0');
        Interceptor.attach(hookAddress, {
            onEnter: function (args) {
                console.log('hook-start');
                var xml_li = [];
                var edi = this.context.edi;
                var edi1 = Memory.readInt(edi);
                var edi2 = Memory.readInt(edi.add('0x4'));
                var num = (edi2 - edi1) /672 ;
                for(var i=0; i<num; i++){
                    var leiji = (112 + 672*i);
                    var pointer_jia = '0x' + leiji.toString(16);
                    console.log(pointer_jia);
                    var xml = Memory.readUtf16String(Memory.readPointer(Memory.readPointer(edi).add(pointer_jia)));
                    xml_li.push(xml);
                 }
                send({'xml_li': xml_li});
            }
        });
        """)
    script.on('message', on_message)
    script.load()
    print("[!] Ctrl+D on UNIX, Ctrl+Z on Windows/cmd.exe to detach from instrumented program.\n\n")
    sys.stdin.read()
    session.detach()


if __name__ == '__main__':
    main('WeChat.exe')
