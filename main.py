import sys, os
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog, QWidget
from qtwidgets import Toggle, AnimatedToggle

from Ui_MainWindow import Ui_MainWindow
from css_config import CSS_Styles


class MainWindow:
    def __init__(self):
        # initialize main window
        self.main_win = QMainWindow()
        self.main_win.setStyleSheet("background:#E5E5E5;")
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self.main_win)

        # initialize stacked widget
        self.ui.stackedWidget.setCurrentWidget(self.ui.home)
        self.ui.stackedWidget.setStyleSheet("background:#FFFFFF;border:solid;border-radius:20px;")

        # add event to autostart button
        self.ui.autostart.toggled.connect(self.send_io)

        # add event to domain button
        self.ui.click_domain.clicked.connect(self.change_page)
        # self.ui.click_domain.setStyleSheet("background:#C4C4C4;border:solid;")
        self.ui.save_domain.clicked.connect(self.save_dom)

        # add event to repository button
        self.ui.click_repo.clicked.connect(self.change_page)
        self.ui.click_repo.setStyleSheet("background:#C4C4C4;border:solid;")
        self.ui.repo_choose_file.clicked.connect(self.upload_liscence)

        # add event to choose theme button
        self.ui.click_theme.clicked.connect(self.change_page)
        self.ui.click_theme.setStyleSheet("background:#C4C4C4;border:solid;")
        self.ui.theme_btn.clicked.connect(lambda: os.system("sh -c 'mate-appearance-properties'"))

        # add event to confidentiality button
        self.ui.click_conf.clicked.connect(self.change_page)
        self.ui.click_conf.setStyleSheet("background:#C4C4C4;border:solid;")
        self.ui.check_geo.toggled.connect(self.send_io)
        self.ui.send_auto.toggled.connect(self.send_logs)
        self.ui.send_not.toggled.connect(self.send_logs)

        # add event to online accounts button
        self.ui.click_account.clicked.connect(self.change_page)
        self.ui.click_account.setStyleSheet("background:#C4C4C4;border:solid;")
        self.ui.gnome_account.clicked.connect(lambda: os.system("sh -c 'gnome-control-center online-accounts'"))

        # add event to user information button
        self.ui.click_user.clicked.connect(self.change_page)
        self.ui.click_user.setStyleSheet("background:#C4C4C4;border:solid;")
        self.ui.gnome_user.clicked.connect(lambda: os.system("sh -c 'gnome-control-center user-accounts'"))
        self.ui.gnome_special.clicked.connect(lambda: os.system("sh -c 'gnome-control-center universal-access'"))

        # add event to company information button
        self.ui.click_info.clicked.connect(self.change_page)
        self.ui.click_info.setStyleSheet("background:#C4C4C4;border:solid;")

        self.ui.repo_choose_file.setStyleSheet("background:#C4C4C4;border:solid;")
        self.ui.repo_upload.setStyleSheet("background:#C4C4C4;border:solid;")

        self.ui.inp_admn.setStyleSheet("background:#C4C4C4;border:solid;")
        self.ui.inp_admp.setStyleSheet("background:#C4C4C4;border:solid;")
        self.ui.inp_comp_name.setStyleSheet("background:#C4C4C4;border:solid;")
        self.ui.inp_dn.setStyleSheet("background:#C4C4C4;border:solid;")
        self.ui.inp_dip.setStyleSheet("background:#C4C4C4;border:solid;")

        # change styles of pages on stacked widget
        self.ui.page_account.setStyleSheet("background:#FFFFFF;border:solid;border-radius:20px;")
        self.ui.page_info.setStyleSheet("background:#FFFFFF;border:solid;border-radius:20px;")
        self.ui.page_conf.setStyleSheet("background:#FFFFFF;border:solid;border-radius:20px;")
        self.ui.page_domain.setStyleSheet("background:#FFFFFF;border:solid;border-radius:20px;")
        self.ui.page_repo.setStyleSheet("background:#FFFFFF;border:solid;border-radius:20px;")
        self.ui.page_theme.setStyleSheet("background:#FFFFFF;border:solid;border-radius:20px;")
        self.ui.page_user.setStyleSheet("background:#FFFFFF;border:solid;border-radius:20px;")

        # change styles of bars amd menus
        self.ui.top.setStyleSheet("background:#383838;")
        self.ui.top2.setStyleSheet("background:#FFFFFF;border-radius:20px;")
        self.ui.menu.setStyleSheet("background:#FFFFFF;border-radius:20px;")
        self.ui.redos_icon.setStyleSheet("background:#FFFFFF;")
        self.ui.widget.setStyleSheet("background:#EC080E;border-radius:1px;")
        self.ui.home.setStyleSheet("background:#FFFFFF;border-radius:20px;")

        CSS_Styles()


    def change_page(self):
        page = QWidget().sender().objectName()
        page = page.replace('click', 'page')
        page_ref = 'self.ui.' + str(page)

        self.ui.stackedWidget.setCurrentWidget(eval(page_ref))

    def send_io(self):
        btn = QWidget().sender().objectName()
        if btn == 'check_geo':
            scrpt = './Location.sh '
        elif btn == 'autostart':
            scrpt = './Autoload.sh '
        btn_status = 'self.ui.' + btn + '.isChecked()'

        if eval(btn_status) == True: param = 1
        else: param = 0
        print((scrpt+str(param)))
        # out = lambda: os.system(scrpt+str(param))
        # out()

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
            os.system('cat /var/log/syslog | grep error > systemreport.txt')
        elif self.ui.send_not.isChecked() == True:
            log_mode = 'none'
        else:
            log_mode = 'no entry'

    def show(self):
        self.main_win.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_win = MainWindow()
    # CSS_Styles()
    main_win.show()
    sys.exit(app.exec_())
