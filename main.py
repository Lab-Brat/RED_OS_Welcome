import sys, os
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog, QWidget
from qtwidgets import Toggle, AnimatedToggle

from Ui_MainWindow import Ui_MainWindow

class MainWindow:
    def __init__(self):
        self.main_win = QMainWindow()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self.main_win)

        self.main_win.setStyleSheet("background:#E5E5E5;")

        self.ui.stackedWidget.setCurrentWidget(self.ui.home)

        self.ui.autostart.toggled.connect(self.click_auto)

        self.ui.click_domain.clicked.connect(self.showDomain)
        self.ui.save_domain.clicked.connect(self.save_dom)

        self.ui.click_repo.clicked.connect(self.showRepo)
        self.ui.repo_choose_file.clicked.connect(self.upload_liscence)

        self.ui.click_theme.clicked.connect(self.showTheme)
        self.ui.theme_btn.clicked.connect(lambda: os.system("sh -c 'mate-appearance-properties'"))

        self.ui.click_conf.clicked.connect(self.showConf)
        self.ui.check_geo.toggled.connect(self.click_geo)
        self.ui.send_auto.toggled.connect(self.send_logs)
        self.ui.send_not.toggled.connect(self.send_logs)

        self.ui.click_account.clicked.connect(self.showAccount)
        self.ui.gnome_account.clicked.connect(lambda: os.system("sh -c 'gnome-control-center online-accounts'"))

        self.ui.click_user.clicked.connect(self.showUser)
        self.ui.gnome_user.clicked.connect(lambda: os.system("sh -c 'gnome-control-center user-accounts'"))
        self.ui.gnome_special.clicked.connect(lambda: os.system("sh -c 'gnome-control-center universal-access'"))

        self.ui.click_info.clicked.connect(self.showInfo)

        self.ui.click_account.setStyleSheet("width:195")

        self.ui.click_domain.setStyleSheet("background:#C4C4C4;border:solid;")

        self.ui.click_repo.setStyleSheet("background:#C4C4C4;border:solid;")

        self.ui.click_theme.setStyleSheet("background:#C4C4C4;border:solid;")

        self.ui.click_conf.setStyleSheet("background:#C4C4C4;border:solid;")

        self.ui.click_account.setStyleSheet("background:#C4C4C4;border:solid;")

        self.ui.click_user.setStyleSheet("background:#C4C4C4;border:solid;")

        self.ui.click_info.setStyleSheet("background:#C4C4C4;border:solid;")

        self.ui.page_account.setStyleSheet("background:#FFFFFF;border:solid;border-radius:20px;")
        self.ui.page_info.setStyleSheet("background:#FFFFFF;border:solid;border-radius:20px;")
        self.ui.page_conf.setStyleSheet("background:#FFFFFF;border:solid;border-radius:20px;")
        self.ui.page_domain.setStyleSheet("background:#FFFFFF;border:solid;border-radius:20px;")
        self.ui.page_repo.setStyleSheet("background:#FFFFFF;border:solid;border-radius:20px;")
        self.ui.page_theme.setStyleSheet("background:#FFFFFF;border:solid;border-radius:20px;")
        self.ui.page_user.setStyleSheet("background:#FFFFFF;border:solid;border-radius:20px;")
        self.ui.stackedWidget.setStyleSheet("background:#FFFFFF;border:solid;border-radius:20px;")
        self.ui.top.setStyleSheet("background:#383838;")
        self.ui.top2.setStyleSheet("background:#FFFFFF;border-radius:20px;")
        self.ui.menu.setStyleSheet("background:#FFFFFF;border-radius:20px;")
        self.ui.redos_icon.setStyleSheet("background:#FFFFFF;")
        self.ui.widget.setStyleSheet("background:#EC080E;border-radius:1px;")
        self.ui.home.setStyleSheet("background:#FFFFFF;border-radius:20px;")

    def showRepo(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.page_repo)

    def showDomain(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.page_domain)

    def showTheme(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.page_theme)

    def showConf(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.page_conf)

    def showAccount(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.page_account)

    def showUser(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.page_user)

    def showInfo(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.page_info)

    def click_auto(self):
        if self.ui.autostart.isChecked() == True:
            param = 1
            out = lambda: os.system('./Autoload.sh {0}'.format(param))
            out()
        else:
            param = 0
            out = lambda: os.system('./Autoload.sh {0}'.format(param))
            out()

    def click_geo(self):
        if self.ui.check_geo.isChecked() == True:
            param = 1
            out = lambda: os.system('./Location.sh {0}'.format(param))
            out()
        else:
            param = 0
            out = lambda: os.system('./Location.sh {0}'.format(param))
            out()

    def upload_liscence(self):
        file_filter = 'Certificate (*.crt);; Any (*)'
        response = QFileDialog.getOpenFileName(parent=QWidget(),
                                              caption='select a file',
                                              directory='os.getcwd()',
                                              filter=file_filter,
                                              initialFilter='Any (*)')
        print(response)

    def save_dom(self):
        sender = QWidget().sender()
        if sender.text() == "Сохранить":
            f1 = self.ui.inp_comp_name.text()
            f2 = self.ui.inp_dn.text()
            f3 = self.ui.inp_dip.text()
            f4 = self.ui.inp_admn.text()
            f5 = self.ui.inp_admp.text()
            f = open("dom_data.txt", "w")
            #f.write(f1+'\n'+f2+'\n'+f3+'\n'+f4+'\n'+f5+'\n')
            f = lambda: os.system("sh -c 'Domain.sh {0} {1} {2} {3}'".format(f2,f1,f4,f5))

    def send_logs(self):
        if self.ui.send_auto.isChecked() == True:
            log_mode = 'auto'

        elif self.ui.send_not.isChecked() == True:
            log_mode = 'none'
        else:
            log_mode = 'no entry'


    def show(self):
        self.main_win.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_win = MainWindow()
    main_win.show()
    sys.exit(app.exec_())
