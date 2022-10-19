import sys
from PySide6.QtCore import Qt, QUrl
from PySide6.QtGui import QIcon, QPixmap, QDesktopServices
from PySide6 import QtWidgets

servants = [("EMIYA", "Archer", "https://gamepress.gg/grandorder/servant/emiya"),
            ("Gilgamesh", "Archer", "https://gamepress.gg/grandorder/servant/gilgamesh"),
            ("Cu Chulainn", "Lancer", "https://gamepress.gg/grandorder/servant/cu-chulainn"),
            ("Alexander", "Rider", "https://gamepress.gg/grandorder/servant/alexander"),
            (
            "Zhuge Liang (El-Melloi II)", "Caster", "https://gamepress.gg/grandorder/servant/zhuge-liang-el-melloi-ii"),
            ("Cu Chulainn (Caster)", "Caster", "https://gamepress.gg/grandorder/servant/cu-chulainn-caster"),
            (
            "Solomon (Grand Caster)", "Caster (Grand)", "https://gamepress.gg/grandorder/servant/solomon-grand-caster"),
            ("Arjuna", "Archer", "https://gamepress.gg/grandorder/servant/arjuna"),
            ("Karna", "Lancer", "https://gamepress.gg/grandorder/servant/karna"),
            ("Kid Gilgamesh", "Archer", "https://gamepress.gg/grandorder/servant/kid-gilgamesh"),
            ("Edmond Dantes", "Avenger", "https://gamepress.gg/grandorder/servant/edmond-dantes"),
            ("Cu Chulainn (Alter)", "Berserker", "https://gamepress.gg/grandorder/servant/cu-chulainn-alter")]


class MyWidget(QtWidgets.QTableWidget):
    def __init__(self):
        super().__init__()
        self.setRowCount(len(servants))
        self.setColumnCount(len(servants[0]) + 1)
        self.setHorizontalHeaderLabels(["Icon", "Name", "Class", "Go to details"])
        self.servantUrl = []
        for i in range(len(servants)):
            btn = QtWidgets.QPushButton(">>")
            btn.setFixedSize(50, 30)
            btn.clicked.connect(self.open_webbrowser)
            self.servantUrl.append(btn)

        for i, (name, _class, _url) in enumerate(servants):
            servantIcon = QtWidgets.QLabel("")
            servantIcon.setPixmap(QPixmap("%s.png" % name))
            servantName = QtWidgets.QTableWidgetItem(name)
            servantClass = QtWidgets.QTableWidgetItem(_class)
            self.setCellWidget(i, 0, servantIcon)
            self.setItem(i, 1, servantName)
            self.setItem(i, 2, servantClass)
            self.setCellWidget(i, 3, self.servantUrl[i])
            self.setRowHeight(i, servantIcon.height())

        self.resizeColumnsToContents()

    def open_webbrowser(self):
        r = self.currentRow()
        url = QUrl(servants[r][2])
        if not QDesktopServices.openUrl(url):
            QtWidgets.QMessageBox.warning('Open Url', 'Could not open url')


if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    QtWidgets.QApplication.setApplicationName("Hello")
    QtWidgets.QApplication.setWindowIcon(QIcon("214.png"))
    table = MyWidget()
    table.show()
    sys.exit(app.exec())
