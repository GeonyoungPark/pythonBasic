import sys

from PyQt5 import uic, QtGui, QtCore, QtWidgets
from PyQt5.Qt import QMainWindow, QIcon, QApplication
from PyQt5.QtWidgets import QPushButton
from networkx.generators import line


#UI파일 연결
#단, UI파일은 Python 코드 파일과 같은 디렉토리에 위치해야한다.
form_class = uic.loadUiType("omok02.ui")[0]

#화면을 띄우는데 사용되는 Class 선언
class WindowClass(QMainWindow, form_class) :
    
    def __init__(self) :
        super().__init__()
        self.setupUi(self)  
        self.flagWb = True
        self.flagIng = True
        self.arr2D = [
            [0,0,0,0,0, 0,0,0,0,0],
            [0,0,0,0,0, 0,0,0,0,0],
            [0,0,0,0,0, 0,0,0,0,0],
            [0,0,0,0,0, 0,0,0,0,0],
            [0,0,0,0,0, 0,0,0,0,0],
            
            [0,0,0,0,0, 0,0,0,0,0],
            [0,0,0,0,0, 0,0,0,0,0],
            [0,0,0,0,0, 0,0,0,0,0],
            [0,0,0,0,0, 0,0,0,0,0],
            [0,0,0,0,0, 0,0,0,0,0]
           
            
        ]
        self.pb2D = []
        for i in range(10):
            line = []
            for j in range(10):
                btn = QPushButton("",self)
                btn.setIcon(QtGui.QIcon("0.png"))
                btn.setGeometry(j*40,i*40,40,40);
                btn.setIconSize(QtCore.QSize(40,40))
                btn.setToolTip("{},{}".format(i,j))
                btn.clicked.connect(self.myClick)
                line.append(btn)
            self.pb2D.append(line)
                
        self.myRender()
        self.pbReset.clicked.connect(self.reset)

    def myRender(self):
        for i in range(10):
            for j in range(10):
                if self.arr2D[i][j] == 0:
                    self.pb2D[i][j].setIcon(QtGui.QIcon("0.png"))     
                if self.arr2D[i][j] == 1:
                    self.pb2D[i][j].setIcon(QtGui.QIcon("1.png"))     
                if self.arr2D[i][j] == 2:
                    self.pb2D[i][j].setIcon(QtGui.QIcon("2.png"))     
    def myClick(self):
        if not self.flagIng :
            return
        str_ij = self.sender().toolTip()
        print(str_ij)
        arr_ij = str_ij.split(",")
        print(arr_ij)
        i = int(arr_ij[0])
        j = int(arr_ij[1])
        print(i,j)
        if self.arr2D[i][j] > 0:
            return
        stone = -1
        if self.flagWb :
            self.arr2D[i][j] = 1
            stone = 1
        else :
            self.arr2D[i][j] = 2
            stone = 2
        
        up = self.checkUp(i,j,stone)
        print("up",up)
        
        dw = self.checkDw(i,j,stone)
        print("dw",dw)
        
        rt = self.checkRt(i,j,stone)
        print("rt",rt)
        
        lt = self.checkLt(i,j,stone)
        print("lt",lt)
        
        ur = self.checkUr(i,j,stone)
        print("ur",ur)
        
        ul = self.checkUl(i,j,stone)
        print("ul",ul)
        
        dr = self.checkDr(i,j,stone)
        print("dr",dr)
        
        dl = self.checkDl(i,j,stone)
        print("dl",dl)
        
        d1 = up + dw + 1
        d2 = ur + dl + 1
        d3 = lt + rt + 1
        d4 = ul + dr + 1
        self.myRender()
        self.flagWb = not self.flagWb
        
        if d1 == 5 or d2 == 5 or d3 == 5 or d4 == 5 :
            self.flagIng = False
            if self.flagWb :
                QtWidgets.QMessageBox.information(self, "Game Over","Black win")
            else :
                QtWidgets.QMessageBox.information(self, "Game Over","White win")
        
    def reset(self):
        for i in range(10):
            for j in range(10):
                self.arr2D[i][j] = 0
        self.myRender()
        self.flagWb = True
        self.flagIng = True
            
    def checkUp(self,i,j,stone):
        cnt = 0
        try:
            while True:
                i -= 1
                if i < 0 : 
                    return cnt
                if j < 0 : 
                    return cnt
                if self.arr2D[i][j] == stone :
                    cnt += 1
                else:
                    return cnt
        except:
            return cnt   
    def checkDw(self,i,j,stone):
        cnt = 0
        try:
            while True:
                i += 1
                if i < 0 : 
                    return cnt
                if j < 0 : 
                    return cnt
                if self.arr2D[i][j] == stone :
                    cnt += 1
                else:
                    return cnt
        except:
            return cnt
        
    def checkRt(self,i,j,stone):
        cnt = 0
        try:
            while True:
                j += 1
                if i < 0 : 
                    return cnt
                if j < 0 : 
                    return cnt
                if self.arr2D[i][j] == stone :
                    cnt += 1
                else:
                    return cnt
        except:
            return cnt
    
    def checkLt(self,i,j,stone):
        cnt = 0
        try:
            while True:
                j -= 1
                if i < 0 : 
                    return cnt
                if j < 0 : 
                    return cnt
                if self.arr2D[i][j] == stone :
                    cnt += 1
                else:
                    return cnt
        except:
            return cnt
    
    def checkUr(self,i,j,stone):
        cnt = 0
        try:
            while True:
                i -= 1
                j += 1
                if i < 0 : 
                    return cnt
                if j < 0 : 
                    return cnt
                if self.arr2D[i][j] == stone :
                    cnt += 1
                else:
                    return cnt
        except:
            return cnt
    
    def checkUl(self,i,j,stone):
        cnt = 0
        try:
            while True:
                i -= 1
                j -= 1
                if i < 0 : 
                    return cnt
                if j < 0 : 
                    return cnt
                if self.arr2D[i][j] == stone :
                    cnt += 1
                else:
                    return cnt
        except:
            return cnt
    
    def checkDr(self,i,j,stone):
        cnt = 0
        try:
            while True:
                i += 1
                j += 1
                if i < 0 : 
                    return cnt
                if j < 0 : 
                    return cnt
                if self.arr2D[i][j] == stone :
                    cnt += 1
                else:
                    return cnt
        except:
            return cnt
    
    def checkDl(self,i,j,stone):
        cnt = 0
        try:
            while True:
                i += 1
                j -= 1
                if i < 0 : 
                    return cnt
                if j < 0 : 
                    return cnt
                if self.arr2D[i][j] == stone :
                    cnt += 1
                else:
                    return cnt
        except:
            return cnt
    
if __name__ == "__main__" :
    app = QApplication(sys.argv) 
    myWindow = WindowClass() 
    myWindow.show()
    app.exec_()
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    