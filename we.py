import sys
from selenium import webdriver
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

class mainwindow(QMainWindow):
    def __init__(self, parent = None):
        super(mainwindow, self).__init__(parent = parent)
        self.title = 'SUDOKU SOLVER'

        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        # add menubar
        menubar = self.menuBar()

        # add drop down items
        exitAct = QAction('&Exit', self)
        exitAct.setShortcut('Ctrl+Q')
        exitAct.setStatusTip('Exit Application')
        exitAct.triggered.connect(qApp.quit)

        newAct = QAction('New', self)
        newAct.setShortcut('Ctrl+N')
        newAct.setStatusTip('New Sudoku')
        newAct.triggered.connect(GameLogic.clearFields)

        rulesAct = QAction('Rules', self)
        rulesAct.setShortcut('Ctrl+R')
        rulesAct.setStatusTip('Sudoku Rules')
        rulesAct.triggered.connect(GameLogic.sudokuRules)

        # add menubar entries
        fileMenu = menubar.addMenu('&File')
        fileMenu.addAction(newAct)
        fileMenu.addAction(exitAct)

        helpMenu = menubar.addMenu('&Help')
        helpMenu.addAction(rulesAct)

        # call gridlayout function
        l = self.gridLayout()
        self.setCentralWidget(l)

        self.show()

    def gridLayout(self):
        layout = QGridLayout()
        solve = QPushButton('Solve', self)
        solve.clicked.connect(GameLogic.solveSudoku)
        solve.setFixedSize(60, 30)

        mainwindow.fields = {}

        # validate user input
        onlyInt = QIntValidator(1, 9, self)

        # this is the part that doesnt work...
        for x in range(9):
            for y in range(9):
                # keep a reference to the buttons
                mainwindow.fields[(x, y)] = QLineEdit(self)
                mainwindow.fields[(x, y)].setMaxLength(1)
                mainwindow.fields[(x, y)].setValidator(onlyInt)
                mainwindow.fields[(x, y)].setFixedSize(60, 60)
                mainwindow.fields[(x, y)].setFont(QFont('Sans Serif', 20))
                mainwindow.fields[(x, y)].setAlignment(Qt.AlignCenter)
                # add to the layout
                layout.addWidget(mainwindow.fields[(x, y)], x, y)

        layout.addWidget(solve, 10, 4)
        w = QWidget()
        w.setLayout(layout)
        return(w)

class GameLogic():

    def clearFields(self):
        for i in range(9):
            for j in range(9):
                mainwindow.fields[(i, j)].clear()

    def sudokuRules(self):
        pass

    def solveSudoku(self):
        pass

def main():
    app = QApplication(sys.argv)
    ex = mainwindow()

    sys.exit(app.exec_())

if __name__ == '__main__':
    main()