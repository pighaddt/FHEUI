#!/usr/bin/python

import sys
from PyQt5.QtGui import QPixmap, QIcon, QMovie
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QDialog
from PyQt5.QtWidgets import QFileDialog
from PyQt5.QtWidgets import (QWidget, QLabel, QHBoxLayout,QVBoxLayout,
                             QComboBox, QApplication,QListWidgetItem,QGroupBox,QComboBox,QLabel,QLineEdit,QGridLayout,QMenuBar,QMenu,QStatusBar,
                             QTextEdit,QDialog,QFrame,QProgressBar, QToolTip,QPushButton)
                             

class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):

        

        self.gridGroupBox = QGroupBox("訊號處理與補償參數設定",self)
        layout = QGridLayout()

        
        self.manLabel = QLabel("導線拉伸條件",self)
        self.manLabel.resize(50,250)
        self.combo001 = QComboBox(self)
        self.combo001.addItem('0%')
        self.combo001.addItem('5%')
        self.combo001.addItem('10%')
        self.combo001.addItem('15%')
        self.combo001.resize(50,400)


        self.hightLabel = QLabel("電極距離(cm)",self)

        self.combo002 = QComboBox(self)
        self.combo002.addItem('1.0')
        self.combo002.addItem('2.0')
        self.combo002.addItem('3.0')

        self.strainLabel = QLabel("電極偏移(%)",self)
        self.combo003 = QComboBox(self)     
        
        self.combo003.addItem('0%')
        self.combo003.addItem('5%')
        self.combo003.addItem('10%')
        self.combo003.addItem('15%')

#        self.combo003.activated[str].connect(self.onActivated)

        layout.setSpacing(20) 
        layout.addWidget(self.manLabel,1,0)
        layout.addWidget(self.combo001,1,1)
        
        layout.addWidget(self.hightLabel,2,0)
        layout.addWidget(self.combo002,2,1)

        layout.addWidget(self.strainLabel,3,0)
#        layout.addWidget(self.emitLineEdit,2,1)
        layout.addWidget(self.combo003,3,1)


        self.noLabel1 = QLabel("訊號源頻率(Hz)",self)
        self.noLineEdit1 = QLineEdit(" ",self)
        self.caseLabel1 = QLabel("振幅(V)",self)
        self.caseLineEdit1 = QLineEdit(" ",self)
        self.dateLabel1 = QLabel("偏移Offset(V)",self)
        self.dateLineEdit1 = QLineEdit("",self)

        self.waveLabel = QLabel("波形(Waveform)",self)
        self.combo004 = QComboBox(self)     
        
        self.combo004.addItem('弦波(Sine)')
        self.combo004.addItem('EMG波')
        self.combo004.addItem('ECG波')
        self.combo004.addItem('方波')
        
        layout.setSpacing(20) 
        layout.addWidget(self.noLabel1,4,0)
        layout.addWidget(self.noLineEdit1,4,1)
        layout.addWidget(self.caseLabel1,5,0)
        layout.addWidget(self.caseLineEdit1,5,1)
        layout.addWidget(self.dateLabel1,6,0)
        layout.addWidget(self.dateLineEdit1,6,1)
        
        layout.addWidget(self.waveLabel,7,0)
        layout.addWidget(self.combo004,7,1)
        

        
        self.pushButton_A01 = QPushButton()
###        self.pushButton_A01.setGeometry(QtCore.QRect(10, 30, 45, 35))
        self.pushButton_A01.setObjectName("pushButton_014")
        self.pushButton_A01.setStyleSheet("background-color: #1F1F1F; color: white;font: 100 10pt \"Arial Narrow\"")
        self.pushButton_A01.setText("存檔")
       # self.pushButton_014.setFont(QFont('Arial', 5))
     #   self.pushButton_A01.scaled(20,15, Qt.KeepAspectRatio, Qt.SmoothTransformation)
        self.pushButton_A01.setStyleSheet("QPushButton{color:white}"
                                  "QPushButton:hover{color:yellow}"
 ##                                 "QPushButton{border-image: url(/FHEUI/fig/max1.png)}"
 #                                 "QPushButton{background-image: url(/FHEUI/fig/max1.png)}"
                                  "QPushButton{background-color:#1E1E1E}"
 #                                 "QPushButton:hover{background-image:url(/FHEUI/fig/max2.png)}"
                                  "QPushButton{border:1px}"
                                  "QPushButton{border-radius:2px}"
                                  "QPushButton{font: 10pt} "
                                  "QPushButton{padding:2px 4px}") 
                                   

        self.pushButton_A01.clicked.connect(self.saveas001) 



        self.pushButton_A02 =QPushButton()
###        self.pushButton_A01.setGeometry(QtCore.QRect(10, 30, 45, 35))
        self.pushButton_A02.setObjectName("pushButton_014")
        self.pushButton_A02.setStyleSheet("background-color: #1F1F1F; color: white;font: 100 10pt \"Arial Narrow\"")
        self.pushButton_A02.setText("修改")
       # self.pushButton_014.setFont(QFont('Arial', 5))
     #   self.pushButton_A01.scaled(20,15, Qt.KeepAspectRatio, Qt.SmoothTransformation)
        self.pushButton_A02.setStyleSheet("QPushButton{color:white}"
                                  "QPushButton:hover{color:yellow}"
 ##                                 "QPushButton{border-image: url(/FHEUI/fig/max1.png)}"
 #                                 "QPushButton{background-image: url(/FHEUI/fig/max1.png)}"
                                  "QPushButton{background-color:#1E1E1E}"
  #                                "QPushButton:hover{background-image:url(/FHEUI/fig/max2.png)}"
                                  "QPushButton{border:1px}"
                                  "QPushButton{border-radius:2px}"
                                  "QPushButton{font: 10pt} "
                                  "QPushButton{padding:2px 4px}") 
                                   

        self.pushButton_A02.clicked.connect(self.modify001) 

        layout.addWidget(self.pushButton_A01,8,0)
        layout.addWidget(self.pushButton_A02,8,1)


        layout.setColumnStretch(1, 1)
        self.gridGroupBox.setLayout(layout)
        self.gridGroupBox.resize(400,450)


        self.setWindowTitle('訊號處理與補償參數設定')
        self.setWindowIcon(QIcon('fig\itrilogo.png'))
        self.setGeometry(900,200,400, 450)


        self.show()
    
    def modify001(self):
        
        self.noLineEdit1.clear()
        self.caseLineEdit1.setText(" ")
        self.dateLineEdit1.setText(" ")
    def saveas001(self,text):

        


        
       
        text001 = str(self.combo001.currentText())
        text002 = str(self.combo002.currentText())
        text003= str(self.combo003.currentText())
       
        text004 =str(self.noLineEdit1.text())
        text005 =str(self.caseLineEdit1.text())
        text006 =str(self.dateLineEdit1.text())    

        text007= str(self.combo004.currentText())


       # print(text001)
        filename, filetype = QFileDialog.getSaveFileName(self, "Save File", "*.sig")
        with open(filename,'w', encoding='utf-8-sig') as f:
            
            print(filename)
            f.write(text001 + '\n')
            f.write(text002 + '\n')
            f.write(text003 + '\n')
            f.write(text004 + '\n')
            f.write(text005 + '\n')
            f.write(text006 + '\n' )
            f.write(text007)
            f.close()

def main():
    
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()