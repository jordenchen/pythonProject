# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

from xml.dom.minidom import parseString
import sys
from PyQt5 import QtWidgets

from logthread import logthread
from weixin import Ui_Form


def log(msg):
    # ui.textEdit.append(msg)
    if msg.strip().startswith("<msg>"):
        dom = parseString(msg)
        name = dom.getElementsByTagName('appname')


def start():
    thread.finishSignal.connect(log)
    thread.start()


if __name__ == "__main__":
    thread = logthread()
    app = QtWidgets.QApplication(sys.argv)  # 创建一个qapplication，也就是你要开发的软件app
    mainwindow = QtWidgets.QMainWindow()  # 创建一个qmainwindow，用来装载你需要的各种组件、控件
    ui = Ui_Form(mainwindow)  # ui是你创建的ui类的实例化对象
    # ui.setupUi(mainwindow)  # 执行类中的setupui方法，方法的参数是第二步中创建的qmainwindow
    rowCount = ui.tableWidget.rowCount()

    ui.pushButton.clicked.connect(start)

    mainwindow.show()  # 执行qmainwindow的show()方法，显示这个qmainwindow
    sys.exit(app.exec_())  # 使用exit()或者点击关闭按钮退出qapplication



