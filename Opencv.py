import sys
from PyQt5.QtWidgets import QMainWindow, QPushButton, QApplication
import cv2
import numpy as np



class Example(QMainWindow):
    
    def __init__(self):
        super().__init__()
        
        self.initUI()
        
        
    def initUI(self):      

        btn1 = QPushButton("Averaging", self)
        btn1.move(30, 50)

        btn2 = QPushButton("Gaussian", self)
        btn2.move(150, 50)
        
        btn3 = QPushButton("Median", self)
        btn3.move(150, 100)
        
        btn4 = QPushButton("Bilateral", self)
        btn4.move(30, 100)
        
        btn5 = QPushButton("orjinal", self)
        btn5.move(90, 10)
      
        btn1.clicked.connect(self.buttonClicked)            
        btn2.clicked.connect(self.button2Clicked)
        btn3.clicked.connect(self.button3Clicked)
        btn4.clicked.connect(self.button4Clicked)
        btn5.clicked.connect(self.button5Clicked)
     
        self.statusBar()
        
        self.setGeometry(300, 300, 290, 150)
        self.setWindowTitle('boxx')
        self.show()
        
        
    def buttonClicked(self):
      
        sender = self.sender()
        self.statusBar().showMessage(sender.text() + ' was pressed')
        cv2.namedWindow('image')
        img = cv2.imread('lenna3.jpg')
        box=cv2.boxFilter(img,-1,(21,21))
        cv2.imshow('image',box)
        
    def button5Clicked(self):
      
        sender = self.sender()
        self.statusBar().showMessage(sender.text() + ' was pressed')
        cv2.namedWindow('image')
        img = cv2.imread('lenna3.jpg')
        box=cv2.boxFilter(img,-1,(21,21))
        cv2.imshow('image',box)
        
        blur=cv2.blur(img,(5,5))
        cv2.imshow('image',blur)
        
    def button2Clicked(self):
      
        sender = self.sender()
        self.statusBar().showMessage(sender.text() + ' was pressed')
        cv2.namedWindow('image')
        img = cv2.imread('lenna3.jpg')
        blur = cv2.GaussianBlur(img,(25,25),0)
        cv2.imshow('image',blur)
        
    def button3Clicked(self):
      
        sender = self.sender()
        self.statusBar().showMessage(sender.text() + ' was pressed')
        cv2.namedWindow('image')
        img = cv2.imread('lenna3.jpg')
        median = cv2.medianBlur(img,5)
        cv2.imshow('image',median)
        
               
    def button4Clicked(self):
      
        sender = self.sender()
        self.statusBar().showMessage(sender.text() + ' was pressed')
        cv2.namedWindow('image')
        img = cv2.imread('lenna3.jpg')
        blur = cv2.bilateralFilter(img,9,75,75)
        cv2.imshow('image',blur)
   
                
if __name__ == '__main__':
    
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
