from PyQt5 import QtCore, QtGui, QtWidgets

from main_panel import Ui_MainWindow
from manege_fight_area_window import Ui_FightManageWindow
from data_sourse import Ui_DataSource

import sys


NUMBER_OF_FIGHT_AREA = 0
FIGHT_AREA_WINDOWS = []
DATABASE_PATH = ''
MATCHES_END_NUMBER = 0


def start_app():
    global MainPanel
    MainPanel = QtWidgets.QMainWindow()
    main_panel_ui = Ui_MainWindow()
    main_panel_ui.setupUi(MainPanel)

    MainPanel.show()

    def add_fight_area():
        global NUMBER_OF_FIGHT_AREA
        NUMBER_OF_FIGHT_AREA += 1

        global FightManage
        FightManage = QtWidgets.QMainWindow()
        fight_manage_ui = Ui_FightManageWindow()
        fight_manage_ui.setupUi(FightManage)

        FIGHT_AREA_WINDOWS.append((FightManage, fight_manage_ui))

        FIGHT_AREA_WINDOWS[-1][0].show()

    def chose_data_source():
        global DataSource
        DataSource = QtWidgets.QMainWindow()
        data_source_ui = Ui_DataSource()
        data_source_ui.setupUi(DataSource)

        DataSource.show()

        def get_file_path():
            global DATABASE_PATH
            DATABASE_PATH = QtWidgets.QFileDialog.getOpenFileName()[0]

            DataSource.close()

        def get_data_form_google():
            pass

        data_source_ui.pushButton_chose_file.clicked.connect(get_file_path)
        data_source_ui.pushButton_connect_google.clicked.connect(get_data_form_google)

    def show_fighters():
        print(DATABASE_PATH)
        # import os
        #
        # os.system(f"start EXCEL.EXE {DATABASE_PATH}")


    def close_all_windows():
        for window in FIGHT_AREA_WINDOWS:
            window[0].close()


    main_panel_ui.pushButton_add_fight_area.clicked.connect(add_fight_area)
    main_panel_ui.pushButton_close_all.clicked.connect(close_all_windows)
    main_panel_ui.pushButton_add_fighters_list.clicked.connect(chose_data_source)
    main_panel_ui.pushButton_show_fighters_list.clicked.connect(show_fighters)

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)

    start_app()

    sys.exit(app.exec_())

