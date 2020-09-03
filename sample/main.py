# -*- coding : utf-8 -*-

from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QToolTip, QMainWindow, QAction, qApp
from PyQt5.QtCore import QCoreApplication
from PyQt5.QtGui import QIcon, QFont

import sys

class Main(QMainWindow):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        """
            빈 줄을 통해 묶음을 구분 했습니다. 묶음끼리 주석을 해체하여 실행하면됩니다.
        :return:
        """
        # 첫번째 연습 - 창 띄우기 -> class Main(QWidget) 로 변경
        # self.setWindowTitle('My First Application')
        # self.move(300, 300)
        # self.resize(400, 200)
        # self.show()

        # 두번째 연습 - 아이콘 넣어보기 -> class Main(QWidget) 로 변경
        # self.setWindowTitle('Icon')
        # self.setWindowIcon(QIcon('./images/web.png'))
        # self.setGeometry(300,300,300,300)
        # self.show()

        # 세번째 연습 - 창 닫기 -> class Main(QWidget) 로 변경
        # btn = QPushButton('Quit', self)
        # btn.move(200, 200)
        # btn.resize(btn.sizeHint())
        # btn.clicked.connect(QCoreApplication.instance().quit)
        # self.setWindowTitle('Quit Button')
        # self.setGeometry(300, 300, 300, 250)
        # self.show()

        # 툴팁 나타내기 -> class Main(QWidget) 로 변경
        # QToolTip.setFont(QFont('SanSerif', 10))
        # self.setToolTip('This is a <b>QWidget</b> widget')
        # btn = QPushButton('Button', self)
        # btn.setToolTip('This is a <b>QPushButton</b> widget')
        # btn.move(50,50)
        # btn.resize(btn.sizeHint())
        # self.setWindowTitle('Tooltips')
        # self.setGeometry(300, 300, 300, 200)
        # self.show()

        # 상태바 만들기 -> class Main(QMainWindow) 로 변경
        # self.statusBar().showMessage('Ready')
        # self.setWindowTitle('StatusBar')
        # self.setGeometry(300, 300, 300, 200)
        # self.show()

        # 메뉴바 만들기 -> class Main(QMainWindow) 로 변경
        exitAction = QAction(QIcon('./images/exit.png'), 'Exit', self)
        exitAction.setShortcut('Ctrl+Q')
        exitAction.setStatusTip('Exit applicaton')
        exitAction.triggered.connect(qApp.quit)
        self.statusBar()
        menubar = self.menuBar()
        menubar.setNativeMenuBar(False)
        filemenu = menubar.addMenu('&File')
        filemenu.addAction(exitAction)
        self.setWindowTitle('Menubar')
        self.setGeometry(300, 300, 300, 200)
        self.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = Main()
    sys.exit(app.exec_())