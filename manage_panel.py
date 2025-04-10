from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import (QMainWindow, QPushButton, QLabel, QVBoxLayout, QWidget,
                             QTimeEdit, QDialog, QMessageBox, QHBoxLayout)
from PyQt5.QtCore import QTimer, QTime, Qt

from scoreborde_user import Ui_Scoreboard


class Ui_ManagePanel(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1386, 652)
        MainWindow.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.combobox_full_name_left = QtWidgets.QComboBox(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Dubai Medium")
        font.setPointSize(20)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(7)
        self.combobox_full_name_left.setFont(font)
        self.combobox_full_name_left.setStyleSheet("\n"
"    font: 57 20pt \"Dubai Medium\";\n"
"")
        self.combobox_full_name_left.setObjectName("label_full_name_left")
        self.verticalLayout_2.addWidget(self.combobox_full_name_left)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_weight_category_left = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Dubai Medium")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(7)
        self.label_weight_category_left.setFont(font)
        self.label_weight_category_left.setStyleSheet("background-color: rgb(221, 221, 221);\n"
"font: 57 12pt \"Dubai Medium\";\n"
"\n"
"border-radius: 10px;\n"
"border: 1px solid black;\n"
"\n"
"padding-right: 10px;\n"
"padding-left: 10px;")
        self.label_weight_category_left.setAlignment(QtCore.Qt.AlignCenter)
        self.label_weight_category_left.setObjectName("label_weight_category_left")
        self.verticalLayout_3.addWidget(self.label_weight_category_left)
        self.label_date_of_birth_left = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Dubai Medium")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(7)
        self.label_date_of_birth_left.setFont(font)
        self.label_date_of_birth_left.setStyleSheet("background-color: rgb(221, 221, 221);\n"
"font: 57 12pt \"Dubai Medium\";\n"
"\n"
"border-radius: 10px;\n"
"border: 1px solid black;")
        self.label_date_of_birth_left.setAlignment(QtCore.Qt.AlignCenter)
        self.label_date_of_birth_left.setObjectName("label_date_of_birth_left")
        self.verticalLayout_3.addWidget(self.label_date_of_birth_left)
        self.horizontalLayout_2.addLayout(self.verticalLayout_3)
        self.label_team_left = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Dubai Medium")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(7)
        self.label_team_left.setFont(font)
        self.label_team_left.setStyleSheet("background-color: rgb(221, 221, 221);\n"
"font: 57 12pt \"Dubai Medium\";\n"
"\n"
"border-radius: 10px;\n"
"border: 1px solid black;\n"
"\n"
"padding-right: 10px;\n"
"padding-left: 10px;")
        self.label_team_left.setObjectName("label_team_left")
        self.horizontalLayout_2.addWidget(self.label_team_left)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.label_pass_left = QtWidgets.QLabel(self.centralwidget)
        self.label_pass_left.setText("")
        self.label_pass_left.setObjectName("label_pass_left")
        self.verticalLayout_2.addWidget(self.label_pass_left)
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setContentsMargins(10, -1, 10, -1)
        self.formLayout.setHorizontalSpacing(20)
        self.formLayout.setVerticalSpacing(10)
        self.formLayout.setObjectName("formLayout")
        self.pushButton_YKO_left = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Sitka Heading Semibold")
        font.setPointSize(16)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(7)
        self.pushButton_YKO_left.setFont(font)
        self.pushButton_YKO_left.setStyleSheet("QPushButton {\n"
"    \n"
"    \n"
"    background-color: rgb(255, 255, 255);\n"
"    \n"
"    font: 63 16pt \"Sitka Heading Semibold\";\n"
"\n"
"    border-radius: 10px;\n"
"    \n"
"    border-color: rgb(0, 0, 0);\n"
"    \n"
"    width: 200px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(217, 217, 217);\n"
"}\n"
"\n"
"")
        self.pushButton_YKO_left.setObjectName("pushButton_YKO_left")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.pushButton_YKO_left)
        self.label_YKO_score_left = QtWidgets.QLabel(self.centralwidget)
        self.label_YKO_score_left.setStyleSheet("\n"
"\n"
"font: 63 20pt \"Sitka Heading Semibold\";")
        self.label_YKO_score_left.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.label_YKO_score_left.setObjectName("label_IPPON_score_left")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.label_YKO_score_left)
        self.pushButton_VAZARI_left = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Sitka Heading Semibold")
        font.setPointSize(16)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(7)
        self.pushButton_VAZARI_left.setFont(font)
        self.pushButton_VAZARI_left.setStyleSheet("QPushButton {\n"
"    \n"
"    \n"
"    background-color: rgb(255, 255, 255);\n"
"    \n"
"    font: 63 16pt \"Sitka Heading Semibold\";\n"
"\n"
"    border-radius: 10px;\n"
"    \n"
"    border-color: rgb(0, 0, 0);\n"
"\n"
"    width: 200px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(217, 217, 217);\n"
"}\n"
"\n"
"")
        self.pushButton_VAZARI_left.setObjectName("pushButton_IPPON_left")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.pushButton_VAZARI_left)
        self.label_VAZARI_score_left = QtWidgets.QLabel(self.centralwidget)
        self.label_VAZARI_score_left.setStyleSheet("\n"
"\n"
"font: 63 20pt \"Sitka Heading Semibold\";")
        self.label_VAZARI_score_left.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.label_VAZARI_score_left.setObjectName("label_VAZARI_score_left")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.label_VAZARI_score_left)
        self.pushButton_IPPON_left = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Sitka Heading Semibold")
        font.setPointSize(16)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(7)
        self.pushButton_IPPON_left.setFont(font)
        self.pushButton_IPPON_left.setStyleSheet("QPushButton {\n"
"    \n"
"    \n"
"    background-color: rgb(255, 255, 255);\n"
"    \n"
"    font: 63 16pt \"Sitka Heading Semibold\";\n"
"\n"
"    border-radius: 10px;\n"
"    \n"
"    border-color: rgb(0, 0, 0);\n"
"\n"
"    width: 200px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(217, 217, 217);\n"
"}\n"
"\n"
"")
        self.pushButton_IPPON_left.setObjectName("pushButton_VAZARI_left")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.pushButton_IPPON_left)
        self.label_IPPON_score_left = QtWidgets.QLabel(self.centralwidget)
        self.label_IPPON_score_left.setStyleSheet("\n"
"\n"
"font: 63 20pt \"Sitka Heading Semibold\";")
        self.label_IPPON_score_left.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.label_IPPON_score_left.setObjectName("label_SHIDO_score_left")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.label_IPPON_score_left)
        self.pushButton_SHIDO_left = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Sitka Heading Semibold")
        font.setPointSize(16)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(7)
        self.pushButton_SHIDO_left.setFont(font)
        self.pushButton_SHIDO_left.setStyleSheet("QPushButton {\n"
"    \n"
"    \n"
"    background-color: rgb(255, 255, 255);\n"
"    \n"
"    font: 63 16pt \"Sitka Heading Semibold\";\n"
"\n"
"    border-radius: 10px;\n"
"    \n"
"    border-color: rgb(0, 0, 0);\n"
"\n"
"    width: 200px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    \n"
"    background-color: rgb(255, 169, 169);\n"
"}\n"
"\n"
"\n"
"")
        self.pushButton_SHIDO_left.setObjectName("pushButton_SHIDO_left")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.pushButton_SHIDO_left)
        self.label_SHIDO_score_left = QtWidgets.QLabel(self.centralwidget)
        self.label_SHIDO_score_left.setStyleSheet("\n"
"\n"
"font: 63 20pt \"Sitka Heading Semibold\";")
        self.label_SHIDO_score_left.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.label_SHIDO_score_left.setObjectName("label_YKO_score_left")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.label_SHIDO_score_left)
        self.verticalLayout_2.addLayout(self.formLayout)
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Sitka Heading Semibold")
        font.setPointSize(20)
        self.label_8.setFont(font)
        self.label_8.setAlignment(QtCore.Qt.AlignCenter)
        self.label_8.setObjectName("label_8")
        self.verticalLayout_2.addWidget(self.label_8)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.pushButton_left_stopwatch_start = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_left_stopwatch_start.setStyleSheet("QPushButton {\n"
"    \n"
"    \n"
"    background-color: rgb(255, 255, 255);\n"
"    \n"
"    font: 63 16pt \"Sitka Heading Semibold\";\n"
"\n"
"    border-radius: 10px;\n"
"\n"
"    padding: 10px;\n"
"    \n"
"}\n"
"\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(255, 240, 176);\n"
"}\n"
"\n"
"")
        self.pushButton_left_stopwatch_start.setObjectName("pushButton")
        self.horizontalLayout_4.addWidget(self.pushButton_left_stopwatch_start)
        self.label_stopwatch_time_left = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Sitka Heading Semibold")
        font.setPointSize(20)
        self.label_stopwatch_time_left.setFont(font)
        self.label_stopwatch_time_left.setAlignment(QtCore.Qt.AlignCenter)
        self.label_stopwatch_time_left.setObjectName("label_7")
        self.horizontalLayout_4.addWidget(self.label_stopwatch_time_left)
        self.pushButton_left_stopwatch_stop = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_left_stopwatch_stop.setStyleSheet("QPushButton {\n"
"    \n"
"    \n"
"    background-color: rgb(255, 255, 255);\n"
"    \n"
"    font: 63 16pt \"Sitka Heading Semibold\";\n"
"\n"
"    border-radius: 10px;\n"
"\n"
"    padding: 10px;\n"
"    \n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(255, 240, 176);\n"
"}\n"
"\n"
"")
        self.pushButton_left_stopwatch_stop.setObjectName("pushButton_2")
        self.horizontalLayout_4.addWidget(self.pushButton_left_stopwatch_stop)
        self.verticalLayout_2.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_3.addLayout(self.verticalLayout_2)
        self.verticalLayout_11 = QtWidgets.QVBoxLayout()
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setText("")
        self.label.setObjectName("label")
        self.verticalLayout_11.addWidget(self.label)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Sitka Heading Semibold")
        font.setPointSize(30)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignHCenter)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_11.addWidget(self.label_2)
        self.label_sum_score_left = QtWidgets.QLabel(self.centralwidget)
        self.label_sum_score_left.setStyleSheet("color: #fff;\n"
"background: #000000;\n"
"font: 57 30pt \"Dubai Medium\";\n"
"\n"
"border-radius: 15px;\n"
"\n"
"")
        self.label_sum_score_left.setAlignment(QtCore.Qt.AlignCenter)
        self.label_sum_score_left.setObjectName("label_sum_score_left")
        self.verticalLayout_11.addWidget(self.label_sum_score_left)
        self.horizontalLayout_3.addLayout(self.verticalLayout_11)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_fight_area_number = QtWidgets.QLabel(self.centralwidget)
        self.label_fight_area_number.setStyleSheet("background-color: rgb(0, 0, 0);\n"
"color: rgb(166, 255, 0);\n"
"font: 57 20pt \"Dubai Medium\";\n"
"\n"
"border-radius: 20px;\n"
"\n"
"width: 250px;\n"
"height: 70px;\n"
"")
        self.label_fight_area_number.setAlignment(QtCore.Qt.AlignCenter)
        self.label_fight_area_number.setObjectName("label_fight_area_number")
        self.verticalLayout.addWidget(self.label_fight_area_number)
        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        self.label_11.setText("")
        self.label_11.setObjectName("label_11")
        self.verticalLayout.addWidget(self.label_11)
        self.label_title_time = QtWidgets.QLabel(self.centralwidget)
        self.label_title_time.setStyleSheet("\n"
"    font: 57 30pt \"Dubai Medium\";\n"
"")
        self.label_title_time.setAlignment(QtCore.Qt.AlignCenter)
        self.label_title_time.setObjectName("label_title_time")
        self.verticalLayout.addWidget(self.label_title_time)
        self.label_time_counter = QtWidgets.QLabel(self.centralwidget)
        self.label_time_counter.setStyleSheet("\n"
"    font: 57 60pt \"Dubai Medium\";\n"
"")
        self.label_time_counter.setAlignment(QtCore.Qt.AlignCenter)
        self.label_time_counter.setObjectName("label_time_counter")
        self.verticalLayout.addWidget(self.label_time_counter)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.pushButton_time_pause = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_time_pause.setStyleSheet("QPushButton {\n"
"    background-color: rgb(255, 80, 80);\n"
"    font: 57 12pt \"Dubai Medium\";\n"
"    border-radius: 10px;\n"
"    padding: 7px;\n"
"\n"
"    width: 150px;\n"
"    height: 30px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    \n"
"    background-color: rgb(198, 0, 0);\n"
"}\n"
"\n"
"")
        self.pushButton_time_pause.setObjectName("pushButton_time_pause")
        self.gridLayout.addWidget(self.pushButton_time_pause, 0, 0, 1, 1)
        self.pushButton_time_continue = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Dubai Medium")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(7)
        self.pushButton_time_continue.setFont(font)
        self.pushButton_time_continue.setStyleSheet("QPushButton {\n"
"    \n"
"    background-color: rgb(139, 255, 133);\n"
"    font: 57 12pt \"Dubai Medium\";\n"
"    border-radius: 10px;\n"
"    padding: 7px;\n"
"\n"
"    width: 150px;\n"
"    height: 30px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    \n"
"    background-color: rgb(0, 193, 12);\n"
"}\n"
"\n"
"")
        self.pushButton_time_continue.setObjectName("pushButton_time_continue")
        self.gridLayout.addWidget(self.pushButton_time_continue, 0, 1, 1, 1)
        self.pushButton_time_start = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_time_start.setStyleSheet("QPushButton {\n"
"    \n"
"    background-color: rgb(255, 194, 123);\n"
"    font-family: \"Dubai Medium\";\n"
"    font-size: 16px;\n"
"    border-radius: 8px;\n"
"    padding: 10px;\n"
"\n"
"    transition: background-color 1s linear;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(225, 171, 108);\n"
"}\n"
"\n"
"")
        self.pushButton_time_start.setObjectName("pushButton_time_start")
        self.gridLayout.addWidget(self.pushButton_time_start, 1, 0, 1, 2)
        self.verticalLayout.addLayout(self.gridLayout)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton_close_scoreboard = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_close_scoreboard.setStyleSheet("QPushButton {\n"
"    background-color: rgb(0, 0, 0);\n"
"    color: rgb(166, 255, 0);\n"
"    font: 57 15pt \"Dubai Medium\";\n"
"\n"
"    border-radius: 20px;\n"
"\n"
"    width: 150px;\n"
"    height: 60px;\n"
"        \n"
"}\n"
"\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(83, 83, 83);\n"
"}")
        self.pushButton_close_scoreboard.setObjectName("pushButton_close_scoreboard")
        self.horizontalLayout.addWidget(self.pushButton_close_scoreboard)
        self.pushButton_open_scoreboard = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_open_scoreboard.setStyleSheet("QPushButton {\n"
"    background-color: rgb(0, 0, 0);\n"
"    color: rgb(166, 255, 0);\n"
"    font: 57 15pt \"Dubai Medium\";\n"
"\n"
"    border-radius: 20px;\n"
"\n"
"    width: 150px;\n"
"    height: 60px;\n"
"        \n"
"}\n"
"\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(83, 83, 83);\n"
"}")
        self.pushButton_open_scoreboard.setObjectName("pushButton_open_scoreboard")
        self.horizontalLayout.addWidget(self.pushButton_open_scoreboard)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_3.addLayout(self.verticalLayout)
        self.verticalLayout_12 = QtWidgets.QVBoxLayout()
        self.verticalLayout_12.setObjectName("verticalLayout_12")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")
        self.verticalLayout_12.addWidget(self.label_3)
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Sitka Heading Semibold")
        font.setPointSize(30)
        self.label_4.setFont(font)
        self.label_4.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignHCenter)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_12.addWidget(self.label_4)
        self.label_sum_score_right = QtWidgets.QLabel(self.centralwidget)
        self.label_sum_score_right.setStyleSheet("color: #fff;\n"
"background: #000000;\n"
"font: 57 30pt \"Dubai Medium\";\n"
"\n"
"border-radius: 15px;\n"
"")
        self.label_sum_score_right.setAlignment(QtCore.Qt.AlignCenter)
        self.label_sum_score_right.setObjectName("label_sum_score_left_2")
        self.verticalLayout_12.addWidget(self.label_sum_score_right)
        self.horizontalLayout_3.addLayout(self.verticalLayout_12)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.combobox_full_name_right = QtWidgets.QComboBox(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Dubai Medium")
        font.setPointSize(20)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(7)
        self.combobox_full_name_right.setFont(font)
        self.combobox_full_name_right.setStyleSheet("\n"
"    font: 57 20pt \"Dubai Medium\";\n"
"")
        self.combobox_full_name_right.setObjectName("label_full_name_right")
        self.verticalLayout_4.addWidget(self.combobox_full_name_right)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_team_right = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Dubai Medium")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(7)
        self.label_team_right.setFont(font)
        self.label_team_right.setStyleSheet("background-color: rgb(221, 221, 221);\n"
"font: 57 12pt \"Dubai Medium\";\n"
"\n"
"border-radius: 10px;\n"
"border: 1px solid black;\n"
"\n"
"padding-right: 10px;\n"
"padding-left: 10px;")
        self.label_team_right.setObjectName("label_team_right")
        self.horizontalLayout_5.addWidget(self.label_team_right)
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.label_weight_category_right = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Dubai Medium")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(7)
        self.label_weight_category_right.setFont(font)
        self.label_weight_category_right.setStyleSheet("background-color: rgb(221, 221, 221);\n"
"font: 57 12pt \"Dubai Medium\";\n"
"\n"
"border-radius: 10px;\n"
"border: 1px solid black;\n"
"\n"
"padding-right: 10px;\n"
"padding-left: 10px;")
        self.label_weight_category_right.setAlignment(QtCore.Qt.AlignCenter)
        self.label_weight_category_right.setObjectName("label_weight_category_right_2")
        self.verticalLayout_5.addWidget(self.label_weight_category_right)
        self.label_date_of_birth_right = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Dubai Medium")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(7)
        self.label_date_of_birth_right.setFont(font)
        self.label_date_of_birth_right.setStyleSheet("background-color: rgb(221, 221, 221);\n"
"font: 57 12pt \"Dubai Medium\";\n"
"border-radius: 10px;\n"
"border: 1px solid black;")
        self.label_date_of_birth_right.setAlignment(QtCore.Qt.AlignCenter)
        self.label_date_of_birth_right.setObjectName("label_date_of_birth_right")
        self.verticalLayout_5.addWidget(self.label_date_of_birth_right)
        self.horizontalLayout_5.addLayout(self.verticalLayout_5)
        self.verticalLayout_4.addLayout(self.horizontalLayout_5)
        self.label_pass_right = QtWidgets.QLabel(self.centralwidget)
        self.label_pass_right.setText("")
        self.label_pass_right.setObjectName("label_pass_right")
        self.verticalLayout_4.addWidget(self.label_pass_right)
        self.formLayout_4 = QtWidgets.QFormLayout()
        self.formLayout_4.setFieldGrowthPolicy(QtWidgets.QFormLayout.FieldsStayAtSizeHint)
        self.formLayout_4.setRowWrapPolicy(QtWidgets.QFormLayout.DontWrapRows)
        self.formLayout_4.setLabelAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.formLayout_4.setFormAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.formLayout_4.setContentsMargins(10, 0, 30, 0)
        self.formLayout_4.setHorizontalSpacing(20)
        self.formLayout_4.setVerticalSpacing(10)
        self.formLayout_4.setObjectName("formLayout_4")
        self.pushButton_YKO_right = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Sitka Heading Semibold")
        font.setPointSize(16)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(7)
        self.pushButton_YKO_right.setFont(font)
        self.pushButton_YKO_right.setStyleSheet("QPushButton {\n"
"    \n"
"    \n"
"    background-color: rgb(255, 255, 255);\n"
"    \n"
"    font: 63 16pt \"Sitka Heading Semibold\";\n"
"\n"
"    border-radius: 10px;\n"
"    \n"
"    border-color: rgb(0, 0, 0);\n"
"    \n"
"    width: 200px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(217, 217, 217);\n"
"}\n"
"\n"
"")
        self.pushButton_YKO_right.setObjectName("pushButton_YKO_right")
        self.formLayout_4.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.pushButton_YKO_right)
        self.pushButton_VAZARI_right = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Sitka Heading Semibold")
        font.setPointSize(16)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(7)
        self.pushButton_VAZARI_right.setFont(font)
        self.pushButton_VAZARI_right.setStyleSheet("QPushButton {\n"
"    \n"
"    \n"
"    background-color: rgb(255, 255, 255);\n"
"    \n"
"    font: 63 16pt \"Sitka Heading Semibold\";\n"
"\n"
"    border-radius: 10px;\n"
"    \n"
"    border-color: rgb(0, 0, 0);\n"
"\n"
"    width: 200px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(217, 217, 217);\n"
"}\n"
"\n"
"")
        self.pushButton_VAZARI_right.setObjectName("pushButton_IPPON_right")
        self.formLayout_4.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.pushButton_VAZARI_right)
        self.pushButton_IPPON_right = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Sitka Heading Semibold")
        font.setPointSize(16)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(7)
        self.pushButton_IPPON_right.setFont(font)
        self.pushButton_IPPON_right.setStyleSheet("QPushButton {\n"
"    \n"
"    \n"
"    background-color: rgb(255, 255, 255);\n"
"    \n"
"    font: 63 16pt \"Sitka Heading Semibold\";\n"
"\n"
"    border-radius: 10px;\n"
"    \n"
"    border-color: rgb(0, 0, 0);\n"
"\n"
"    width: 200px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(217, 217, 217);\n"
"}\n"
"\n"
"")
        self.pushButton_IPPON_right.setObjectName("pushButton_VAZARI_right")
        self.formLayout_4.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.pushButton_IPPON_right)
        self.pushButton_SHIDO_right = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Sitka Heading Semibold")
        font.setPointSize(16)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(7)
        self.pushButton_SHIDO_right.setFont(font)
        self.pushButton_SHIDO_right.setStyleSheet("QPushButton {\n"
"    \n"
"    \n"
"    background-color: rgb(255, 255, 255);\n"
"    \n"
"    font: 63 16pt \"Sitka Heading Semibold\";\n"
"\n"
"    border-radius: 10px;\n"
"    \n"
"    border-color: rgb(0, 0, 0);\n"
"\n"
"    width: 200px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    \n"
"    background-color: rgb(255, 169, 169);\n"
"}\n"
"\n"
"\n"
"")
        self.pushButton_SHIDO_right.setObjectName("pushButton_SHIDO_right")
        self.formLayout_4.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.pushButton_SHIDO_right)
        self.label_YKO_score_right = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_YKO_score_right.sizePolicy().hasHeightForWidth())
        self.label_YKO_score_right.setSizePolicy(sizePolicy)
        self.label_YKO_score_right.setStyleSheet("\n"
"\n"
"font: 63 20pt \"Sitka Heading Semibold\";")
        self.label_YKO_score_right.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.label_YKO_score_right.setIndent(0)
        self.label_YKO_score_right.setObjectName("label_IPPON_score_left_4")
        self.formLayout_4.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_YKO_score_right)
        self.label_VAZARI_score_right = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_VAZARI_score_right.sizePolicy().hasHeightForWidth())
        self.label_VAZARI_score_right.setSizePolicy(sizePolicy)
        self.label_VAZARI_score_right.setStyleSheet("\n"
"\n"
"font: 63 20pt \"Sitka Heading Semibold\";")
        self.label_VAZARI_score_right.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.label_VAZARI_score_right.setIndent(0)
        self.label_VAZARI_score_right.setObjectName("label_VAZARI_score_right")
        self.formLayout_4.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_VAZARI_score_right)
        self.label_IPPON_score_right = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_IPPON_score_right.sizePolicy().hasHeightForWidth())
        self.label_IPPON_score_right.setSizePolicy(sizePolicy)
        self.label_IPPON_score_right.setStyleSheet("\n"
"\n"
"font: 63 20pt \"Sitka Heading Semibold\";")
        self.label_IPPON_score_right.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.label_IPPON_score_right.setIndent(0)
        self.label_IPPON_score_right.setObjectName("label_SHIDO_score_right")
        self.formLayout_4.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_IPPON_score_right)
        self.label_SHIDO_score_right = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_SHIDO_score_right.sizePolicy().hasHeightForWidth())
        self.label_SHIDO_score_right.setSizePolicy(sizePolicy)
        self.label_SHIDO_score_right.setStyleSheet("\n"
"\n"
"font: 63 20pt \"Sitka Heading Semibold\";")
        self.label_SHIDO_score_right.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.label_SHIDO_score_right.setIndent(0)
        self.label_SHIDO_score_right.setObjectName("label_YKO_score_right")
        self.formLayout_4.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.label_SHIDO_score_right)
        self.verticalLayout_4.addLayout(self.formLayout_4)
        self.label_hold = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Sitka Heading Semibold")
        font.setPointSize(20)
        self.label_hold.setFont(font)
        self.label_hold.setAlignment(QtCore.Qt.AlignCenter)
        self.label_hold.setObjectName("label_9")
        self.verticalLayout_4.addWidget(self.label_hold)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.pushButton_right_stopwatch_start = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_right_stopwatch_start.setStyleSheet("QPushButton {\n"
"    \n"
"    \n"
"    background-color: rgb(255, 255, 255);\n"
"    \n"
"    font: 63 16pt \"Sitka Heading Semibold\";\n"
"\n"
"    border-radius: 10px;\n"
"\n"
"    padding: 10px;\n"
"    \n"
"}\n"
"\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(255, 240, 176);\n"
"}\n"
"\n"
"")
        self.pushButton_right_stopwatch_start.setObjectName("pushButton_3")
        self.horizontalLayout_6.addWidget(self.pushButton_right_stopwatch_start)
        self.label_stopwatch_time_right = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Sitka Heading Semibold")
        font.setPointSize(20)
        self.label_stopwatch_time_right.setFont(font)
        self.label_stopwatch_time_right.setAlignment(QtCore.Qt.AlignCenter)
        self.label_stopwatch_time_right.setObjectName("label_10")
        self.horizontalLayout_6.addWidget(self.label_stopwatch_time_right)
        self.pushButton_right_stopwatch_stop = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_right_stopwatch_stop.setStyleSheet("QPushButton {\n"
"    \n"
"    \n"
"    background-color: rgb(255, 255, 255);\n"
"    \n"
"    font: 63 16pt \"Sitka Heading Semibold\";\n"
"\n"
"    border-radius: 10px;\n"
"\n"
"    padding: 10px;\n"
"    \n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(255, 240, 176);\n"
"}\n"
"\n"
"")
        self.pushButton_right_stopwatch_stop.setObjectName("pushButton_4")
        self.horizontalLayout_6.addWidget(self.pushButton_right_stopwatch_stop)
        self.verticalLayout_4.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_3.addLayout(self.verticalLayout_4)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        ############## my code part ##################
        self.functions()

        self.timer = QTimer()
        self.timer.timeout.connect(self.update_timer)
        self.timer_time = QTime(0, 0)

        self.stopwatch_left = QTimer()
        self.stopwatch_left.timeout.connect(self.update_stopwatch_left)
        self.stopwatch_left.start(100)
        self.stopwatch_left_time = 0
        self.stopwatch_left_flag = False
        self.stopwatch_left_counter = 0

        self.stopwatch_right = QTimer()
        self.stopwatch_right.timeout.connect(self.update_stopwatch_right)
        self.stopwatch_right.start(100)
        self.stopwatch_right_time = 0
        self.stopwatch_right_flag = False
        self.stopwatch_right_counter = 0

        self.fighters_list = {}
        self.scoreboard_ui = None

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_weight_category_left.setText(_translate("MainWindow", "Весовая кат. - 22"))
        self.label_date_of_birth_left.setText(_translate("MainWindow", "19.02.2005"))
        self.label_team_left.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\">Школа</p><p align=\"center\">Одинцовская </p><p align=\"center\">СОШ 3</p></body></html>"))
        self.pushButton_YKO_left.setText(_translate("MainWindow", "ЮКО"))
        self.label_YKO_score_left.setText(_translate("MainWindow", "0"))
        self.pushButton_VAZARI_left.setText(_translate("MainWindow", "ВАЗАРИ"))
        self.label_VAZARI_score_left.setText(_translate("MainWindow", "0"))
        self.pushButton_IPPON_left.setText(_translate("MainWindow", "ИППОН"))
        self.label_IPPON_score_left.setText(_translate("MainWindow", "0"))
        self.pushButton_SHIDO_left.setText(_translate("MainWindow", "ШИДО"))
        self.label_SHIDO_score_left.setText(_translate("MainWindow", "0"))
        self.label_8.setText(_translate("MainWindow", "УДЕРЖАНИЕ"))
        self.pushButton_left_stopwatch_start.setText(_translate("MainWindow", "Старт"))
        self.label_stopwatch_time_left.setText(_translate("MainWindow", "0.0"))
        self.pushButton_left_stopwatch_stop.setText(_translate("MainWindow", "Стоп"))
        self.label_2.setText(_translate("MainWindow", "Очки"))
        self.label_sum_score_left.setText(_translate("MainWindow", "0"))
        self.label_fight_area_number.setText(_translate("MainWindow", "Ковер №1"))
        self.label_title_time.setText(_translate("MainWindow", "Время"))
        self.label_time_counter.setText(_translate("MainWindow", "00:00"))
        self.pushButton_time_pause.setText(_translate("MainWindow", "Пауза"))
        self.pushButton_time_continue.setText(_translate("MainWindow", "Старт"))
        self.pushButton_time_start.setText(_translate("MainWindow", "Выбрать время"))
        self.pushButton_close_scoreboard.setText(_translate("MainWindow", "Закрыть\nтабло"))
        self.pushButton_open_scoreboard.setText(_translate("MainWindow", "Вывести\nтабло"))
        self.label_4.setText(_translate("MainWindow", "Очки"))
        self.label_sum_score_right.setText(_translate("MainWindow", "0"))
        self.label_team_right.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\">Школа</p><p align=\"center\">Одинцовская </p><p align=\"center\">СОШ 3</p></body></html>"))
        self.label_weight_category_right.setText(_translate("MainWindow", "Весовая кат. - 22"))
        self.label_date_of_birth_right.setText(_translate("MainWindow", "19.02.2005"))
        self.pushButton_YKO_right.setText(_translate("MainWindow", "ЮКО"))
        self.pushButton_VAZARI_right.setText(_translate("MainWindow", "ВАЗАРИ"))
        self.pushButton_IPPON_right.setText(_translate("MainWindow", "ИППОН"))
        self.pushButton_SHIDO_right.setText(_translate("MainWindow", "ШИДО"))
        self.label_YKO_score_right.setText(_translate("MainWindow", "0"))
        self.label_VAZARI_score_right.setText(_translate("MainWindow", "0"))
        self.label_IPPON_score_right.setText(_translate("MainWindow", "0"))
        self.label_SHIDO_score_right.setText(_translate("MainWindow", "0"))
        self.label_hold.setText(_translate("MainWindow", "УДЕРЖАНИЕ"))
        self.pushButton_right_stopwatch_start.setText(_translate("MainWindow", "Старт"))
        self.label_stopwatch_time_right.setText(_translate("MainWindow", "0.0"))
        self.pushButton_right_stopwatch_stop.setText(_translate("MainWindow", "Стоп"))


    def functions(self):
        ##################################### plus punish buttons #####################################
        self.pushButton_SHIDO_right.clicked.connect(lambda: self.plus_one_score(self.label_SHIDO_score_right, ''))
        self.pushButton_SHIDO_left.clicked.connect(lambda: self.plus_one_score(self.label_SHIDO_score_left, ''))

        ##################################### plus score buttons #####################################

        ########### left side #########
        self.pushButton_IPPON_left.clicked.connect(lambda: self.plus_one_score(self.label_IPPON_score_left, 'left'))
        self.pushButton_VAZARI_left.clicked.connect(lambda: self.plus_one_score(self.label_VAZARI_score_left, 'left'))
        self.pushButton_YKO_left.clicked.connect(lambda: self.plus_one_score(self.label_YKO_score_left, 'left'))

        ########### right side #########
        self.pushButton_IPPON_right.clicked.connect(lambda: self.plus_one_score(self.label_IPPON_score_right, 'right'))
        self.pushButton_YKO_right.clicked.connect(lambda: self.plus_one_score(self.label_YKO_score_right, 'right'))
        self.pushButton_VAZARI_right.clicked.connect(lambda: self.plus_one_score(self.label_VAZARI_score_right, 'right'))


        ##################################### time buttons #####################################
        ###### timer ########
        self.pushButton_time_start.clicked.connect(self.set_time)
        self.pushButton_time_continue.clicked.connect(lambda: self.timer.start())
        self.pushButton_time_pause.clicked.connect(lambda: self.timer.stop())

        ###### stopwatch left ########
        self.pushButton_left_stopwatch_start.clicked.connect(self.start_stopwatch_left)
        self.pushButton_left_stopwatch_stop.clicked.connect(self.stop_stopwatch_left)

        ###### stopwatch right ########
        self.pushButton_right_stopwatch_start.clicked.connect(self.start_stopwatch_right)
        self.pushButton_right_stopwatch_stop.clicked.connect(self.stop_stopwatch_right)

        ############ change fighter info ################
        self.combobox_full_name_left.currentTextChanged.connect(lambda: self.update_fighter_info('left'))
        self.combobox_full_name_right.currentTextChanged.connect(lambda: self.update_fighter_info('right'))



    def open_manage_panel(self, number, fighters_list):
        self.label_fight_area_number.setText(f"Ковер №{number}")

        if fighters_list:
                self.fighters_list = fighters_list
                self.combobox_full_name_left.addItems(self.fighters_list['Спортсмен'])
                self.combobox_full_name_right.addItems(self.fighters_list['Спортсмен'])

    def plus_one_score(self, name, side):
        text = int(name.text()) + 1
        name.setText(str(text))

        self.is_baned()
        self.update_score(side)

        self.update_scoreboard()

##################### is baned #################################
    def is_baned(self):

            font = QtGui.QFont()
            font.setFamily("Sitka Heading Semibold")
            font.setPointSize(18)

            if int(self.label_SHIDO_score_right.text()) > 2:
                    self.label_pass_right.setText('ХАНСОКУ МАКЕ')
                    self.label_pass_right.setFont(font)
                    self.label_pass_right.setAlignment(QtCore.Qt.AlignCenter)

            if int(self.label_SHIDO_score_left.text()) > 2:
                    self.label_pass_left.setText('ХАНСОКУ МАКЕ')
                    self.label_pass_left.setFont(font)
                    self.label_pass_left.setAlignment(QtCore.Qt.AlignCenter)

            self.update_scoreboard()

##################### score counter ############################
    def update_score(self, side):
            if side == 'left':
                    score = (int(self.label_YKO_score_left.text()) +
                             10 * int(self.label_VAZARI_score_left.text()) +
                             100 * int(self.label_IPPON_score_left.text()))
                    self.label_sum_score_left.setText(str(score))

            elif side == 'right':
                    score = (int(self.label_YKO_score_right.text()) +
                             10 * int(self.label_VAZARI_score_right.text()) +
                             100 * int(self.label_IPPON_score_right.text()))
                    self.label_sum_score_right.setText(str(score))

            self.update_scoreboard()

############## timer setup functions #########################
###### timer ########
    def set_time(self):
        ChoseTime = QDialog()
        ChoseTime.setWindowTitle("Выберите время")
        ChoseTime.resize(260, 231)

        time_edit = QTimeEdit()
        time_edit.setDisplayFormat("mm:ss")
        time_edit.setGeometry(QtCore.QRect(40, 90, 181, 51))
        font = QtGui.QFont()
        font.setPointSize(30)
        time_edit.setFont(font)
        time_edit.setAlignment(QtCore.Qt.AlignCenter)

        pushButton_ok_time = QPushButton("OK")
        pushButton_ok_time.setGeometry(QtCore.QRect(60, 170, 141, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        pushButton_ok_time.setFont(font)

        layout = QVBoxLayout()
        layout.addWidget(time_edit)
        layout.addWidget(pushButton_ok_time)
        ChoseTime.setLayout(layout)

        pushButton_ok_time.clicked.connect(lambda: self.start_timer(ChoseTime, time_edit.time()))

        ChoseTime.exec_()

        self.update_scoreboard()

    def start_timer(self, window, time):
            window.close()

            self.timer_time = time
            self.update_timer_display()

            if not self.timer.isActive():
                    self.timer.start(1000)  # Обновляем каждую секунду

            self.timer.stop()

            self.update_scoreboard()

    def update_timer(self):
            if self.timer_time == QTime(0, 0):
                    self.timer.stop()
                    return

            self.timer_time = self.timer_time.addSecs(-1)
            self.update_timer_display()

            self.update_scoreboard()

    def update_timer_display(self):
            self.label_time_counter.setText(self.timer_time.toString("mm:ss"))

            self.update_scoreboard()

###### stopwatch left ########
    def update_stopwatch_left(self):
            if self.stopwatch_left_flag:
                self.stopwatch_left_time += 1

            left_time = str(self.stopwatch_left_time / 10)

            self.label_stopwatch_time_left.setText(left_time)

            self.update_scoreboard()

    def start_stopwatch_left(self):
        self.stopwatch_left_flag = True
        self.pushButton_left_stopwatch_stop.setText('Стоп')
        self.stopwatch_left_counter = 0

    def stop_stopwatch_left(self):

        if self.stopwatch_left_counter == 0:
                self.stopwatch_left_flag = False
                self.pushButton_left_stopwatch_stop.setText('Сброс')
                self.stopwatch_left_counter += 1

        elif self.stopwatch_left_counter == 1:
                self.stopwatch_left_flag = False
                self.pushButton_left_stopwatch_stop.setText('Стоп')
                self.stopwatch_left_time = 0
                self.label_stopwatch_time_left.setText(str(self.stopwatch_left_time))
                self.stopwatch_left_counter = 0

        self.update_scoreboard()

###### stopwatch right ########
    def update_stopwatch_right(self):
            if self.stopwatch_right_flag:
                self.stopwatch_right_time += 1

            right_time = str(self.stopwatch_right_time / 10)

            self.label_stopwatch_time_right.setText(right_time)

            self.update_scoreboard()

    def start_stopwatch_right(self):
            self.stopwatch_right_flag = True
            self.pushButton_right_stopwatch_stop.setText('Стоп')
            self.stopwatch_right_counter = 0

    def stop_stopwatch_right(self):
            if self.stopwatch_right_counter == 0:
                    self.stopwatch_right_flag = False
                    self.pushButton_right_stopwatch_stop.setText('Сброс')
                    self.stopwatch_right_counter += 1

            elif self.stopwatch_right_counter == 1:
                    self.stopwatch_right_flag = False
                    self.pushButton_right_stopwatch_stop.setText('Стоп')
                    self.stopwatch_right_time = 0
                    self.label_stopwatch_time_right.setText(str(self.stopwatch_right_time))
                    self.stopwatch_right_counter = 0

            self.update_scoreboard()


########################## save link to scoreboard ###################################
    def save_scoreboard_link(self, link):
            self.scoreboard_ui = link['ui']

####################### change fighter info ################################
    def update_fighter_info(self, side):
            if side == 'left':
                    index = self.fighters_list['Спортсмен'].index(self.combobox_full_name_left.currentText())

                    self.label_date_of_birth_left.setText(f"Весовая кат. - {self.fighters_list['Вес кат'][index]}")
                    self.label_team_left.setText(f"Школа\n{self.fighters_list['Команда'][index]}")
                    self.label_weight_category_left.setText(str(self.fighters_list['Год рождения'][index]).split()[0])

            elif side == 'right':
                    index = self.fighters_list['Спортсмен'].index(self.combobox_full_name_right.currentText())

                    self.label_date_of_birth_right.setText(f"Весовая кат. - {self.fighters_list['Вес кат'][index]}")
                    self.label_team_right.setText(f"Школа\n{self.fighters_list['Команда'][index]}")
                    self.label_weight_category_right.setText(str(self.fighters_list['Год рождения'][index]).split()[0])


    def update_scoreboard(self):
            if self.scoreboard_ui is not None:
                    ########### main timer ###############
                    self.scoreboard_ui.label_timer.setText(self.label_time_counter.text())

                    ############ hold stopwatch ##################
                    self.scoreboard_ui.label_hold_left.setText(f'УДЕРЖАНИЕ {self.label_stopwatch_time_left.text()}')
                    self.scoreboard_ui.label_hold_right.setText(f'{self.label_stopwatch_time_right.text()} УДЕРЖАНИЕ')

                    ############## name ####################
                    self.scoreboard_ui.label_name_left.setText(self.combobox_full_name_left.currentText())
                    self.scoreboard_ui.label_name_right.setText(self.combobox_full_name_right.currentText())

                    ############### fighter info ##################
                    self.scoreboard_ui.label_weight_category_left.setText(self.label_weight_category_left.text())
                    self.scoreboard_ui.label_date_left.setText(self.label_date_of_birth_left.text())
                    self.scoreboard_ui.label_school_left.setText(self.label_team_left.text())

                    self.scoreboard_ui.label_weight_category_right.setText(self.label_weight_category_right.text())
                    self.scoreboard_ui.label_date_right.setText(self.label_date_of_birth_right.text())
                    self.scoreboard_ui.label_school_right.setText(self.label_team_right.text())

                    ###################### win or ban #####################
                    self.scoreboard_ui.label_win_or_ban_left.setText(self.label_pass_left.text())
                    self.scoreboard_ui.label_win_or_ban_right.setText(self.label_pass_right.text())

                    ################# punish or reward ##################
                    self.scoreboard_ui.label_YKO_score_left.setText(self.label_YKO_score_left.text())
                    self.scoreboard_ui.label_VAZARI_score_left.setText(self.label_VAZARI_score_left.text())
                    self.scoreboard_ui.label_IPPON_score_left.setText(self.label_IPPON_score_left.text())
                    self.scoreboard_ui.label_SHIDO_score_left.setText(self.label_SHIDO_score_left.text())

                    self.scoreboard_ui.label_YKO_score_right.setText(self.label_YKO_score_right.text())
                    self.scoreboard_ui.label_VAZARI_score_right.setText(self.label_VAZARI_score_right.text())
                    self.scoreboard_ui.label_IPPON_score_right.setText(self.label_IPPON_score_right.text())
                    self.scoreboard_ui.label_SHIDO_score_right.setText(self.label_SHIDO_score_right.text())

                    ################## total score ####################
                    self.scoreboard_ui.label_total_score_left.setText(self.label_sum_score_left.text())
                    self.scoreboard_ui.label_total_score_right.setText(self.label_sum_score_right.text())







