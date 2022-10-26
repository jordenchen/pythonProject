# This is a sample Python script.
import time
# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

from xml.dom.minidom import parseString
import sys
from PyQt5 import QtWidgets, QtCore
from PyQt5.QtCore import QUrl
from PyQt5.QtGui import QDesktopServices
from PyQt5.QtWidgets import QTableWidgetItem, QPushButton

from logthread import logthread
from weixin import Ui_Form


listALl = []


def buttonClicked():
    print('clicked')
    row = ui.tableWidget.currentRow()
    print("row"+str(row))
    # column = ui.tableWidget.currentColumn()
    print(listALl)
    url = QUrl(listALl[row]['url'])
    if not QDesktopServices.openUrl(url):
        QtWidgets.QMessageBox.warning('Open Url', 'Could not open url')


def log(msg):
    global count
    print("收到微信信息")
    listDYH = []
    if msg.strip().startswith("<msg>"):
        print("收到微信公众号信息")
        dom = parseString(msg)
        name = dom.getElementsByTagName('appname')[0].childNodes[0].nodeValue.strip()
        print("name:" + name)
        items = dom.getElementsByTagName('item')
        for item in items:
            dictDYH = {}
            dictDYH['title'] = item.getElementsByTagName('title')[0].childNodes[0].nodeValue.replace('![CDATA[', '') \
                .replace(']]', '')
            print("title:" + dictDYH['title'])

            pushTime = item.getElementsByTagName('pub_time')[0].childNodes[0].nodeValue.strip()
            dictDYH['pub_time'] = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(int(pushTime)))
            print("pub_time:" + dictDYH['pub_time'])
            
            dictDYH['url'] = item.getElementsByTagName('url')[0].childNodes[0].nodeValue.replace('![CDATA[', '') \
                .replace(']]', '')
            print("url:" + dictDYH['url'])
            listDYH.append(dictDYH)
            listALl.append(dictDYH)
        global count
        for element in listDYH:
            detail = QPushButton('查看')
            # detail.setStyleSheet("QPushButton(margin:3px)")
            detail.clicked.connect(buttonClicked)

            print(count)
            ui.tableWidget.setRowCount(count + 1)

            ui.tableWidget.setItem(count, 0, QTableWidgetItem(name))
            ui.tableWidget.setItem(count, 1, QTableWidgetItem(element['title']))
            ui.tableWidget.setItem(count, 2, QTableWidgetItem(element['pub_time']))
            # ui.tableWidget.setItem(count, 3, QTableWidgetItem(element['url']))
            ui.tableWidget.setCellWidget(count, 3, detail)

            count = count + 1

        mainwindow.activateWindow()
        mainwindow.setWindowState(mainwindow.windowState() & ~QtCore.Qt.WindowMinimized | QtCore.Qt.WindowActive)
        mainwindow.showNormal()


def start():
    thread.finishSignal.connect(log)
    thread.start()
    ui.textEdit.append("启动成功")


if __name__ == "__main__":
    thread = logthread()
    app = QtWidgets.QApplication(sys.argv)  # 创建一个qapplication，也就是你要开发的软件app
    mainwindow = QtWidgets.QMainWindow()  # 创建一个qmainwindow，用来装载你需要的各种组件、控件
    ui = Ui_Form(mainwindow)  # ui是你创建的ui类的实例化对象
    mainwindow.setWindowTitle("微信订阅号监控")
    # ui.setupUi(mainwindow)  # 执行类中的setupui方法，方法的参数是第二步中创建的qmainwindow
    count = ui.tableWidget.rowCount()
    ui.pushButton.clicked.connect(start)

    # ui.tableWidget.setItem(0, 0, QTableWidgetItem("康美中药网"))
    # ui.tableWidget.setItem(0, 1, QTableWidgetItem("医生垫了3000块！12年后，患者千里送还"))
    # ui.tableWidget.setItem(0, 2, QTableWidgetItem("dd"))
    # ui.tableWidget.setItem(0, 3, QTableWidgetItem("http://www.badiu.com"))


    mainwindow.show()  # 执行qmainwindow的show()方法，显示这个qmainwindow
    sys.exit(app.exec_())  # 使用exit()或者点击关闭按钮退出qapplication


