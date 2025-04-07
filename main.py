from PyQt5 import QtCore, QtGui, QtWidgets
from main_panel import Ui_MainWindow
from manege_fight_area_window import Ui_FightManageWindow
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

    def close_all_windows():
        for window in FIGHT_AREA_WINDOWS:
            window[0].close()


    main_panel_ui.pushButton_add_fight_area.clicked.connect(add_fight_area)
    main_panel_ui.pushButton_close_all.clicked.connect(close_all_windows)

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)

    start_app()

    sys.exit(app.exec_())

