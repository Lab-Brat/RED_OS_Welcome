# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_maini.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(860, 640)
        MainWindow.setMinimumSize(QtCore.QSize(860, 640))
        MainWindow.setMaximumSize(QtCore.QSize(860, 640))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.click_repo = QtWidgets.QPushButton(self.centralwidget)
        self.click_repo.setGeometry(QtCore.QRect(23, 150, 185, 45))
        self.click_repo.setObjectName("click_repo")
        self.redos_icon = QtWidgets.QLabel(self.centralwidget)
        self.redos_icon.setGeometry(QtCore.QRect(23, 30, 120, 50))
        self.redos_icon.setText("")
        self.redos_icon.setPixmap(QtGui.QPixmap("logo.png"))
        self.redos_icon.setScaledContents(True)
        self.redos_icon.setObjectName("redos_icon")
        self.click_domain = QtWidgets.QPushButton(self.centralwidget)
        self.click_domain.setGeometry(QtCore.QRect(23, 205, 185, 45))
        self.click_domain.setObjectName("click_domain")
        self.click_conf = QtWidgets.QPushButton(self.centralwidget)
        self.click_conf.setGeometry(QtCore.QRect(23, 315, 185, 45))
        self.click_conf.setObjectName("click_conf")
        self.click_theme = QtWidgets.QPushButton(self.centralwidget)
        self.click_theme.setGeometry(QtCore.QRect(23, 260, 185, 45))
        self.click_theme.setObjectName("click_theme")
        self.click_user = QtWidgets.QPushButton(self.centralwidget)
        self.click_user.setGeometry(QtCore.QRect(23, 425, 185, 45))
        self.click_user.setObjectName("click_user")
        self.click_account = QtWidgets.QPushButton(self.centralwidget)
        self.click_account.setGeometry(QtCore.QRect(23, 370, 185, 45))
        self.click_account.setObjectName("click_account")
        self.click_info = QtWidgets.QPushButton(self.centralwidget)
        self.click_info.setGeometry(QtCore.QRect(23, 480, 185, 45))
        self.click_info.setObjectName("click_info")
        self.stackedWidget = QtWidgets.QStackedWidget(self.centralwidget)
        self.stackedWidget.setGeometry(QtCore.QRect(233, 130, 605, 415))
        self.stackedWidget.setObjectName("stackedWidget")
        self.home = QtWidgets.QWidget()
        self.home.setObjectName("home")
        self.home_label = QtWidgets.QLabel(self.home)
        self.home_label.setGeometry(QtCore.QRect(210, 130, 141, 61))
        self.home_label.setObjectName("home_label")
        self.stackedWidget.addWidget(self.home)
        self.page_repo = QtWidgets.QWidget()
        self.page_repo.setObjectName("page_repo")
        self.repo_upload = QtWidgets.QPushButton(self.page_repo)
        self.repo_upload.setGeometry(QtCore.QRect(90, 80, 89, 25))
        self.repo_upload.setObjectName("repo_upload")
        self.repo_choose_file = QtWidgets.QToolButton(self.page_repo)
        self.repo_choose_file.setGeometry(QtCore.QRect(50, 80, 26, 24))
        self.repo_choose_file.setObjectName("repo_choose_file")
        self.repo_label = QtWidgets.QLabel(self.page_repo)
        self.repo_label.setGeometry(QtCore.QRect(50, 20, 321, 41))
        self.repo_label.setObjectName("repo_label")
        self.repo_label.raise_()
        self.repo_upload.raise_()
        self.repo_choose_file.raise_()
        self.stackedWidget.addWidget(self.page_repo)
        self.page_domain = QtWidgets.QWidget()
        self.page_domain.setObjectName("page_domain")
        self.formLayoutWidget = QtWidgets.QWidget(self.page_domain)
        self.formLayoutWidget.setGeometry(QtCore.QRect(20, 20, 501, 301))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setHorizontalSpacing(15)
        self.formLayout.setVerticalSpacing(20)
        self.formLayout.setObjectName("formLayout")
        self.inpl_comp_name = QtWidgets.QLabel(self.formLayoutWidget)
        self.inpl_comp_name.setObjectName("inpl_comp_name")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.inpl_comp_name)
        self.inp_comp_name = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.inp_comp_name.setObjectName("inp_comp_name")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.inp_comp_name)
        self.inpl_dn = QtWidgets.QLabel(self.formLayoutWidget)
        self.inpl_dn.setObjectName("inpl_dn")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.inpl_dn)
        self.inp_dn = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.inp_dn.setObjectName("inp_dn")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.inp_dn)
        self.inpl_dip = QtWidgets.QLabel(self.formLayoutWidget)
        self.inpl_dip.setObjectName("inpl_dip")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.inpl_dip)
        self.inp_dip = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.inp_dip.setObjectName("inp_dip")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.inp_dip)
        self.inpl_admn = QtWidgets.QLabel(self.formLayoutWidget)
        self.inpl_admn.setObjectName("inpl_admn")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.inpl_admn)
        self.inp_admn = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.inp_admn.setObjectName("inp_admn")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.inp_admn)
        self.inpl_admp = QtWidgets.QLabel(self.formLayoutWidget)
        self.inpl_admp.setObjectName("inpl_admp")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.inpl_admp)
        self.inp_admp = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.inp_admp.setObjectName("inp_admp")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.inp_admp)
        self.save_domain = QtWidgets.QPushButton(self.formLayoutWidget)
        self.save_domain.setObjectName("save_domain")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.save_domain)
        self.inp_admp.raise_()
        self.inp_admn.raise_()
        self.inpl_dip.raise_()
        self.inp_dip.raise_()
        self.inpl_dn.raise_()
        self.inpl_admn.raise_()
        self.inp_dn.raise_()
        self.inp_comp_name.raise_()
        self.inpl_admp.raise_()
        self.inpl_comp_name.raise_()
        self.save_domain.raise_()
        self.stackedWidget.addWidget(self.page_domain)
        self.page_theme = QtWidgets.QWidget()
        self.page_theme.setObjectName("page_theme")
        self.theme_label = QtWidgets.QLabel(self.page_theme)
        self.theme_label.setGeometry(QtCore.QRect(140, 180, 201, 41))
        self.theme_label.setObjectName("theme_label")
        self.theme_btn = QtWidgets.QPushButton(self.page_theme)
        self.theme_btn.setGeometry(QtCore.QRect(330, 180, 121, 41))
        self.theme_btn.setObjectName("theme_btn")
        self.stackedWidget.addWidget(self.page_theme)
        self.page_conf = QtWidgets.QWidget()
        self.page_conf.setObjectName("page_conf")
        self.formLayoutWidget_4 = QtWidgets.QWidget(self.page_conf)
        self.formLayoutWidget_4.setGeometry(QtCore.QRect(40, 150, 441, 80))
        self.formLayoutWidget_4.setObjectName("formLayoutWidget_4")
        self.formLayout_4 = QtWidgets.QFormLayout(self.formLayoutWidget_4)
        self.formLayout_4.setContentsMargins(0, 0, 0, 0)
        self.formLayout_4.setObjectName("formLayout_4")
        self.send_report = QtWidgets.QLabel(self.formLayoutWidget_4)
        self.send_report.setObjectName("send_report")
        self.formLayout_4.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.send_report)
        self.send_auto = QtWidgets.QRadioButton(self.formLayoutWidget_4)
        self.send_auto.setObjectName("send_auto")
        self.formLayout_4.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.send_auto)
        self.send_not = QtWidgets.QRadioButton(self.formLayoutWidget_4)
        self.send_not.setObjectName("send_not")
        self.formLayout_4.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.send_not)
        self.send_not.raise_()
        self.send_auto.raise_()
        self.send_report.raise_()
        self.check_geo = QtWidgets.QCheckBox(self.page_conf)
        self.check_geo.setGeometry(QtCore.QRect(40, 70, 231, 23))
        self.check_geo.setObjectName("check_geo")
        self.stackedWidget.addWidget(self.page_conf)
        self.page_account = QtWidgets.QWidget()
        self.page_account.setObjectName("page_account")
        self.gnome_account = QtWidgets.QPushButton(self.page_account)
        self.gnome_account.setGeometry(QtCore.QRect(220, 210, 141, 51))
        self.gnome_account.setObjectName("gnome_account")
        self.account_label = QtWidgets.QLabel(self.page_account)
        self.account_label.setGeometry(QtCore.QRect(190, 140, 201, 71))
        self.account_label.setObjectName("account_label")
        self.stackedWidget.addWidget(self.page_account)
        self.page_user = QtWidgets.QWidget()
        self.page_user.setObjectName("page_user")
        self.user_label = QtWidgets.QLabel(self.page_user)
        self.user_label.setGeometry(QtCore.QRect(140, 70, 341, 71))
        self.user_label.setObjectName("user_label")
        self.gnome_user = QtWidgets.QPushButton(self.page_user)
        self.gnome_user.setGeometry(QtCore.QRect(220, 140, 141, 51))
        self.gnome_user.setObjectName("gnome_user")
        self.user_labelsp = QtWidgets.QLabel(self.page_user)
        self.user_labelsp.setGeometry(QtCore.QRect(150, 220, 281, 61))
        self.user_labelsp.setObjectName("user_labelsp")
        self.gnome_special = QtWidgets.QPushButton(self.page_user)
        self.gnome_special.setGeometry(QtCore.QRect(220, 290, 141, 51))
        self.gnome_special.setObjectName("gnome_special")
        self.stackedWidget.addWidget(self.page_user)
        self.page_info = QtWidgets.QWidget()
        self.page_info.setObjectName("page_info")
        self.purchase_title = QtWidgets.QLabel(self.page_info)
        self.purchase_title.setGeometry(QtCore.QRect(20, 0, 511, 41))
        self.purchase_title.setObjectName("purchase_title")
        self.purchase_email = QtWidgets.QLabel(self.page_info)
        self.purchase_email.setGeometry(QtCore.QRect(20, 40, 131, 21))
        self.purchase_email.setMouseTracking(True)
        self.purchase_email.setOpenExternalLinks(True)
        self.purchase_email.setTextInteractionFlags(QtCore.Qt.TextBrowserInteraction)
        self.purchase_email.setObjectName("purchase_email")
        self.partner_title = QtWidgets.QLabel(self.page_info)
        self.partner_title.setGeometry(QtCore.QRect(20, 70, 511, 41))
        self.partner_title.setObjectName("partner_title")
        self.partner_email = QtWidgets.QLabel(self.page_info)
        self.partner_email.setGeometry(QtCore.QRect(20, 110, 151, 21))
        self.partner_email.setOpenExternalLinks(True)
        self.partner_email.setObjectName("partner_email")
        self.suppoer_title = QtWidgets.QLabel(self.page_info)
        self.suppoer_title.setGeometry(QtCore.QRect(20, 140, 511, 41))
        self.suppoer_title.setObjectName("suppoer_title")
        self.title_email = QtWidgets.QLabel(self.page_info)
        self.title_email.setGeometry(QtCore.QRect(20, 180, 201, 21))
        self.title_email.setOpenExternalLinks(True)
        self.title_email.setObjectName("title_email")
        self.resource_link = QtWidgets.QLabel(self.page_info)
        self.resource_link.setGeometry(QtCore.QRect(20, 250, 421, 21))
        self.resource_link.setOpenExternalLinks(True)
        self.resource_link.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByKeyboard|QtCore.Qt.LinksAccessibleByMouse|QtCore.Qt.TextBrowserInteraction|QtCore.Qt.TextSelectableByKeyboard|QtCore.Qt.TextSelectableByMouse)
        self.resource_link.setObjectName("resource_link")
        self.resource_title = QtWidgets.QLabel(self.page_info)
        self.resource_title.setGeometry(QtCore.QRect(20, 210, 511, 41))
        self.resource_title.setObjectName("resource_title")
        self.phone_title = QtWidgets.QLabel(self.page_info)
        self.phone_title.setGeometry(QtCore.QRect(20, 290, 511, 41))
        self.phone_title.setObjectName("phone_title")
        self.stackedWidget.addWidget(self.page_info)
        self.autostart = QtWidgets.QRadioButton(self.centralwidget)
        self.autostart.setGeometry(QtCore.QRect(23, 555, 321, 23))
        self.autostart.setChecked(True)
        self.autostart.setAutoExclusive(False)
        self.autostart.setObjectName("autostart")
        self.menu = QtWidgets.QWidget(self.centralwidget)
        self.menu.setGeometry(QtCore.QRect(23, 130, 185, 415))
        self.menu.setObjectName("menu")
        self.top = QtWidgets.QWidget(self.centralwidget)
        self.top.setGeometry(QtCore.QRect(0, 0, 860, 20))
        self.top.setObjectName("top")
        self.top2 = QtWidgets.QWidget(self.centralwidget)
        self.top2.setGeometry(QtCore.QRect(0, 0, 860, 90))
        self.top2.setObjectName("top2")
        self.top2.raise_()
        self.menu.raise_()
        self.click_repo.raise_()
        self.click_domain.raise_()
        self.click_conf.raise_()
        self.click_theme.raise_()
        self.click_user.raise_()
        self.click_account.raise_()
        self.click_info.raise_()
        self.stackedWidget.raise_()
        self.autostart.raise_()
        self.top.raise_()
        self.redos_icon.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionNew = QtWidgets.QAction(MainWindow)
        self.actionNew.setObjectName("actionNew")
        self.actionOpen = QtWidgets.QAction(MainWindow)
        self.actionOpen.setObjectName("actionOpen")
        self.actionWrite = QtWidgets.QAction(MainWindow)
        self.actionWrite.setObjectName("actionWrite")

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(6)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.click_repo.setText(_translate("MainWindow", "Репозитории"))
        self.click_domain.setText(_translate("MainWindow", "Ввод в домен"))
        self.click_conf.setText(_translate("MainWindow", "Конфиденциальность"))
        self.click_theme.setText(_translate("MainWindow", "Тема"))
        self.click_user.setText(_translate("MainWindow", "Пользователь"))
        self.click_account.setText(_translate("MainWindow", "Учетные записи"))
        self.click_info.setText(_translate("MainWindow", "О РедОС"))
        self.home_label.setText(_translate("MainWindow", "Welcome!"))
        self.repo_upload.setText(_translate("MainWindow", "Загрузить"))
        self.repo_choose_file.setText(_translate("MainWindow", "..."))
        self.repo_label.setText(_translate("MainWindow", "Выбери сертификат и нажми на \"Загрузить\""))
        self.inpl_comp_name.setText(_translate("MainWindow", "Имя компьютера"))
        self.inpl_dn.setText(_translate("MainWindow", "Доменное имя"))
        self.inpl_dip.setText(_translate("MainWindow", "IP домена"))
        self.inpl_admn.setText(_translate("MainWindow", "Имя администратора домена"))
        self.inpl_admp.setText(_translate("MainWindow", "Пароль администратора"))
        self.save_domain.setText(_translate("MainWindow", "Сохранить"))
        self.theme_label.setText(_translate("MainWindow", "Нажми для выбора темы:"))
        self.theme_btn.setText(_translate("MainWindow", "Темы"))
        self.send_report.setText(_translate("MainWindow", "Отправлять отчеты: "))
        self.send_auto.setText(_translate("MainWindow", "Автоматически"))
        self.send_not.setText(_translate("MainWindow", "Не отправлять"))
        self.check_geo.setText(_translate("MainWindow", "Включить местоположение"))
        self.gnome_account.setText(_translate("MainWindow", "Начать"))
        self.account_label.setText(_translate("MainWindow", "Добавить онлайн аккаунты"))
        self.user_label.setText(_translate("MainWindow", "Задать имя пользователя и загрузить аватар"))
        self.gnome_user.setText(_translate("MainWindow", "Начать"))
        self.user_labelsp.setText(_translate("MainWindow", "Настроить специальные возможности"))
        self.gnome_special.setText(_translate("MainWindow", "Начать"))
        self.purchase_title.setText(_translate("MainWindow", "Приобретение РЕД ОС и коммерческое партнёрство"))
        self.purchase_email.setText(_translate("MainWindow", " redos@red-soft.ru"))
        self.partner_title.setText(_translate("MainWindow", "Технологическое партнёрство и обучение РЕД ОС"))
        self.partner_email.setText(_translate("MainWindow", "partner@red-soft.ru"))
        self.suppoer_title.setText(_translate("MainWindow", "Техническая поддержка"))
        self.title_email.setText(_translate("MainWindow", "redos.support@red-soft.ru"))
        self.resource_link.setText(_translate("MainWindow", "https://redos.red-soft.ru/informational-resources-red-soft/"))
        self.resource_title.setText(_translate("MainWindow", "Информационные ресурсы"))
        self.phone_title.setText(_translate("MainWindow", "Телефон  8 (800) 200-48-02"))
        self.autostart.setText(_translate("MainWindow", "Показывать окно при запуске системы"))
        self.actionNew.setText(_translate("MainWindow", "New"))
        self.actionNew.setStatusTip(_translate("MainWindow", "Create a new file"))
        self.actionOpen.setText(_translate("MainWindow", "Open"))
        self.actionOpen.setStatusTip(_translate("MainWindow", "Open a file"))
        self.actionWrite.setText(_translate("MainWindow", "Write"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
