import sys, os
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog, QWidget

from Ui_MainWindow import Ui_MainWindow

class MainWindow:
    def __init__(self):
        self.main_win = QMainWindow()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self.main_win)

        self.ui.stackedWidget.setCurrentWidget(self.ui.home)

        self.ui.autostart.toggled.connect(self.click_auto)

        self.ui.click_domain.clicked.connect(self.showDomain)

        self.ui.click_repo.clicked.connect(self.showRepo)
        self.ui.repo_choose_file.clicked.connect(self.upload_liscence)

        self.ui.click_theme.clicked.connect(self.showTheme)

        self.ui.click_conf.clicked.connect(self.showConf)

        self.ui.click_account.clicked.connect(self.showAccount)

        self.ui.click_user.clicked.connect(self.showUser)

        self.ui.click_info.clicked.connect(self.showInfo)


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

    def upload_liscence(self):
        file_filter = 'Certificate (*.crt);; Any (*)'
        response = QFileDialog.getOpenFileName(parent=QWidget(),
                                              caption='select a file',
                                              directory='os.getcwd()',
                                              filter=file_filter,
                                              initialFilter='Any (*)')
        print(response)


    def show(self):
        self.main_win.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_win = MainWindow()
    main_win.show()
    sys.exit(app.exec_())
