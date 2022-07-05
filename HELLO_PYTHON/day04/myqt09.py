import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
from PyQt5 import QtCore, QtWidgets

#UI파일 연결
#단, UI파일은 Python 코드 파일과 같은 디렉토리에 위치해야한다.
form_class = uic.loadUiType("myqt09.ui")[0]

#화면을 띄우는데 사용되는 Class 선언
class WindowClass(QMainWindow, form_class) :
    def __init__(self) :
        super().__init__()
        self.setupUi(self)
        self.pb_call.clicked.connect(self.btnCallFunction)
        self.pb1.clicked.connect(self.btn1Function)
        self.pb2.clicked.connect(self.btn2Function)
        self.pb3.clicked.connect(self.btn3Function)
        self.pb4.clicked.connect(self.btn4Function)
        self.pb5.clicked.connect(self.btn5Function)
        self.pb6.clicked.connect(self.btn6Function)
        self.pb7.clicked.connect(self.btn7Function)
        self.pb8.clicked.connect(self.btn8Function)
        self.pb9.clicked.connect(self.btn9Function)
        self.pb0.clicked.connect(self.btn0Function)
    def btnCallFunction(self):
        QtWidgets.QMessageBox.information(self, "Calling",self.le.text())
        self.sender().text()
    def btn1Function(self):
        self.le.insert("1")
    def btn2Function(self):
        self.le.insert("2")
    def btn3Function(self):
        self.le.insert("3")
    def btn4Function(self):
        self.le.insert("4")
    def btn5Function(self):
        self.le.insert("5")
    def btn6Function(self):
        self.le.insert("6")
    def btn7Function(self):
        self.le.insert("7")
    def btn8Function(self):
        self.le.insert("8")
    def btn9Function(self):
        self.le.insert("9")
    def btn0Function(self):
        self.le.insert("0")



if __name__ == "__main__" :
    #QApplication : 프로그램을 실행시켜주는 클래스
    app = QApplication(sys.argv) 

    #WindowClass의 인스턴스 생성
    myWindow = WindowClass() 

    #프로그램 화면을 보여주는 코드
    myWindow.show()

    #프로그램을 이벤트루프로 진입시키는(프로그램을 작동시키는) 코드
    app.exec_()