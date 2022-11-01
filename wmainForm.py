import sys
from xml.dom.minidom import parseString

from PyQt5 import QtCore, QtWidgets
from PyQt5.QtCore import QUrl
from PyQt5.QtGui import QDesktopServices
from PyQt5.QtWidgets import QMainWindow, QApplication, QTableWidgetItem, QPushButton

from TraceThread import RunThread
from wmain import Ui_WeiXinForm


class wmainForm(QMainWindow, Ui_WeiXinForm):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.th = RunThread()
        self.count = self.tableWidget.rowCount()
        self.initUi()
        self.listAll = []

    def initUi(self):
        self.pushButton.clicked.connect(self.startMoniter)

    def startMoniter(self):
        self.th.start()
        self.th.finishSignal.connect(self.wxInfo)
        self.textEdit.append("启动成功")

    def wxInfo(self, msg):
        listDYH = []
        if msg.strip().startswith("<msg>"):
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
                self.listAll.append(dictDYH)
            for element in listDYH:
                detail = QPushButton('查看')
                # detail.setStyleSheet("QPushButton(margin:3px)")
                detail.clicked.connect(self.urlClicked)

                self.tableWidget.setRowCount(self.count + 1)
                self.tableWidget.setItem(self.count, 0, QTableWidgetItem(name))
                self.tableWidget.setItem(self.count, 1, QTableWidgetItem(element['title']))
                self.tableWidget.setItem(self.count, 2, QTableWidgetItem(element['pub_time']))
                # ui.tableWidget.setItem(count, 3, QTableWidgetItem(element['url']))
                self.tableWidget.setCellWidget(self.count, 3, detail)
                self.count = self.count + 1

            self.activateWindow()
            self.setWindowState(self.windowState() & ~QtCore.Qt.WindowMinimized | QtCore.Qt.WindowActive)
            self.showNormal()

    def urlClicked(self):
        row = self.tableWidget.currentRow()
        url = QUrl(self[row]['url'])
        if not QDesktopServices.openUrl(url):
            QtWidgets.QMessageBox.warning('Open Url', 'Could not open url')


if __name__ == "__main__":
    app = QApplication(sys.argv)
    wmainForm = wmainForm()
    wmainForm.show()
    sys.exit(app.exec_())
