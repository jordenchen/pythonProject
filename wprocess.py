# -*- coding: utf-8 -*-
import sys

# Form implementation generated from reading ui file 'weixin2.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIcon
import ctypes

ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID("myappid")  # 解决任务栏图标问题，不知道原理


class Ui_WeiXinProcess(QtWidgets.):

    def setupUi(self, Form):
        Form.setObjectName("FormProcess")
        Form.resize(1000, 501)
        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate

