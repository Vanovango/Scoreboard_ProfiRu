from PyQt5 import QtCore, QtGui, QtWidgets

from start_window import Ui_StartWindow
from manage_panel import Ui_ManagePanel
from data_sourse import Ui_DataSource

import sys


NUMBER_OF_FIGHT_AREA = 0
FIGHT_AREA_WINDOWS = []
FIGHTERS_LIST = {}
DATABASE_PATH = ''
MATCHES_END_NUMBER = 0

################################################# start app ############################################################
def start_app():
    global StartWindow
    StartWindow = QtWidgets.QMainWindow()
    start_window_ui = Ui_StartWindow()
    start_window_ui.setupUi(StartWindow)

    StartWindow.show()

############################################# add manage panel #########################################################
    def add_fight_area():
        global NUMBER_OF_FIGHT_AREA
        NUMBER_OF_FIGHT_AREA += 1

        global FightManage
        FightManage = QtWidgets.QMainWindow()
        fight_manage_ui = Ui_ManagePanel()
        fight_manage_ui.setupUi(FightManage)

        fight_manage_ui.change_area_number(NUMBER_OF_FIGHT_AREA)

        FIGHT_AREA_WINDOWS.append({'window':FightManage, 'ui':fight_manage_ui, 'index':NUMBER_OF_FIGHT_AREA})

        FIGHT_AREA_WINDOWS[-1]['window'].show()

##################################### open chose data source window ####################################################
    def chose_data_source():
        global DataSource
        DataSource = QtWidgets.QMainWindow()
        data_source_ui = Ui_DataSource()
        data_source_ui.setupUi(DataSource)

        DataSource.show()

        def get_file_path():
            global DATABASE_PATH
            DATABASE_PATH = QtWidgets.QFileDialog.getOpenFileName()[0]

            load_list_from_exel()

            DataSource.close()

        def get_data_form_google():
            pass

        ################################ data source window buttons ####################################################
        data_source_ui.pushButton_chose_file.clicked.connect(get_file_path)
        data_source_ui.pushButton_connect_google.clicked.connect(get_data_form_google)

############################################ show fighters info ########################################################
    def show_fighters():
        print(DATABASE_PATH)
        # import os
        #
        # os.system(f"start EXCEL.EXE {DATABASE_PATH}")

############################################## close all panels ########################################################
    def close_all_windows():
        for window in FIGHT_AREA_WINDOWS:
            window['window'].close()

        global NUMBER_OF_FIGHT_AREA
        NUMBER_OF_FIGHT_AREA = 0

    ################################### start window buttons ##################################################
    start_window_ui.pushButton_add_fight_area.clicked.connect(add_fight_area)
    start_window_ui.pushButton_close_all.clicked.connect(close_all_windows)
    start_window_ui.pushButton_add_fighters_list.clicked.connect(chose_data_source)
    start_window_ui.pushButton_show_fighters_list.clicked.connect(show_fighters)


####################################### load data about fighters from exel ############################################
def load_list_from_exel():
    import pandas as pd
    global FIGHTERS_LIST

    df = pd.read_excel(DATABASE_PATH)

    FIGHTERS_LIST = df.to_dict(orient='list')

    print(FIGHTERS_LIST)

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)

    start_app()

    sys.exit(app.exec_())

