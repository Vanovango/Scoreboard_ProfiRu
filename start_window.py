
from PyQt5 import QtCore, QtGui, QtWidgets



class Ui_StartWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(600, 400)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.pushButton_add_fight_area = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Sitka Heading Semibold")
        font.setPointSize(16)
        self.pushButton_add_fight_area.setFont(font)
        self.pushButton_add_fight_area.setObjectName("pushButton_add_fight_area")
        self.gridLayout.addWidget(self.pushButton_add_fight_area, 1, 0, 1, 1)
        self.pushButton_close_all = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Sitka Heading Semibold")
        font.setPointSize(16)
        self.pushButton_close_all.setFont(font)
        self.pushButton_close_all.setObjectName("pushButton_close_all")
        self.gridLayout.addWidget(self.pushButton_close_all, 4, 0, 1, 1)
        self.label_title = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Sitka Display Semibold")
        font.setPointSize(28)
        self.label_title.setFont(font)
        self.label_title.setObjectName("label_title")
        self.gridLayout.addWidget(self.label_title, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Главная"))
        self.pushButton_add_fight_area.setText(_translate("MainWindow", "Добавить мониторинг ковра"))
        self.pushButton_close_all.setText(_translate("MainWindow", "Закрыть все окна"))
        self.label_title.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\">Табло </p><p align=\"center\">для проведения </p><p align=\"center\">соревнований по Дзюдо</p></body></html>"))

