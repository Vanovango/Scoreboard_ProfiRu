from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIcon

from start_window import Ui_StartWindow
from manage_panel import Ui_ManagePanel
from scoreborde_user import Ui_Scoreboard


import sys


NUMBER_OF_FIGHT_AREA = [0]
FIGHT_AREA_WINDOWS = []
SCOREBOARD_WINDOWS = []
FIGHTERS_LIST = {}
TEAMS_LIST = {}
RESULT_OF_FIGHTS = {}
DATABASE_PATH = ''
MATCHES_END_NUMBER = 0

def set_area_number(areas_list):
    for i in range(1, len(areas_list)):
        if not areas_list[i] - areas_list[i - 1] == 1:
            return areas_list[i - 1] + 1
    return max(areas_list) + 1

################################################# start app ############################################################
def start_app():
    global StartWindow
    StartWindow = QtWidgets.QMainWindow()
    StartWindow.setWindowIcon(QIcon("images/judo-main.png"))
    start_window_ui = Ui_StartWindow()
    start_window_ui.setupUi(StartWindow)

    StartWindow.show()

############################################# add manage panel #########################################################
    def add_fight_area():
        if not FIGHTERS_LIST:
            get_file_path()

        global NUMBER_OF_FIGHT_AREA
        new_area_number = set_area_number(NUMBER_OF_FIGHT_AREA)
        NUMBER_OF_FIGHT_AREA.append(new_area_number)

        # open exist window or create new
        open_new_window = True
        for window in FIGHT_AREA_WINDOWS:
            if window['index'] == new_area_number:
                window['window'].show()
                open_new_window = False

        if open_new_window:
            global FightManage
            FightManage = QtWidgets.QMainWindow()
            FightManage.setWindowIcon(QIcon("images/judo-main.png"))
            fight_manage_ui = Ui_ManagePanel()
            fight_manage_ui.setupUi(FightManage)

            FIGHT_AREA_WINDOWS.append({'window': FightManage, 'ui': fight_manage_ui, 'index': new_area_number})
            FIGHT_AREA_WINDOWS[-1]['window'].show()


        FIGHT_AREA_WINDOWS[-1]['ui'].open_manage_panel(new_area_number, FIGHTERS_LIST)

        NUMBER_OF_FIGHT_AREA.sort()

        # test prints
        # print("########## open manage panel ###########")
        # print(f"FIGHT_AREA_WINDOWS - {FIGHT_AREA_WINDOWS}")
        # print(f"SCOREBOARD_WINDOWS - {SCOREBOARD_WINDOWS}")
        # print(f"NUMBER_OF_FIGHT_AREA - {NUMBER_OF_FIGHT_AREA}")

        def open_scoreboard(index):
            # open exist window or create new
            open_new_scoreboard = True
            for scoreboard in SCOREBOARD_WINDOWS:
                if scoreboard['index'] == new_area_number:
                    scoreboard['window'].show()
                    open_new_scoreboard = False

            if open_new_scoreboard:
                ScoreboardWindow = QtWidgets.QMainWindow()
                ScoreboardWindow.setWindowIcon(QIcon("images/judo-main.png"))
                ui_scoreboard = Ui_Scoreboard()
                ui_scoreboard.setupUi(ScoreboardWindow)

                ui_scoreboard.change_area_number(index)

                SCOREBOARD_WINDOWS.append({'window':ScoreboardWindow, 'ui':ui_scoreboard, 'index':index})
                SCOREBOARD_WINDOWS[-1]['window'].show()


            # save link in current manage window for check changes
            for scoreboard in SCOREBOARD_WINDOWS:
                if scoreboard['index'] == index:

                    for manage_panel in FIGHT_AREA_WINDOWS:
                        if manage_panel['index'] == index:
                            manage_panel['ui'].save_scoreboard_link(scoreboard)

            # test prints
            # print("########## open scoreboard ###########")
            # print(f"FIGHT_AREA_WINDOWS - {FIGHT_AREA_WINDOWS}")
            # print(f"SCOREBOARD_WINDOWS - {SCOREBOARD_WINDOWS}")
            # print(f"NUMBER_OF_FIGHT_AREA - {NUMBER_OF_FIGHT_AREA}")

        def close_index_windows(index):
            # close current window and scoreboard
            for scoreboard in SCOREBOARD_WINDOWS:
                if scoreboard['index'] == index:
                    scoreboard['window'].close()
                    # del SCOREBOARD_WINDOWS[SCOREBOARD_WINDOWS.index(scoreboard)]

            for manage_panel in FIGHT_AREA_WINDOWS:
                if manage_panel['index'] == index:
                    manage_panel['window'].close()
                    # del FIGHT_AREA_WINDOWS[FIGHT_AREA_WINDOWS.index(manage_panel)]

            del NUMBER_OF_FIGHT_AREA[NUMBER_OF_FIGHT_AREA.index(index)]

            # test prints
            # print("########## close scoreboard ###########")
            # print(f"FIGHT_AREA_WINDOWS - {FIGHT_AREA_WINDOWS}")
            # print(f"SCOREBOARD_WINDOWS - {SCOREBOARD_WINDOWS}")
            # print(f"NUMBER_OF_FIGHT_AREA - {NUMBER_OF_FIGHT_AREA}")


        ########################## open and close scoreboard ############################
        FIGHT_AREA_WINDOWS[-1]['ui'].pushButton_open_scoreboard.clicked.connect(
            lambda checked, index=new_area_number: open_scoreboard(index)
        )
        FIGHT_AREA_WINDOWS[-1]['ui'].pushButton_close_scoreboard.clicked.connect(
            lambda checked, index=new_area_number: close_index_windows(index)
        )
        #################################################################################

##################################### open chose data source window ####################################################
    def get_file_path():
        global DATABASE_PATH
        DATABASE_PATH = QtWidgets.QFileDialog.getOpenFileName()[0]

        load_list_from_exel()



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

        NUMBER_OF_FIGHT_AREA = [0]

        # test prints
        # print("########## close all windows ###########")
        # print(f"FIGHT_AREA_WINDOWS - {FIGHT_AREA_WINDOWS}")
        # print(f"SCOREBOARD_WINDOWS - {SCOREBOARD_WINDOWS}")
        # print(f"NUMBER_OF_FIGHT_AREA - {NUMBER_OF_FIGHT_AREA}")


    ################################### start window buttons ##################################################
    start_window_ui.pushButton_add_fight_area.clicked.connect(add_fight_area)
    start_window_ui.pushButton_close_all.clicked.connect(close_all_windows)


####################################### load data about fighters from exel ############################################
def load_list_from_exel():
    import pandas as pd
    global FIGHTERS_LIST, TEAMS_LIST

    if DATABASE_PATH == '':
        pass
    else:
        df = pd.read_excel(DATABASE_PATH)
        df = df.replace('\xa0', '', regex=True)
        FIGHTERS_LIST = df.to_dict(orient='list')


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)

    start_app()

    sys.exit(app.exec_())

