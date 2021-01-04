import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

class ToolBox(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        btn = [QPushButton('B', self) for i in range(6)]
        for Btn in btn:
            Btn.resize(30, 30)
        self.resize(60, 90)
        k = 0
        for i in range(6):
            btn[i].move((i%2)*30, k*30)
            k += 1 if i % 2 == 1 else 0

class Asa(QWidget):
    def __init__(self):
        super(Asa,self).__init__()


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.resize(300, 200)
        self.statusBar().showMessage('Ready!')

        exitAction = QAction(QIcon('idea.png'), 'Exit', self)
        exitAction.setStatusTip('Exit application')
        exitAction.setShortcut('Ctrl+Q')
        exitAction.triggered.connect(self.yeni)

        menuBar = self.menuBar()
        fileMenu = menuBar.addMenu('File')
        fileMenu.addAction(exitAction)

        t = ToolBox()
        self.setCentralWidget(t)
    def yeni(self):
        a = Asa()
        self.setCentralWidget(a)



if __name__ == '__main__':
    app = QApplication(sys.argv)
    m = MainWindow()
    m.show()
    sys.exit(app.exec_())