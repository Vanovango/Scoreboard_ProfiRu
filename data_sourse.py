
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_DataSource(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(502, 416)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_title = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Sitka Heading Semibold")
        font.setPointSize(30)
        self.label_title.setFont(font)
        self.label_title.setObjectName("label")
        self.verticalLayout.addWidget(self.label_title)
        self.pushButton_chose_file = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Sitka Heading Semibold")
        font.setPointSize(18)
        self.pushButton_chose_file.setFont(font)
        self.pushButton_chose_file.setObjectName("pushButton_2")
        self.verticalLayout.addWidget(self.pushButton_chose_file)
        self.pushButton_connect_google = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Sitka Heading Semibold")
        font.setPointSize(18)
        self.pushButton_connect_google.setFont(font)
        self.pushButton_connect_google.setObjectName("pushButton")
        self.verticalLayout.addWidget(self.pushButton_connect_google)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Источник данных"))
        self.label_title.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\">Выбор</p><p align=\"center\">источника данных</p><p align=\"center\">об участниках</p></body></html>"))
        self.pushButton_chose_file.setText(_translate("MainWindow", "Выбор фалйа"))
        self.pushButton_connect_google.setText(_translate("MainWindow", "Ссылка на GoogleSheets"))
