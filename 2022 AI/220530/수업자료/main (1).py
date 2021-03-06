import sys
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication, QMainWindow, QAction, qApp

# QtCore 모듈의 QCoreApplication 클래스 가져 오기
from PyQt5.QtCore import QCoreApplication


class MyApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):

        # 아이콘 추가
        self.setWindowIcon(QIcon("./web.png"))

        # 프레임 만들기
        # setWindowTitle -> 타이틀바에 나타는 창의 제목
        self.setWindowTitle("My First Application !!")
        self.move(300, 300)
        self.resize(400, 200)

        # 메뉴바 만들기
        exitAction = QAction('&Exit', self)
        # 단축키
        exitAction.setShortcut('Ctrl+Q')
        exitAction.setStatusTip("Exit application")
        exitAction.triggered.connect(qApp.quit)

        menuber = self.menuBar()
        fileMenu = menuber.addMenu('&File')
        fileMenu.addAction(exitAction)

        self.show()


if __name__ == "__main__":
    # 모든 PyQt5 어플리케이션은 어플리케이션 객체 생성
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())
