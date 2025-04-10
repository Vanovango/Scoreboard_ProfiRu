from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Scoreboard(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1804, 926)
        MainWindow.setStyleSheet("background-color: rgb(0, 0, 0);")

        ################################# my fonts ############################################
        self.font_timer = QtGui.QFont()
        self.font_timer.setFamily("Arial")
        self.font_timer.setPointSize(95)

        self.font_label_time = QtGui.QFont()
        self.font_label_time.setFamily("Arial")
        self.font_label_time.setPointSize(50)

        self.font_name = QtGui.QFont()
        self.font_name.setFamily("Arial")
        self.font_name.setPointSize(25)

        self.font_fighter_info = QtGui.QFont()
        self.font_fighter_info.setFamily("Arial")
        self.font_fighter_info.setPointSize(20)

        self.font_win_or_ban = QtGui.QFont()
        self.font_win_or_ban.setFamily("Arial")
        self.font_win_or_ban.setPointSize(25)

        self.font_punish_and_succsess = QtGui.QFont()
        self.font_punish_and_succsess.setFamily("Arial")
        self.font_punish_and_succsess.setPointSize(25)

        self.font_hold = QtGui.QFont()
        self.font_hold.setFamily("Arial")
        self.font_hold.setPointSize(25)

        self.font_label_score = QtGui.QFont()
        self.font_label_score.setFamily("Arial")
        self.font_label_score.setPointSize(30)

        self.font_total_score = QtGui.QFont()
        self.font_total_score.setFamily("Arial")
        self.font_total_score.setPointSize(70)

        self.font_area_number = QtGui.QFont()
        self.font_area_number.setFamily("Arial")
        self.font_area_number.setPointSize(25)
        #####################################################################################

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setSpacing(15)
        self.verticalLayout.setObjectName("verticalLayout")

        self.label_name_left = QtWidgets.QLabel(self.centralwidget)
        self.label_name_left.setFont(self.font_name)
        self.label_name_left.setStyleSheet("color: rgb(255, 255, 255);\n"
"padding-left: 10px;\n"
"padding: 20px;")
        self.label_name_left.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_name_left)

        self.gridLayout_3 = QtWidgets.QGridLayout()
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.label_weight_category_left = QtWidgets.QLabel(self.centralwidget)
        self.label_weight_category_left.setFont(self.font_fighter_info)
        self.label_weight_category_left.setStyleSheet("color: rgb(255, 255, 255);\n"
"border: 1px solid rgb(140, 140, 140);\n"
"border-radius: 20px;\n"
"padding: 10px;")
        self.label_weight_category_left.setAlignment(QtCore.Qt.AlignCenter)
        self.label_weight_category_left.setObjectName("label_14")
        self.gridLayout_3.addWidget(self.label_weight_category_left, 0, 0, 1, 1)
        self.label_date_left = QtWidgets.QLabel(self.centralwidget)
        self.label_date_left.setFont(self.font_fighter_info)
        self.label_date_left.setStyleSheet("color: rgb(255, 255, 255);\n"
"border: 1px solid rgb(140, 140, 140);\n"
"border-radius: 20px;\n"
"padding: 10px;")
        self.label_date_left.setAlignment(QtCore.Qt.AlignCenter)
        self.label_date_left.setObjectName("label_15")
        self.gridLayout_3.addWidget(self.label_date_left, 0, 1, 1, 1)
        self.label_school_left = QtWidgets.QLabel(self.centralwidget)
        self.label_school_left.setFont(self.font_fighter_info)
        self.label_school_left.setStyleSheet("color: rgb(255, 255, 255);\n"
"border: 1px solid rgb(140, 140, 140);\n"
"border-radius: 20px;\n"
"padding: 10px;")
        self.label_school_left.setAlignment(QtCore.Qt.AlignCenter)
        self.label_school_left.setObjectName("label_16")
        self.gridLayout_3.addWidget(self.label_school_left, 1, 0, 1, 2)
        self.verticalLayout.addLayout(self.gridLayout_3)
        self.label_win_or_ban_left = QtWidgets.QLabel(self.centralwidget)
        self.label_win_or_ban_left.setFont(self.font_win_or_ban)
        self.label_win_or_ban_left.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_win_or_ban_left.setAlignment(QtCore.Qt.AlignCenter)
        self.label_win_or_ban_left.setObjectName("label")
        self.verticalLayout.addWidget(self.label_win_or_ban_left)
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setContentsMargins(10, 10, 10, 10)
        self.gridLayout_2.setHorizontalSpacing(15)
        self.gridLayout_2.setVerticalSpacing(10)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setObjectName("label_8")
        self.gridLayout_2.addWidget(self.label_8, 0, 2, 5, 1)
        self.label_YKO_left = QtWidgets.QLabel(self.centralwidget)
        self.label_YKO_left.setFont(self.font_punish_and_succsess)
        self.label_YKO_left.setStyleSheet("color: rgb(255, 255, 255);\n"
"padding-left: 10px;\n"
"padding-right: 10px;")
        self.label_YKO_left.setAlignment(QtCore.Qt.AlignCenter)
        self.label_YKO_left.setObjectName("label_3")
        self.gridLayout_2.addWidget(self.label_YKO_left, 0, 0, 1, 1)
        self.label_YKO_score_left = QtWidgets.QLabel(self.centralwidget)
        self.label_YKO_score_left.setFont(self.font_punish_and_succsess)
        self.label_YKO_score_left.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_YKO_score_left.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.label_YKO_score_left.setObjectName("label_9")
        self.gridLayout_2.addWidget(self.label_YKO_score_left, 0, 1, 1, 1)
        self.label_VAZARI_left = QtWidgets.QLabel(self.centralwidget)
        self.label_VAZARI_left.setFont(self.font_punish_and_succsess)
        self.label_VAZARI_left.setStyleSheet("color: rgb(255, 255, 255);\n"
"padding-left: 10px;\n"
"padding-right: 10px;")
        self.label_VAZARI_left.setAlignment(QtCore.Qt.AlignCenter)
        self.label_VAZARI_left.setObjectName("label_4")
        self.gridLayout_2.addWidget(self.label_VAZARI_left, 1, 0, 1, 1)
        self.label_SHIDO_left = QtWidgets.QLabel(self.centralwidget)
        self.label_SHIDO_left.setFont(self.font_punish_and_succsess)
        self.label_SHIDO_left.setStyleSheet("color:rgb(255, 140, 140);\n"
"padding-left: 10px;\n"
"padding-right: 10px;")
        self.label_SHIDO_left.setAlignment(QtCore.Qt.AlignCenter)
        self.label_SHIDO_left.setObjectName("label_6")
        self.gridLayout_2.addWidget(self.label_SHIDO_left, 4, 0, 1, 1)
        self.label_IPPON_left = QtWidgets.QLabel(self.centralwidget)
        self.label_IPPON_left.setFont(self.font_punish_and_succsess)
        self.label_IPPON_left.setStyleSheet("color: rgb(255, 255, 255);\n"
"padding-left: 10px;\n"
"padding-right: 10px;")
        self.label_IPPON_left.setAlignment(QtCore.Qt.AlignCenter)
        self.label_IPPON_left.setObjectName("label_5")
        self.gridLayout_2.addWidget(self.label_IPPON_left, 2, 0, 1, 1)
        self.label_VAZARI_score_left = QtWidgets.QLabel(self.centralwidget)
        self.label_VAZARI_score_left.setFont(self.font_punish_and_succsess)
        self.label_VAZARI_score_left.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_VAZARI_score_left.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.label_VAZARI_score_left.setObjectName("label_10")
        self.gridLayout_2.addWidget(self.label_VAZARI_score_left, 1, 1, 1, 1)
        self.label_IPPON_score_left = QtWidgets.QLabel(self.centralwidget)
        self.label_IPPON_score_left.setFont(self.font_punish_and_succsess)
        self.label_IPPON_score_left.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_IPPON_score_left.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.label_IPPON_score_left.setObjectName("label_11")
        self.gridLayout_2.addWidget(self.label_IPPON_score_left, 2, 1, 1, 1)
        self.label_SHIDO_score_left = QtWidgets.QLabel(self.centralwidget)
        self.label_SHIDO_score_left.setFont(self.font_punish_and_succsess)
        self.label_SHIDO_score_left.setStyleSheet("color:rgb(255, 140, 140);")
        self.label_SHIDO_score_left.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.label_SHIDO_score_left.setObjectName("label_13")
        self.gridLayout_2.addWidget(self.label_SHIDO_score_left, 4, 1, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout_2)
        self.label_hold_left = QtWidgets.QLabel(self.centralwidget)
        self.label_hold_left.setFont(self.font_hold)
        self.label_hold_left.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_hold_left.setAlignment(QtCore.Qt.AlignCenter)
        self.label_hold_left.setObjectName("label_12")
        self.verticalLayout.addWidget(self.label_hold_left)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_17 = QtWidgets.QLabel(self.centralwidget)
        self.label_17.setObjectName("label_17")
        self.verticalLayout_3.addWidget(self.label_17)
        self.label_score_title_left = QtWidgets.QLabel(self.centralwidget)
        self.label_score_title_left.setFont(self.font_label_score)
        self.label_score_title_left.setStyleSheet("color: rgb(255, 255, 255);\n"
"padding-top: 250px;")
        self.label_score_title_left.setAlignment(QtCore.Qt.AlignCenter)
        self.label_score_title_left.setObjectName("label_18")
        self.verticalLayout_3.addWidget(self.label_score_title_left)
        self.label_total_score_left = QtWidgets.QLabel(self.centralwidget)
        self.label_total_score_left.setFont(self.font_total_score)
        self.label_total_score_left.setStyleSheet("color: rgb(255, 255, 255);\n"
"padding-bottom: 150px;")
        self.label_total_score_left.setAlignment(QtCore.Qt.AlignCenter)
        self.label_total_score_left.setObjectName("label_20")
        self.verticalLayout_3.addWidget(self.label_total_score_left)
        self.horizontalLayout.addLayout(self.verticalLayout_3)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.label_timer = QtWidgets.QLabel(self.centralwidget)
        self.label_timer.setSizeIncrement(QtCore.QSize(10, 10))
        self.label_timer.setFont(self.font_timer)
        self.label_timer.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_timer.setAutoFillBackground(False)
        self.label_timer.setStyleSheet("color: rgb(255, 255, 255);\n"
"padding-bottom: 100px;\n"
"\n"
"")
        self.label_timer.setScaledContents(False)
        self.label_timer.setAlignment(QtCore.Qt.AlignCenter)
        self.label_timer.setObjectName("label_time")
        self.gridLayout.addWidget(self.label_timer, 2, 0, 1, 1)
        self.label_title_time = QtWidgets.QLabel(self.centralwidget)
        self.label_title_time.setFont(self.font_label_time)
        self.label_title_time.setStyleSheet("color: rgb(255, 255, 255);\n"
"padding-top: 150px;")
        self.label_title_time.setAlignment(QtCore.Qt.AlignCenter)
        self.label_title_time.setObjectName("label_title_time")
        self.gridLayout.addWidget(self.label_title_time, 1, 0, 1, 1)
        self.label_19 = QtWidgets.QLabel(self.centralwidget)
        self.label_19.setText("")
        self.label_19.setObjectName("label_19")
        self.gridLayout.addWidget(self.label_19, 3, 0, 1, 1)

        self.pushButton_area_number = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_area_number.setFont(self.font_area_number)
        self.pushButton_area_number.setStyleSheet("QPushButton {\n"
"    color: rgb(166, 255, 0);\n"
"    border: 1px solid white;\n"
"    border-radius: 20px;\n"
"    height: 75px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    \n"
"    background-color: rgb(61, 61, 61);\n"
"}")
        self.pushButton_area_number.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton_area_number, 0, 0, 1, 1)

        self.horizontalLayout.addLayout(self.gridLayout)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label_22 = QtWidgets.QLabel(self.centralwidget)
        self.label_22.setObjectName("label_22")
        self.verticalLayout_4.addWidget(self.label_22)
        self.label_score_title_right = QtWidgets.QLabel(self.centralwidget)
        self.label_score_title_right.setFont(self.font_label_score)
        self.label_score_title_right.setStyleSheet("color: rgb(255, 255, 255);\n"
"padding-top: 250px;")
        self.label_score_title_right.setAlignment(QtCore.Qt.AlignCenter)
        self.label_score_title_right.setObjectName("label_23")
        self.verticalLayout_4.addWidget(self.label_score_title_right)
        self.label_total_score_right = QtWidgets.QLabel(self.centralwidget)
        self.label_total_score_right.setFont(self.font_total_score)
        self.label_total_score_right.setStyleSheet("color: rgb(255, 255, 255);\n"
"padding-bottom: 150px;")
        self.label_total_score_right.setAlignment(QtCore.Qt.AlignCenter)
        self.label_total_score_right.setObjectName("label_21")
        self.verticalLayout_4.addWidget(self.label_total_score_right)
        self.horizontalLayout.addLayout(self.verticalLayout_4)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setSpacing(15)
        self.verticalLayout_5.setObjectName("verticalLayout_5")

        self.label_name_right = QtWidgets.QLabel(self.centralwidget)
        self.label_name_right.setFont(self.font_name)
        self.label_name_right.setStyleSheet("color: rgb(255, 255, 255);\n"
"padding-left: 10px;\n"
"padding: 20px;")
        self.label_name_right.setObjectName("label_7")
        self.verticalLayout_5.addWidget(self.label_name_right)

        self.gridLayout_4 = QtWidgets.QGridLayout()
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.label_school_right = QtWidgets.QLabel(self.centralwidget)
        self.label_school_right.setFont(self.font_fighter_info)
        self.label_school_right.setStyleSheet("color: rgb(255, 255, 255);\n"
"border: 1px solid rgb(140, 140, 140);\n"
"border-radius: 20px;\n"
"padding: 10px;")
        self.label_school_right.setAlignment(QtCore.Qt.AlignCenter)
        self.label_school_right.setObjectName("label_26")
        self.gridLayout_4.addWidget(self.label_school_right, 1, 1, 1, 2)
        self.label_weight_category_right = QtWidgets.QLabel(self.centralwidget)
        self.label_weight_category_right.setFont(self.font_fighter_info)
        self.label_weight_category_right.setStyleSheet("color: rgb(255, 255, 255);\n"
"border: 1px solid rgb(140, 140, 140);\n"
"border-radius: 20px;\n"
"padding: 10px;")
        self.label_weight_category_right.setAlignment(QtCore.Qt.AlignCenter)
        self.label_weight_category_right.setObjectName("label_24")
        self.gridLayout_4.addWidget(self.label_weight_category_right, 0, 2, 1, 1)
        self.label_date_right = QtWidgets.QLabel(self.centralwidget)
        self.label_date_right.setFont(self.font_fighter_info)
        self.label_date_right.setStyleSheet("color: rgb(255, 255, 255);\n"
"border: 1px solid rgb(140, 140, 140);\n"
"border-radius: 20px;\n"
"padding: 10px;")
        self.label_date_right.setAlignment(QtCore.Qt.AlignCenter)
        self.label_date_right.setObjectName("label_25")
        self.gridLayout_4.addWidget(self.label_date_right, 0, 1, 1, 1)
        self.verticalLayout_5.addLayout(self.gridLayout_4)
        self.label_win_or_ban_right = QtWidgets.QLabel(self.centralwidget)
        self.label_win_or_ban_right.setFont(self.font_win_or_ban)
        self.label_win_or_ban_right.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_win_or_ban_right.setAlignment(QtCore.Qt.AlignCenter)
        self.label_win_or_ban_right.setObjectName("label_27")
        self.verticalLayout_5.addWidget(self.label_win_or_ban_right)
        self.gridLayout_5 = QtWidgets.QGridLayout()
        self.gridLayout_5.setContentsMargins(10, 10, 10, 10)
        self.gridLayout_5.setHorizontalSpacing(15)
        self.gridLayout_5.setVerticalSpacing(10)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.label_VAZARI_right = QtWidgets.QLabel(self.centralwidget)
        self.label_VAZARI_right.setFont(self.font_punish_and_succsess)
        self.label_VAZARI_right.setStyleSheet("color: rgb(255, 255, 255);\n"
"padding-left: 10px;\n"
"padding-right: 10px;")
        self.label_VAZARI_right.setAlignment(QtCore.Qt.AlignCenter)
        self.label_VAZARI_right.setObjectName("label_31")
        self.gridLayout_5.addWidget(self.label_VAZARI_right, 1, 2, 1, 1)
        self.label_SHIDO_right = QtWidgets.QLabel(self.centralwidget)
        self.label_SHIDO_right.setFont(self.font_punish_and_succsess)
        self.label_SHIDO_right.setStyleSheet("color:rgb(255, 140, 140);\n"
"padding-left: 10px;\n"
"padding-right: 10px;")
        self.label_SHIDO_right.setAlignment(QtCore.Qt.AlignCenter)
        self.label_SHIDO_right.setObjectName("label_32")
        self.gridLayout_5.addWidget(self.label_SHIDO_right, 4, 2, 1, 1)
        self.label_IPPON_right = QtWidgets.QLabel(self.centralwidget)
        self.label_IPPON_right.setFont(self.font_punish_and_succsess)
        self.label_IPPON_right.setStyleSheet("color: rgb(255, 255, 255);\n"
"padding-left: 10px;\n"
"padding-right: 10px;")
        self.label_IPPON_right.setAlignment(QtCore.Qt.AlignCenter)
        self.label_IPPON_right.setObjectName("label_33")
        self.gridLayout_5.addWidget(self.label_IPPON_right, 2, 2, 1, 1)
        self.label_28 = QtWidgets.QLabel(self.centralwidget)
        self.label_28.setObjectName("label_28")
        self.gridLayout_5.addWidget(self.label_28, 0, 0, 5, 1)
        self.label_YKO_score_right = QtWidgets.QLabel(self.centralwidget)
        self.label_YKO_score_right.setFont(self.font_punish_and_succsess)
        self.label_YKO_score_right.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_YKO_score_right.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.label_YKO_score_right.setObjectName("label_30")
        self.gridLayout_5.addWidget(self.label_YKO_score_right, 0, 1, 1, 1)
        self.label_VAZARI_score_right = QtWidgets.QLabel(self.centralwidget)
        self.label_VAZARI_score_right.setFont(self.font_punish_and_succsess)
        self.label_VAZARI_score_right.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_VAZARI_score_right.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.label_VAZARI_score_right.setObjectName("label_34")
        self.gridLayout_5.addWidget(self.label_VAZARI_score_right, 1, 1, 1, 1)
        self.label_IPPON_score_right = QtWidgets.QLabel(self.centralwidget)
        self.label_IPPON_score_right.setFont(self.font_punish_and_succsess)
        self.label_IPPON_score_right.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_IPPON_score_right.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.label_IPPON_score_right.setObjectName("label_35")
        self.gridLayout_5.addWidget(self.label_IPPON_score_right, 2, 1, 1, 1)
        self.label_YKO_right = QtWidgets.QLabel(self.centralwidget)
        self.label_YKO_right.setFont(self.font_punish_and_succsess)
        self.label_YKO_right.setStyleSheet("color: rgb(255, 255, 255);\n"
"padding-left: 10px;\n"
"padding-right: 10px;")
        self.label_YKO_right.setAlignment(QtCore.Qt.AlignCenter)
        self.label_YKO_right.setObjectName("label_29")
        self.gridLayout_5.addWidget(self.label_YKO_right, 0, 2, 1, 1)
        self.label_SHIDO_score_right = QtWidgets.QLabel(self.centralwidget)
        self.label_SHIDO_score_right.setFont(self.font_punish_and_succsess)
        self.label_SHIDO_score_right.setStyleSheet("color:rgb(255, 140, 140);")
        self.label_SHIDO_score_right.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.label_SHIDO_score_right.setObjectName("label_36")
        self.gridLayout_5.addWidget(self.label_SHIDO_score_right, 4, 1, 1, 1)
        self.verticalLayout_5.addLayout(self.gridLayout_5)
        self.label_hold_right = QtWidgets.QLabel(self.centralwidget)
        self.label_hold_right.setFont(self.font_hold)
        self.label_hold_right.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_hold_right.setAlignment(QtCore.Qt.AlignCenter)
        self.label_hold_right.setObjectName("label_37")
        self.verticalLayout_5.addWidget(self.label_hold_right)
        self.verticalLayout_2.addLayout(self.verticalLayout_5)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.functions(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_name_left.setText(_translate("MainWindow", "<html><head/><body><p>Иванов</p><p>Иван Иванович</p></body></html>"))
        self.label_weight_category_left.setText(_translate("MainWindow", "Весовая кат. - 22"))
        self.label_date_left.setText(_translate("MainWindow", "19.02.2005"))
        self.label_school_left.setText(_translate("MainWindow", "Школа: Одинцовская СОШ 3"))
        self.label_win_or_ban_left.setText(_translate("MainWindow", ""))
        self.label_8.setText(_translate("MainWindow", ""))
        self.label_YKO_left.setText(_translate("MainWindow", "ЮКО"))
        self.label_YKO_score_left.setText(_translate("MainWindow", "0"))
        self.label_VAZARI_left.setText(_translate("MainWindow", "ВАЗАРИ"))
        self.label_SHIDO_left.setText(_translate("MainWindow", "ШИДО"))
        self.label_IPPON_left.setText(_translate("MainWindow", "ИППОН"))
        self.label_VAZARI_score_left.setText(_translate("MainWindow", "0"))
        self.label_IPPON_score_left.setText(_translate("MainWindow", "0"))
        self.label_SHIDO_score_left.setText(_translate("MainWindow", "0"))
        self.label_hold_left.setText(_translate("MainWindow", "УДЕРЖАНИЕ 0.0"))
        self.label_17.setText(_translate("MainWindow", ""))
        self.label_score_title_left.setText(_translate("MainWindow", "Счет"))
        self.label_total_score_left.setText(_translate("MainWindow", "0"))
        self.label_timer.setText(_translate("MainWindow", " 00:00 "))
        self.label_title_time.setText(_translate("MainWindow", "Время"))
        self.pushButton_area_number.setText(_translate("MainWindow", "Ковер №1"))
        self.label_22.setText(_translate("MainWindow", "TextLabel"))
        self.label_score_title_right.setText(_translate("MainWindow", "Счет"))
        self.label_total_score_right.setText(_translate("MainWindow", "0"))
        self.label_name_right.setText(_translate("MainWindow", "<html><head/><body><p align=\"right\">Иванов</p><p align=\"right\">Иван Иванович</p></body></html>"))
        self.label_school_right.setText(_translate("MainWindow", "Школа: Одинцовская СОШ 3"))
        self.label_weight_category_right.setText(_translate("MainWindow", "Весовая кат. - 22"))
        self.label_date_right.setText(_translate("MainWindow", "19.02.2005"))
        self.label_win_or_ban_right.setText(_translate("MainWindow", ""))
        self.label_VAZARI_right.setText(_translate("MainWindow", "ВАЗАРИ"))
        self.label_SHIDO_right.setText(_translate("MainWindow", "ШИДО"))
        self.label_IPPON_right.setText(_translate("MainWindow", "ИППОН"))
        self.label_28.setText(_translate("MainWindow", "TextLabel"))
        self.label_YKO_score_right.setText(_translate("MainWindow", "0"))
        self.label_VAZARI_score_right.setText(_translate("MainWindow", "0"))
        self.label_IPPON_score_right.setText(_translate("MainWindow", "0"))
        self.label_YKO_right.setText(_translate("MainWindow", "ЮКО"))
        self.label_SHIDO_score_right.setText(_translate("MainWindow", "0"))
        self.label_hold_right.setText(_translate("MainWindow", "0.0 УДЕРЖАНИЕ"))


    def functions(self, MainWindow):
            self.pushButton_area_number.clicked.connect(lambda: self.update_font(MainWindow))

    def change_area_number(self, number):
        self.pushButton_area_number.setText(f"Ковер №{number}")

    def update_font(self, MainWindow):
            window_size = (MainWindow.width(), MainWindow.height())
            new_size = int((window_size[0] + window_size[1]) / 200)

            ################ upscale coefs ######################
            self.font_timer.setPointSize(new_size * 7)                  # 95
            self.font_label_time.setPointSize(new_size * 3)             # 50
            self.font_name.setPointSize(new_size * 2)                   # 25
            self.font_fighter_info.setPointSize(int(new_size * 1.5))    # 20
            self.font_win_or_ban.setPointSize(new_size * 2)             # 25
            self.font_punish_and_succsess.setPointSize(new_size * 2)    # 25
            self.font_hold.setPointSize(new_size * 2)                   # 25
            self.font_label_score.setPointSize(new_size * 3)            # 30
            self.font_total_score.setPointSize(new_size * 4)            # 70
            self.font_area_number.setPointSize(new_size * 2)            # 25
            ##################################################


            ################### name #########################
            self.label_name_left.setFont(self.font_name)
            self.label_name_right.setFont(self.font_name)

            ####################### fighter info ####################
            self.label_weight_category_left.setFont(self.font_fighter_info)
            self.label_weight_category_right.setFont(self.font_fighter_info)
            self.label_date_left.setFont(self.font_fighter_info)
            self.label_date_right.setFont(self.font_fighter_info)
            self.label_school_left.setFont(self.font_fighter_info)
            self.label_school_right.setFont(self.font_fighter_info)

            ###################### win or  ban label ####################3
            self.label_win_or_ban_left.setFont(self.font_win_or_ban)
            self.label_win_or_ban_right.setFont(self.font_win_or_ban)


            ##################### punish and reward ####################
            self.label_YKO_left.setFont(self.font_punish_and_succsess)
            self.label_YKO_score_left.setFont(self.font_punish_and_succsess)
            self.label_VAZARI_left.setFont(self.font_punish_and_succsess)
            self.label_SHIDO_left.setFont(self.font_punish_and_succsess)
            self.label_IPPON_left.setFont(self.font_punish_and_succsess)
            self.label_VAZARI_score_left.setFont(self.font_punish_and_succsess)
            self.label_IPPON_score_left.setFont(self.font_punish_and_succsess)
            self.label_SHIDO_score_left.setFont(self.font_punish_and_succsess)

            self.label_VAZARI_right.setFont(self.font_punish_and_succsess)
            self.label_SHIDO_right.setFont(self.font_punish_and_succsess)
            self.label_IPPON_right.setFont(self.font_punish_and_succsess)
            self.label_YKO_score_right.setFont(self.font_punish_and_succsess)
            self.label_VAZARI_score_right.setFont(self.font_punish_and_succsess)
            self.label_IPPON_score_right.setFont(self.font_punish_and_succsess)
            self.label_YKO_right.setFont(self.font_punish_and_succsess)
            self.label_SHIDO_score_right.setFont(self.font_punish_and_succsess)

            ############## hold label #####################
            self.label_hold_left.setFont(self.font_hold)
            self.label_hold_right.setFont(self.font_hold)

            ################## score title ##########################
            self.label_score_title_left.setFont(self.font_label_score)
            self.label_score_title_right.setFont(self.font_label_score)

            ################## total score ##########################
            self.label_total_score_left.setFont(self.font_total_score)
            self.label_total_score_right.setFont(self.font_total_score)

            ################## timer counter ######################
            self.label_timer.setFont(self.font_timer)

            ################## title timer label ######################3
            self.label_title_time.setFont(self.font_label_time)

            #################### area number ############################
            self.pushButton_area_number.setFont(self.font_area_number)

