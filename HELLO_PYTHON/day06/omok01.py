import sys

from PyQt5 import uic, QtGui, QtCore
from PyQt5.Qt import QMainWindow, QIcon, QApplication
from PyQt5.QtWidgets import QPushButton



#UI파일 연결
#단, UI파일은 Python 코드 파일과 같은 디렉토리에 위치해야한다.
form_class = uic.loadUiType("omok01.ui")[0]

#화면을 띄우는데 사용되는 Class 선언
class WindowClass(QMainWindow, form_class) :
    
    def __init__(self) :
        super().__init__()
        self.setupUi(self)  
        self.flagWb = False #전역변수 self안쓰면 local global로 할수도 있지만 
        rMyIcon = QtGui.QPixmap("0.png");
        self.pb.clicked.connect(self.reset)
        for j in range(10):
            for i in range(10):
                self.btn = QPushButton("",self)
                self.btn.setIcon(QtGui.QIcon(rMyIcon))
                self.btn.setGeometry(i*40,j*40,40,40);
                self.btn.setIconSize(QtCore.QSize(40,40))     
                self.btn.clicked.connect(self.myClick)
        
                
        
        
    def myClick(self):
        if self.flagWb:
            self.sender().setIcon(QtGui.QIcon("1.png"))
        else:
            self.sender().setIcon(QtGui.QIcon("2.png"))
        self.flagWb = not self.flagWb
    def reset(self):
        print("rest")
        self.btn.setIcon(QtGui.QIcon("0.png"))
        
if __name__ == "__main__" :
    app = QApplication(sys.argv) 
    myWindow = WindowClass() 
    myWindow.show()
    app.exec_()