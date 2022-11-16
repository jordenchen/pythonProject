#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: anchen
# @Date:   2022-09-30 13:06:26
# @Last Modified by:   anchen
# @Last Modified time: 2022-10-20 13:55:46
#  [edi]
#   hook偏址5AD8ECED  - 5A7D0000 = 5BECED  微信运行报错
# 66B29654 - 663D0000 = 0x759654


from __future__ import print_function
import frida
import sys


def on_message(message, data):
    if message['type'] == 'send':
        print('类型')
        print(message['payload']['leixing'])
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


# F为公众号消息
def main(target_process):
    # session = frida.attach(target_process)
    process_list = frida.get_local_device().enumerate_processes()
    # process_list = device.enumerate_processes()
    weixin_list = [i.pid for i in process_list if i.name.lower() == target_process.lower()]
    print(weixin_list)

if __name__ == '__main__':
    main('WeChat.exe')
