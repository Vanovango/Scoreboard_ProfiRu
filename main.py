from PyQt5 import QtCore, QtGui, QtWidgets

from start_window import Ui_StartWindow
from manage_panel import Ui_ManagePanel
from data_sourse import Ui_DataSource
from scoreborde_user import Ui_Scoreboard

import sys


NUMBER_OF_FIGHT_AREA = 0
FIGHT_AREA_WINDOWS = []
SCOREBOARD_WINDOWS = []
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

        fight_manage_ui.open_manage_panel(NUMBER_OF_FIGHT_AREA, FIGHTERS_LIST)

        ########################## open and close scoreboard ############################
        fight_manage_ui.pushButton_open_scoreboard.clicked.connect(
            lambda checked, index=NUMBER_OF_FIGHT_AREA: open_scoreboard(index)
        )
        fight_manage_ui.pushButton_close_scoreboard.clicked.connect(
            lambda checked, index=NUMBER_OF_FIGHT_AREA: close_scoreboard(index)
        )
        #################################################################################

        FIGHT_AREA_WINDOWS.append({'window':FightManage, 'ui':fight_manage_ui, 'index':NUMBER_OF_FIGHT_AREA})
        FIGHT_AREA_WINDOWS[-1]['window'].show()


        def open_scoreboard(index):
            ScoreboardWindow = QtWidgets.QMainWindow()
            ui_scoreboard = Ui_Scoreboard()
            ui_scoreboard.setupUi(ScoreboardWindow)

            ui_scoreboard.change_area_number(index)
            SCOREBOARD_WINDOWS.append({'window':ScoreboardWindow, 'ui':ui_scoreboard, 'index':index})

            for scoreboard in SCOREBOARD_WINDOWS:
                if scoreboard['index'] == index:
                    scoreboard['window'].show()


            for scoreboard in SCOREBOARD_WINDOWS:
                if scoreboard['index'] == index:

                    for manage_panel in FIGHT_AREA_WINDOWS:
                        if manage_panel['index'] == index:
                            manage_panel['ui'].save_scoreboard_link(scoreboard)

        def close_scoreboard(index):
            for scoreboard in SCOREBOARD_WINDOWS:
                if scoreboard['index'] == index:
                    scoreboard['window'].close()
                    del scoreboard


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


############################################## close all panels ########################################################
    def close_all_windows():
        global NUMBER_OF_FIGHT_AREA

        for window in FIGHT_AREA_WINDOWS:
            window['window'].close()

        for window in SCOREBOARD_WINDOWS:
            window['window'].close()


        NUMBER_OF_FIGHT_AREA = 0
        FIGHT_AREA_WINDOWS.clear()
        SCOREBOARD_WINDOWS.clear()

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

