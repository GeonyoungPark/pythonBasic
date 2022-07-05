import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
import random
from _cffi_backend import typeof
#UI파일 연결
#단, UI파일은 Python 코드 파일과 같은 디렉토리에 위치해야한다.
form_class = uic.loadUiType("myqt06.ui")[0]

#화면을 띄우는데 사용되는 Class 선언

class WindowClass(QMainWindow, form_class) :
    def __init__(self) :
        super().__init__()
        self.setupUi(self)
        self.pb.clicked.connect(self.btn1Function)
    def btn1Function(self):
        arr = list(range(1,46))
        random.shuffle(arr)
        self.lbl1.setText(str(arr[0]))
        self.lbl2.setText(str(arr[1]))
        self.lbl3.setText(str(arr[2]))
        self.lbl4.setText(str(arr[3]))
        self.lbl5.setText(str(arr[4]))
        self.lbl6.setText(str(arr[5]))
if __name__ == "__main__" :
    #QApplication : 프로그램을 실행시켜주는 클래스
    app = QApplication(sys.argv) 

    #WindowClass의 인스턴스 생성
    myWindow = WindowClass() 

    #프로그램 화면을 보여주는 코드
    myWindow.show()

    #프로그램을 이벤트루프로 진입시키는(프로그램을 작동시키는) 코드
    app.exec_()