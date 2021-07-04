import sys, os
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog, QWidget
from qtwidgets import Toggle, AnimatedToggle

from Ui_MainWindow import Ui_MainWindow

class CSS_Styles():
    def __init__(self):
        # initialize main window
        self.main_win = QMainWindow()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self.main_win)

        self.ui.click_domain.setStyleSheet("background:#C4C4C4;border:solid;")
        self.check = 'CHECK!!!'
        print(self.check)
