from PyQt5 import QtCore, QtGui, QtWidgets


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
        self.label_full_name_left = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Dubai Medium")
        font.setPointSize(30)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(7)
        self.label_full_name_left.setFont(font)
        self.label_full_name_left.setStyleSheet("\n"
"    font: 57 30pt \"Dubai Medium\";\n"
"")
        self.label_full_name_left.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_full_name_left.setObjectName("label_full_name_left")
        self.verticalLayout_2.addWidget(self.label_full_name_left)
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
        self.label_IPPON_score_left = QtWidgets.QLabel(self.centralwidget)
        self.label_IPPON_score_left.setStyleSheet("\n"
"\n"
"font: 63 20pt \"Sitka Heading Semibold\";")
        self.label_IPPON_score_left.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_IPPON_score_left.setObjectName("label_IPPON_score_left")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.label_IPPON_score_left)
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
        self.pushButton_IPPON_left.setObjectName("pushButton_IPPON_left")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.pushButton_IPPON_left)
        self.label_VAZARI_score_left = QtWidgets.QLabel(self.centralwidget)
        self.label_VAZARI_score_left.setStyleSheet("\n"
"\n"
"font: 63 20pt \"Sitka Heading Semibold\";")
        self.label_VAZARI_score_left.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_VAZARI_score_left.setObjectName("label_VAZARI_score_left")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.label_VAZARI_score_left)
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
        self.pushButton_VAZARI_left.setObjectName("pushButton_VAZARI_left")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.pushButton_VAZARI_left)
        self.label_SHIDO_score_left = QtWidgets.QLabel(self.centralwidget)
        self.label_SHIDO_score_left.setStyleSheet("\n"
"\n"
"font: 63 20pt \"Sitka Heading Semibold\";")
        self.label_SHIDO_score_left.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_SHIDO_score_left.setObjectName("label_SHIDO_score_left")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.label_SHIDO_score_left)
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
        self.label_YKO_score_left = QtWidgets.QLabel(self.centralwidget)
        self.label_YKO_score_left.setStyleSheet("\n"
"\n"
"font: 63 20pt \"Sitka Heading Semibold\";")
        self.label_YKO_score_left.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_YKO_score_left.setObjectName("label_YKO_score_left")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.label_YKO_score_left)
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
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setStyleSheet("QPushButton {\n"
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
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout_4.addWidget(self.pushButton)
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Sitka Heading Semibold")
        font.setPointSize(20)
        self.label_7.setFont(font)
        self.label_7.setAlignment(QtCore.Qt.AlignCenter)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_4.addWidget(self.label_7)
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setStyleSheet("QPushButton {\n"
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
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout_4.addWidget(self.pushButton_2)
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
        self.label_sum_score_left_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_sum_score_left_2.setStyleSheet("color: #fff;\n"
"background: #000000;\n"
"font: 57 30pt \"Dubai Medium\";\n"
"\n"
"border-radius: 15px;\n"
"")
        self.label_sum_score_left_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_sum_score_left_2.setObjectName("label_sum_score_left_2")
        self.verticalLayout_12.addWidget(self.label_sum_score_left_2)
        self.horizontalLayout_3.addLayout(self.verticalLayout_12)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label_full_name_right = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Dubai Medium")
        font.setPointSize(30)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(7)
        self.label_full_name_right.setFont(font)
        self.label_full_name_right.setStyleSheet("\n"
"    font: 57 30pt \"Dubai Medium\";\n"
"")
        self.label_full_name_right.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_full_name_right.setObjectName("label_full_name_right")
        self.verticalLayout_4.addWidget(self.label_full_name_right)
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
        self.label_weight_category_right_2 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Dubai Medium")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(7)
        self.label_weight_category_right_2.setFont(font)
        self.label_weight_category_right_2.setStyleSheet("background-color: rgb(221, 221, 221);\n"
"font: 57 12pt \"Dubai Medium\";\n"
"\n"
"border-radius: 10px;\n"
"border: 1px solid black;\n"
"\n"
"padding-right: 10px;\n"
"padding-left: 10px;")
        self.label_weight_category_right_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_weight_category_right_2.setObjectName("label_weight_category_right_2")
        self.verticalLayout_5.addWidget(self.label_weight_category_right_2)
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
        self.pushButton_IPPON_right.setObjectName("pushButton_IPPON_right")
        self.formLayout_4.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.pushButton_IPPON_right)
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
        self.pushButton_VAZARI_right.setObjectName("pushButton_VAZARI_right")
        self.formLayout_4.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.pushButton_VAZARI_right)
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
        self.label_IPPON_score_left_4 = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_IPPON_score_left_4.sizePolicy().hasHeightForWidth())
        self.label_IPPON_score_left_4.setSizePolicy(sizePolicy)
        self.label_IPPON_score_left_4.setStyleSheet("\n"
"\n"
"font: 63 20pt \"Sitka Heading Semibold\";")
        self.label_IPPON_score_left_4.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_IPPON_score_left_4.setIndent(0)
        self.label_IPPON_score_left_4.setObjectName("label_IPPON_score_left_4")
        self.formLayout_4.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_IPPON_score_left_4)
        self.label_VAZARI_score_right = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_VAZARI_score_right.sizePolicy().hasHeightForWidth())
        self.label_VAZARI_score_right.setSizePolicy(sizePolicy)
        self.label_VAZARI_score_right.setStyleSheet("\n"
"\n"
"font: 63 20pt \"Sitka Heading Semibold\";")
        self.label_VAZARI_score_right.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_VAZARI_score_right.setIndent(0)
        self.label_VAZARI_score_right.setObjectName("label_VAZARI_score_right")
        self.formLayout_4.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_VAZARI_score_right)
        self.label_SHIDO_score_right = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_SHIDO_score_right.sizePolicy().hasHeightForWidth())
        self.label_SHIDO_score_right.setSizePolicy(sizePolicy)
        self.label_SHIDO_score_right.setStyleSheet("\n"
"\n"
"font: 63 20pt \"Sitka Heading Semibold\";")
        self.label_SHIDO_score_right.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_SHIDO_score_right.setIndent(0)
        self.label_SHIDO_score_right.setObjectName("label_SHIDO_score_right")
        self.formLayout_4.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_SHIDO_score_right)
        self.label_YKO_score_right = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_YKO_score_right.sizePolicy().hasHeightForWidth())
        self.label_YKO_score_right.setSizePolicy(sizePolicy)
        self.label_YKO_score_right.setStyleSheet("\n"
"\n"
"font: 63 20pt \"Sitka Heading Semibold\";")
        self.label_YKO_score_right.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_YKO_score_right.setIndent(0)
        self.label_YKO_score_right.setObjectName("label_YKO_score_right")
        self.formLayout_4.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.label_YKO_score_right)
        self.verticalLayout_4.addLayout(self.formLayout_4)
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Sitka Heading Semibold")
        font.setPointSize(20)
        self.label_9.setFont(font)
        self.label_9.setAlignment(QtCore.Qt.AlignCenter)
        self.label_9.setObjectName("label_9")
        self.verticalLayout_4.addWidget(self.label_9)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setStyleSheet("QPushButton {\n"
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
        self.pushButton_3.setObjectName("pushButton_3")
        self.horizontalLayout_6.addWidget(self.pushButton_3)
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Sitka Heading Semibold")
        font.setPointSize(20)
        self.label_10.setFont(font)
        self.label_10.setAlignment(QtCore.Qt.AlignCenter)
        self.label_10.setObjectName("label_10")
        self.horizontalLayout_6.addWidget(self.label_10)
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setStyleSheet("QPushButton {\n"
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
        self.pushButton_4.setObjectName("pushButton_4")
        self.horizontalLayout_6.addWidget(self.pushButton_4)
        self.verticalLayout_4.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_3.addLayout(self.verticalLayout_4)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.functions

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_full_name_left.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:36pt; font-weight:600;\">Иванов</span></p><p><span style=\" font-size:26pt; font-weight:600;\">Иван Иванович</span></p></body></html>"))
        self.label_weight_category_left.setText(_translate("MainWindow", "Весовая кат. - 22"))
        self.label_date_of_birth_left.setText(_translate("MainWindow", "19.02.2005"))
        self.label_team_left.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\">Школа</p><p align=\"center\">Одинцовская </p><p align=\"center\">СОШ 3</p></body></html>"))
        self.pushButton_YKO_left.setText(_translate("MainWindow", "ЮКО "))
        self.label_IPPON_score_left.setText(_translate("MainWindow", "0"))
        self.pushButton_IPPON_left.setText(_translate("MainWindow", "ИППОН"))
        self.label_VAZARI_score_left.setText(_translate("MainWindow", "0"))
        self.pushButton_VAZARI_left.setText(_translate("MainWindow", "ВАЗАРИ"))
        self.label_SHIDO_score_left.setText(_translate("MainWindow", "0"))
        self.pushButton_SHIDO_left.setText(_translate("MainWindow", "ШИДО"))
        self.label_YKO_score_left.setText(_translate("MainWindow", "<html><head/><body><p>0</p></body></html>"))
        self.label_8.setText(_translate("MainWindow", "УДЕРЖАНИЕ"))
        self.pushButton.setText(_translate("MainWindow", "Старт"))
        self.label_7.setText(_translate("MainWindow", "00:00"))
        self.pushButton_2.setText(_translate("MainWindow", "Стоп"))
        self.label_2.setText(_translate("MainWindow", "Очки"))
        self.label_sum_score_left.setText(_translate("MainWindow", "0"))
        self.label_fight_area_number.setText(_translate("MainWindow", "Ковер №1"))
        self.label_title_time.setText(_translate("MainWindow", "Время"))
        self.label_time_counter.setText(_translate("MainWindow", "00:00"))
        self.pushButton_time_pause.setText(_translate("MainWindow", "Пауза"))
        self.pushButton_time_continue.setText(_translate("MainWindow", "Продолжить"))
        self.pushButton_time_start.setText(_translate("MainWindow", "Старт"))
        self.pushButton_close_scoreboard.setText(_translate("MainWindow", "Закрыть\n"
"табло"))
        self.pushButton_open_scoreboard.setText(_translate("MainWindow", "Вывести\n"
" табло"))
        self.label_4.setText(_translate("MainWindow", "Очки"))
        self.label_sum_score_left_2.setText(_translate("MainWindow", "0"))
        self.label_full_name_right.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:36pt; font-weight:600;\">Иванов</span></p><p><span style=\" font-size:26pt; font-weight:600;\">Иван Иванович</span></p></body></html>"))
        self.label_team_right.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\">Школа</p><p align=\"center\">Одинцовская </p><p align=\"center\">СОШ 3</p></body></html>"))
        self.label_weight_category_right_2.setText(_translate("MainWindow", "Весовая кат. - 22"))
        self.label_date_of_birth_right.setText(_translate("MainWindow", "19.02.2005"))
        self.pushButton_YKO_right.setText(_translate("MainWindow", "ЮКО "))
        self.pushButton_IPPON_right.setText(_translate("MainWindow", "ИППОН"))
        self.pushButton_VAZARI_right.setText(_translate("MainWindow", "ВАЗАРИ"))
        self.pushButton_SHIDO_right.setText(_translate("MainWindow", "ШИДО"))
        self.label_IPPON_score_left_4.setText(_translate("MainWindow", "0"))
        self.label_VAZARI_score_right.setText(_translate("MainWindow", "0"))
        self.label_SHIDO_score_right.setText(_translate("MainWindow", "0"))
        self.label_YKO_score_right.setText(_translate("MainWindow", "<html><head/><body><p>0</p></body></html>"))
        self.label_9.setText(_translate("MainWindow", "УДЕРЖАНИЕ"))
        self.pushButton_3.setText(_translate("MainWindow", "Старт"))
        self.label_10.setText(_translate("MainWindow", "00:00"))
        self.pushButton_4.setText(_translate("MainWindow", "Стоп"))


    def functions(self):
            pass


    def change_area_number(self, number):
            self.label_fight_area_number.setText(f"Ковер №{number}")