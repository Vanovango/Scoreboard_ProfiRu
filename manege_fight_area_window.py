
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_FightManageWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1400, 450)
        MainWindow.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.label_25 = QtWidgets.QLabel(self.centralwidget)
        self.label_25.setStyleSheet("background-color: rgb(0, 0, 0);\n"
"color: rgb(166, 255, 0);\n"
"font: 57 20pt \"Dubai Medium\";\n"
"\n"
"border-radius: 20px;\n"
"")
        self.label_25.setAlignment(QtCore.Qt.AlignCenter)
        self.label_25.setObjectName("label_25")
        self.gridLayout.addWidget(self.label_25, 0, 4, 1, 2)
        self.label_33 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Dubai Medium")
        font.setPointSize(30)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(7)
        self.label_33.setFont(font)
        self.label_33.setStyleSheet("\n"
"    font: 57 30pt \"Dubai Medium\";\n"
"")
        self.label_33.setAlignment(QtCore.Qt.AlignCenter)
        self.label_33.setObjectName("label_33")
        self.gridLayout.addWidget(self.label_33, 1, 0, 2, 4)
        self.label_20 = QtWidgets.QLabel(self.centralwidget)
        self.label_20.setStyleSheet("\n"
"    font: 57 30pt \"Dubai Medium\";\n"
"")
        self.label_20.setAlignment(QtCore.Qt.AlignCenter)
        self.label_20.setObjectName("label_20")
        self.gridLayout.addWidget(self.label_20, 1, 4, 1, 2)
        self.label_24 = QtWidgets.QLabel(self.centralwidget)
        self.label_24.setStyleSheet("\n"
"    font: 57 30pt \"Dubai Medium\";\n"
"")
        self.label_24.setAlignment(QtCore.Qt.AlignCenter)
        self.label_24.setObjectName("label_24")
        self.gridLayout.addWidget(self.label_24, 1, 6, 2, 5)
        self.label_31 = QtWidgets.QLabel(self.centralwidget)
        self.label_31.setStyleSheet("\n"
"    font: 57 60pt \"Dubai Medium\";\n"
"")
        self.label_31.setObjectName("label_31")
        self.gridLayout.addWidget(self.label_31, 2, 4, 3, 2)
        self.label_30 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Dubai Medium")
        font.setPointSize(15)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(7)
        self.label_30.setFont(font)
        self.label_30.setStyleSheet("\n"
"    font: 57 15pt \"Dubai Medium\";\n"
"")
        self.label_30.setObjectName("label_30")
        self.gridLayout.addWidget(self.label_30, 3, 0, 1, 2)
        self.label_28 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Dubai Medium")
        font.setPointSize(15)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(7)
        self.label_28.setFont(font)
        self.label_28.setStyleSheet("\n"
"    font: 57 15pt \"Dubai Medium\";\n"
"")
        self.label_28.setObjectName("label_28")
        self.gridLayout.addWidget(self.label_28, 3, 2, 3, 2)
        self.label_26 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Dubai Medium")
        font.setPointSize(15)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(7)
        self.label_26.setFont(font)
        self.label_26.setStyleSheet("\n"
"    font: 57 15pt \"Dubai Medium\";\n"
"")
        self.label_26.setObjectName("label_26")
        self.gridLayout.addWidget(self.label_26, 3, 6, 2, 3)
        self.label_23 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Dubai Medium")
        font.setPointSize(15)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(7)
        self.label_23.setFont(font)
        self.label_23.setStyleSheet("\n"
"    font: 57 15pt \"Dubai Medium\";\n"
"")
        self.label_23.setObjectName("label_23")
        self.gridLayout.addWidget(self.label_23, 3, 9, 3, 2)
        self.label_32 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Dubai Medium")
        font.setPointSize(15)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(7)
        self.label_32.setFont(font)
        self.label_32.setStyleSheet("\n"
"    font: 57 15pt \"Dubai Medium\";\n"
"")
        self.label_32.setObjectName("label_32")
        self.gridLayout.addWidget(self.label_32, 4, 0, 2, 2)
        self.pushButton_30 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_30.setStyleSheet("QPushButton {\n"
"    background-color: rgb(255, 80, 80);\n"
"    font: 57 15pt \"Dubai Medium\";\n"
"    border-radius: 15px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    \n"
"    background-color: rgb(198, 0, 0);\n"
"}\n"
"\n"
"")
        self.pushButton_30.setObjectName("pushButton_30")
        self.gridLayout.addWidget(self.pushButton_30, 5, 4, 1, 1)
        self.pushButton_31 = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Dubai Medium")
        font.setPointSize(15)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(7)
        self.pushButton_31.setFont(font)
        self.pushButton_31.setStyleSheet("QPushButton {\n"
"    \n"
"    background-color: rgb(139, 255, 133);\n"
"    font: 57 15pt \"Dubai Medium\";\n"
"    border-radius: 15px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    \n"
"    background-color: rgb(0, 193, 12);\n"
"}\n"
"\n"
"")
        self.pushButton_31.setObjectName("pushButton_31")
        self.gridLayout.addWidget(self.pushButton_31, 5, 5, 1, 1)
        self.label_27 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Dubai Medium")
        font.setPointSize(15)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(7)
        self.label_27.setFont(font)
        self.label_27.setStyleSheet("\n"
"    font: 57 15pt \"Dubai Medium\";\n"
"")
        self.label_27.setObjectName("label_27")
        self.gridLayout.addWidget(self.label_27, 5, 6, 1, 3)
        self.pushButton_32 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_32.setStyleSheet("QPushButton {\n"
"    \n"
"    \n"
"    background-color: rgb(255, 255, 255);\n"
"    font: 57 15pt \"Dubai Medium\";\n"
"\n"
"    border-radius: 15px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    \n"
"    background-color: rgb(255, 169, 169);\n"
"}\n"
"\n"
"")
        self.pushButton_32.setObjectName("pushButton_32")
        self.gridLayout.addWidget(self.pushButton_32, 6, 0, 1, 1)
        self.pushButton_38 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_38.setStyleSheet("QPushButton {\n"
"    \n"
"    \n"
"    background-color: rgb(255, 255, 255);\n"
"    font: 57 15pt \"Dubai Medium\";\n"
"\n"
"    border-radius: 15px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(217, 217, 217);\n"
"}\n"
"\n"
"")
        self.pushButton_38.setObjectName("pushButton_38")
        self.gridLayout.addWidget(self.pushButton_38, 6, 1, 1, 1)
        self.pushButton_37 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_37.setStyleSheet("QPushButton {\n"
"    \n"
"    \n"
"    background-color: rgb(255, 255, 255);\n"
"    font: 57 15pt \"Dubai Medium\";\n"
"\n"
"    border-radius: 15px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(217, 217, 217);\n"
"}\n"
"\n"
"")
        self.pushButton_37.setObjectName("pushButton_37")
        self.gridLayout.addWidget(self.pushButton_37, 6, 2, 1, 1)
        self.pushButton_35 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_35.setStyleSheet("QPushButton {\n"
"    \n"
"    \n"
"    background-color: rgb(255, 255, 255);\n"
"    font: 57 15pt \"Dubai Medium\";\n"
"\n"
"    border-radius: 15px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(217, 217, 217);\n"
"}\n"
"\n"
"")
        self.pushButton_35.setObjectName("pushButton_35")
        self.gridLayout.addWidget(self.pushButton_35, 6, 3, 1, 1)
        self.label_29 = QtWidgets.QLabel(self.centralwidget)
        self.label_29.setStyleSheet("\n"
"    font: 57 30pt \"Dubai Medium\";\n"
"")
        self.label_29.setObjectName("label_29")
        self.gridLayout.addWidget(self.label_29, 6, 4, 1, 2)
        self.pushButton_28 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_28.setStyleSheet("QPushButton {\n"
"    \n"
"    \n"
"    background-color: rgb(255, 255, 255);\n"
"    font: 57 15pt \"Dubai Medium\";\n"
"\n"
"    border-radius: 15px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    \n"
"    background-color: rgb(255, 169, 169);\n"
"}\n"
"\n"
"")
        self.pushButton_28.setObjectName("pushButton_28")
        self.gridLayout.addWidget(self.pushButton_28, 6, 6, 1, 1)
        self.pushButton_27 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_27.setStyleSheet("QPushButton {\n"
"    \n"
"    \n"
"    background-color: rgb(255, 255, 255);\n"
"    font: 57 15pt \"Dubai Medium\";\n"
"\n"
"    border-radius: 15px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(217, 217, 217);\n"
"}\n"
"\n"
"")
        self.pushButton_27.setObjectName("pushButton_27")
        self.gridLayout.addWidget(self.pushButton_27, 6, 7, 1, 1)
        self.pushButton_39 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_39.setStyleSheet("QPushButton {\n"
"    \n"
"    \n"
"    background-color: rgb(255, 255, 255);\n"
"    font: 57 15pt \"Dubai Medium\";\n"
"\n"
"    border-radius: 15px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(217, 217, 217);\n"
"}\n"
"\n"
"")
        self.pushButton_39.setObjectName("pushButton_39")
        self.gridLayout.addWidget(self.pushButton_39, 6, 8, 1, 2)
        self.pushButton_33 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_33.setStyleSheet("QPushButton {\n"
"    \n"
"    \n"
"    background-color: rgb(255, 255, 255);\n"
"    font: 57 15pt \"Dubai Medium\";\n"
"\n"
"    border-radius: 15px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(217, 217, 217);\n"
"}\n"
"\n"
"")
        self.pushButton_33.setObjectName("pushButton_33")
        self.gridLayout.addWidget(self.pushButton_33, 6, 10, 1, 1)
        self.pushButton_36 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_36.setStyleSheet("QPushButton {\n"
"    \n"
"    \n"
"    background-color: rgb(255, 255, 255);\n"
"    font: 57 15pt \"Dubai Medium\";\n"
"\n"
"    border-radius: 15px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    \n"
"    background-color: rgb(255, 87, 87);\n"
"}\n"
"\n"
"")
        self.pushButton_36.setObjectName("pushButton_36")
        self.gridLayout.addWidget(self.pushButton_36, 7, 0, 1, 4)
        self.label_22 = QtWidgets.QLabel(self.centralwidget)
        self.label_22.setStyleSheet("color: #fff;\n"
"background: #000000;\n"
"font: 57 30pt \"Dubai Medium\";\n"
"\n"
"border-radius: 15px;\n"
"")
        self.label_22.setAlignment(QtCore.Qt.AlignCenter)
        self.label_22.setObjectName("label_22")
        self.gridLayout.addWidget(self.label_22, 7, 4, 1, 1)
        self.label_21 = QtWidgets.QLabel(self.centralwidget)
        self.label_21.setStyleSheet("color: #fff;\n"
"background: #000000;\n"
"font: 57 30pt \"Dubai Medium\";\n"
"\n"
"border-radius: 15px;\n"
"")
        self.label_21.setAlignment(QtCore.Qt.AlignCenter)
        self.label_21.setObjectName("label_21")
        self.gridLayout.addWidget(self.label_21, 7, 5, 1, 1)
        self.pushButton_29 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_29.setStyleSheet("QPushButton {\n"
"    \n"
"    \n"
"    background-color: rgb(255, 255, 255);\n"
"    font: 57 15pt \"Dubai Medium\";\n"
"\n"
"    border-radius: 15px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    \n"
"    background-color: rgb(255, 87, 87);\n"
"}\n"
"\n"
"")
        self.pushButton_29.setObjectName("pushButton_29")
        self.gridLayout.addWidget(self.pushButton_29, 7, 6, 1, 5)
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(23)
        self.line_2.setFont(font)
        self.line_2.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.line_2.setLineWidth(-2)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.gridLayout.addWidget(self.line_2, 8, 0, 1, 12)
        self.pushButton_34 = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Dubai Medium")
        font.setPointSize(15)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(7)
        self.pushButton_34.setFont(font)
        self.pushButton_34.setStyleSheet("QPushButton {\n"
"    background-color: rgb(0, 0, 0);\n"
"    color: rgb(166, 255, 0);\n"
"    font: 57 15pt \"Dubai Medium\";\n"
"\n"
"    border-radius: 30px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(76, 76, 76);\n"
"}\n"
"\n"
"")
        self.pushButton_34.setObjectName("pushButton_34")
        self.gridLayout.addWidget(self.pushButton_34, 1, 11, 7, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_25.setText(_translate("MainWindow", "Ковер №1"))
        self.label_33.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:600;\">Иванов Иван Иванович</span></p></body></html>"))
        self.label_20.setText(_translate("MainWindow", "Время"))
        self.label_24.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:600;\">Петров Петр Петрович</span></p></body></html>"))
        self.label_31.setText(_translate("MainWindow", "00:00"))
        self.label_30.setText(_translate("MainWindow", "Весовая категория - 22"))
        self.label_28.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\">Школа</p><p align=\"center\">Одинцовская СОШ 3</p></body></html>"))
        self.label_26.setText(_translate("MainWindow", "Весовая категория - 28"))
        self.label_23.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\">Школа</p><p align=\"center\">Химки 31 школа</p></body></html>"))
        self.label_32.setText(_translate("MainWindow", "Год рождения - 19.02.2005"))
        self.pushButton_30.setText(_translate("MainWindow", "Пауза"))
        self.pushButton_31.setText(_translate("MainWindow", "Продолжить"))
        self.label_27.setText(_translate("MainWindow", "Год рождения - 31.07.2005"))
        self.pushButton_32.setText(_translate("MainWindow", "ШИДО - 0"))
        self.pushButton_38.setText(_translate("MainWindow", "ЮКО - 0"))
        self.pushButton_37.setText(_translate("MainWindow", "ВАЗАРИ - 0"))
        self.pushButton_35.setText(_translate("MainWindow", "ИППОН - 0"))
        self.label_29.setText(_translate("MainWindow", "Общий счет"))
        self.pushButton_28.setText(_translate("MainWindow", "ШИДО - 0"))
        self.pushButton_27.setText(_translate("MainWindow", "ЮКО - 0"))
        self.pushButton_39.setText(_translate("MainWindow", "ВАЗАРИ - 0"))
        self.pushButton_33.setText(_translate("MainWindow", "ИППОН - 0"))
        self.pushButton_36.setText(_translate("MainWindow", "ХАНСОКУ МАКЕ"))
        self.label_22.setText(_translate("MainWindow", "0"))
        self.label_21.setText(_translate("MainWindow", "0"))
        self.pushButton_29.setText(_translate("MainWindow", "ХАНСОКУ МАКЕ"))
        self.pushButton_34.setText(_translate("MainWindow", "Вывести\n"
"табло"))


