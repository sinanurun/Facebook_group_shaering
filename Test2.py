from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow1(object):

    def exIpDomInv_clicked(self):
        print("You clicked a button...")

    def setup(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(412, 440)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")

        self.exIpDomInv = QtWidgets.QPushButton(self.centralwidget)
        self.exIpDomInv.setObjectName("exIpDomInv")
        self.verticalLayout.addWidget(self.exIpDomInv)

        MainWindow.setCentralWidget(self.centralwidget)
        self.Menu = QtWidgets.QMenuBar(MainWindow)
        self.Menu.setGeometry(QtCore.QRect(0, 0, 412, 31))
        self.Menu.setObjectName("Menu")

        MainWindow.setMenuBar(self.Menu)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")

        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.exIpDomInv.clicked.connect(self.exIpDomInv_clicked)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Investigation"))
        MainWindow.setAccessibleName(_translate("MainWindow", "InvestigationMenu"))
        self.exIpDomInv.setText(_translate("MainWindow", "External IP/ Domain Investigation"))


# if __name__ == "__main__":
#     import sys
#
#     app = QtWidgets.QApplication(sys.argv)
#     MainWindow1 = QtWidgets.QMainWindow()
#     ui2 = Ui_MainWindow1()
#     ui2.setup(MainWindow1)
#     MainWindow1.show()
#     sys.exit(app.exec_())