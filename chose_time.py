from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_ChoseTime(object):
    def setupUi(self, ChoseTime):
        ChoseTime.setObjectName("ChoseTime")
        ChoseTime.resize(260, 231)

        self.timeEdit = QtWidgets.QTimeEdit(ChoseTime)
        self.timeEdit.setGeometry(QtCore.QRect(40, 90, 181, 51))
        font = QtGui.QFont()
        font.setPointSize(30)
        self.timeEdit.setFont(font)
        self.timeEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.timeEdit.setCurrentSection(QtWidgets.QDateTimeEdit.SecondSection)
        self.timeEdit.setObjectName("timeEdit")

        self.label = QtWidgets.QLabel(ChoseTime)
        self.label.setGeometry(QtCore.QRect(30, 20, 201, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")

        self.pushButton_ok_time = QtWidgets.QPushButton(ChoseTime)
        self.pushButton_ok_time.setGeometry(QtCore.QRect(60, 170, 141, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.pushButton_ok_time.setFont(font)
        self.pushButton_ok_time.setObjectName("pushButton")

        self.retranslateUi(ChoseTime)
        QtCore.QMetaObject.connectSlotsByName(ChoseTime)

    def retranslateUi(self, ChoseTime):
        _translate = QtCore.QCoreApplication.translate
        ChoseTime.setWindowTitle(_translate("ChoseTime", "Выбор времени"))
        self.timeEdit.setDisplayFormat(_translate("ChoseTime", "mm:ss"))
        self.label.setText(_translate("ChoseTime", "Укажите время"))
        self.pushButton_ok_time.setText(_translate("ChoseTime", "Ок"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ChoseTime = QtWidgets.QWidget()
    ui = Ui_ChoseTime()
    ui.setupUi(ChoseTime)
    ChoseTime.show()
    sys.exit(app.exec_())
