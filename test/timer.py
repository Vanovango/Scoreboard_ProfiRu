from PyQt5.QtWidgets import (QMainWindow, QPushButton, QLabel, QVBoxLayout, QWidget,
                             QTimeEdit, QDialog, QMessageBox, QHBoxLayout)
from PyQt5 import QtWidgets
from PyQt5.QtCore import QTimer, QTime, Qt
import sys


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Таймер")
        self.setGeometry(100, 100, 400, 200)

        # Создаем виджеты
        self.timer_label = QLabel("00:00", self)
        self.timer_label.setAlignment(Qt.AlignCenter)
        self.timer_label.setStyleSheet("font-size: 40px;")

        self.start_button = QPushButton("Запустить таймер", self)
        self.start_button.clicked.connect(self.show_time_dialog)

        # Размещаем виджеты
        layout = QVBoxLayout()
        layout.addWidget(self.timer_label)
        layout.addWidget(self.start_button)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

        # Инициализируем таймер
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_timer)
        self.remaining_time = QTime(0, 0, 0)

    def show_time_dialog(self):
        """Открывает диалоговое окно для выбора времени"""
        dialog = QDialog(self)
        dialog.setWindowTitle("Выберите время")

        time_edit = QTimeEdit()
        time_edit.setDisplayFormat("mm:ss")
        time_edit.setTime(QTime(1, 0))  # Устанавливаем время по умолчанию 00:01:00

        ok_button = QPushButton("OK")
        ok_button.clicked.connect(lambda: self.start_countdown(time_edit.time(), dialog))

        layout = QVBoxLayout()
        layout.addWidget(time_edit)
        layout.addWidget(ok_button)
        dialog.setLayout(layout)

        dialog.exec_()

    def start_countdown(self, time, dialog):
        """Начинает обратный отсчет"""
        dialog.close()

        self.remaining_time = time
        self.update_timer_display()

        if not self.timer.isActive():
            self.timer.start(1000)  # Обновляем каждую секунду

    def update_timer(self):
        """Обновляет оставшееся время"""
        if self.remaining_time == QTime(0, 0):
            self.timer.stop()
            QMessageBox.information(self, "Таймер", "Время вышло!")
            return

        self.remaining_time = self.remaining_time.addSecs(-1)
        self.update_timer_display()

    def update_timer_display(self):
        """Обновляет текст QLabel"""
        self.timer_label.setText(self.remaining_time.toString("mm:ss"))





if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)

    wind = MainWindow()

    wind.show()

    sys.exit(app.exec_())