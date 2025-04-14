
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

        self.pushButton_save_results = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Sitka Heading Semibold")
        font.setPointSize(16)
        self.pushButton_save_results.setFont(font)
        self.pushButton_save_results.setObjectName("pushButton_close_all")
        self.gridLayout.addWidget(self.pushButton_save_results, 3, 0, 1, 1)

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

        self.functions()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Главная"))
        self.pushButton_add_fight_area.setText(_translate("MainWindow", "Добавить мониторинг ковра"))
        self.pushButton_close_all.setText(_translate("MainWindow", "Закрыть все окна"))
        self.label_title.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\">Табло </p><p align=\"center\">для проведения </p><p align=\"center\">соревнований по Дзюдо</p></body></html>"))
        self.pushButton_save_results.setText(_translate("MainWindow", "Сохранить результаты"))

    def functions(self):
        self.pushButton_save_results.clicked.connect(self.save_results)


    @staticmethod
    def save_results():
        print(111)
        import os
        import pandas as pd
        from openpyxl import Workbook
        from openpyxl.utils.dataframe import dataframe_to_rows
        from PyQt5.QtWidgets import (QApplication, QFileDialog, QMessageBox)
        from PyQt5.QtCore import QCoreApplication

        from main import TEAMS_LIST, RESULT_OF_FIGHTS

        # Инициализация QApplication
        app = QApplication.instance() or QCoreApplication([])

        # Выбор директории для сохранения
        folder_path = QFileDialog.getExistingDirectory(
            None,
            "Выберите папку для сохранения результатов",
            os.path.expanduser("~"),
            QFileDialog.ShowDirsOnly
        )

        if not folder_path:
            QMessageBox.information(None, "Отменено", "Сохранение отменено пользователем")
            return

        df_teams_list = pd.DataFrame(data=TEAMS_LIST)
        df_res_of_fights = pd.DataFrame(data=RESULT_OF_FIGHTS)

        df_teams_list = df_teams_list.T
        df_res_of_fights = df_res_of_fights.T

        try:
            df_teams_list.to_excel(f'{folder_path}\статистика_команд.xlsx')
            df_res_of_fights.to_excel(f'{folder_path}\результаты_встреч.xlsx')
            QMessageBox.information(
                None,
                "Сохранено",
                f"Файлы успешно сохранены в папке:\n{folder_path}",
                QMessageBox.Ok
            )
        except Exception as e:
            QMessageBox.critical(
                None,
                "Ошибка",
                f"Не удалось сохранить файл:\n{str(e)}",
                QMessageBox.Ok
            )
