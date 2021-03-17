import sys
import csv
import pyqtgraph as pg
from pyqtgraph import PlotWidget, plot
# import cv2
import string, os 
import subprocess
from PyQt5 import *
from PyQt5.QtGui import QPixmap, QIcon, QMovie
from PyQt5.QtWidgets import QApplication, QWidget, QListWidget, QHBoxLayout,QListWidgetItem,QGroupBox

from PyQt5.QtWidgets import    QFormLayout
from PyQt5.QtWidgets import QDockWidget

from PyQt5.QtWidgets import (QMessageBox,QApplication, QWidget, QPushButton,
                             QDesktopWidget, QMainWindow, QAction, qApp, QToolBar, QVBoxLayout,
                             QComboBox,QLabel,QLineEdit,QGridLayout,QMenuBar,QMenu,QStatusBar,
                             QTextEdit,QDialog,QFrame,QProgressBar, QToolTip
                             )
from PyQt5 import QtCore, QtWidgets, QtGui
from PyQt5.QtGui import QFont,QPalette 
from PyQt5.QtCore import QCoreApplication, Qt,QBasicTimer, QPoint
from PyQt5.QtWidgets import QFontComboBox 


from PyQt5.QtGui import QPainter
from PyQt5.QtGui import QImage, QBrush, QCloseEvent
from PyQt5.QtGui import  QColor
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import * 
import matplotlib
matplotlib.use('Qt5Agg')

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtWebEngineWidgets import *
import pandas as pd
import plotly.graph_objects as go


from PyQt5.QtGui import QPixmap, QIcon, QMovie,QPainter
from PyQt5.QtGui import QImage, QPalette, QBrush, QCloseEvent

from PyQt5.QtCore import QThread, pyqtSignal
from PyQt5.QtCore import QCoreApplication, QSize

from PyQt5.QtWidgets import QMdiArea, QMdiSubWindow 
from PyQt5.QtWidgets import QMainWindow, QTextEdit, QAction
from PyQt5.QtWidgets import QWidget, QApplication, QLabel, QPushButton,QLineEdit
from PyQt5.QtWidgets import QToolTip
# from PyQt5.QtWidgets import *
from PyQt5.QtWidgets import QApplication, QWidget, QMessageBox
from PyQt5.QtWidgets import QDesktopWidget 
from PyQt5.QtWidgets import QDialog
from PyQt5.QtWidgets import QFileDialog
from PyQt5.QtCore import Qt
from PyQt5 import QtMultimedia, QtMultimediaWidgets


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QDir, Qt, QUrl
from PyQt5.QtGui import QMovie
from PyQt5.QtMultimedia import QMediaContent, QMediaPlayer
from PyQt5.QtMultimediaWidgets import QVideoWidget
from PyQt5.QtWidgets import (QApplication, QFileDialog, QLabel,
        QPushButton, QSizePolicy, QSlider, QStyle, QWidget)
from PyQt5.QtWidgets import QMainWindow,QWidget, QPushButton, QAction, QListView
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QAction, QTableWidget,QTableWidgetItem

from PyQt5.QtCore import QStringListModel
from PyQt5.QtGui import QKeySequence
import time


class BackendThread(QObject):

    update_date = pyqtSignal(str)
    def run(self):
        while True:
            data001 = QDateTime.currentDateTime()
            currTime = data001.toString("yyyy-MM-dd hh:mm:ss")
            self.update_date.emit(str(currTime))
            time.sleep(1)



class TableModel(QtCore.QAbstractTableModel):
    def __init__(self, data):
        super(TableModel, self).__init__()
        self._data = data
       # print(data)

    def data(self, index, role):
        if role == Qt.DisplayRole:
        # Get the raw value
            value = self._data[index.row()][index.column()]

        # Perform per-type checks and render accordingly.
           # if isinstance(value, datetime):
                       # Render time to YYY-MM-DD.
               # return value.strftime("%Y-%m-%d")



            if isinstance(value, float):
            # Render float to 2 dp
                return "%.2f" % value

            if isinstance(value, str):
            # Render strings with quotes
                return '"%s"' % value

        # Default (anything not captured above: e.g. int)
            return value

        if role == Qt.TextAlignmentRole:
            value = self._data[index.row()][index.column()]

            if isinstance(value, int) or isinstance(value, float):
            # Align right, vertical middle.
               # return Qt.AlignVCenter + Qt.AlignRight

                return Qt.AlignVCenter + Qt.AlignCenter

    def rowCount(self, index):
        # The length of the outer list.
        return len(self._data)

    def columnCount(self, index):
        # The following takes the first sub-list, and returns
        # the length (only works if all rows are an equal length)
        return len(self._data[0])



class MplCanvas(FigureCanvasQTAgg):

    def __init__(self, parent=None, width=5, height=4, dpi=100):
        fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = fig.add_subplot(111)
        super(MplCanvas, self).__init__(fig)


class MdiSubWindow(QMdiSubWindow):
    def __init__(self):
        super(MdiSubWindow, self).__init__()
    def closeEvent(self, event):
        self.deleteLater()  #關閉後刪除


class Window(QtWidgets.QMainWindow):
    timeStamp = int(time.time())
        #轉換為其他日期格式,如:”%Y-%m-%d %H:%M:%S”
    timeArray = time.localtime(timeStamp)
    otherStyleTime = time.strftime('%Y-%m-%d %H:%M:%S', timeArray)

    print ('current_time',otherStyleTime)
        
    f = open('D:\\FHEUI\\FHE2021.log', 'a')
        #f.write("Try to use file.write()\nHail HYDRA")
        
    f.write("\n登入時間:  ")
    f.write(otherStyleTime)
    f.close()



    #TAB2
    choice = '智慧褲'
    choice_list = ['智慧護具', '智慧袖套', '智慧衣',]
    choice002 = '股四頭肌'
    choice_list002 = ['股二頭肌', '臀大肌',]
    choice003 = '銀膠'
    choice_list003 = ['織物', ]
    choice004 = '右腰'
    choice_list004 = ['左腰','右大腿前側','左大腿前側', ]

   ## skin control
    skinset= 'white'
   
   
    #TAB8
    paraf01 = '100'
    paraf01_list = ['1000', '10000', '100000',]
    paraf02 = '200'
    paraf02_list = ['2000', '20000', '200000',]


    def __init__(self, parent=None):
    ###   def __init__(self, *args, **kwargs):
        super(Window, self).__init__(parent)

    ###  super(Window, self).__init__(*args, **kwargs)

       # layout102 = QHBoxLayout()

        self.left = 5
        self.top  = 5
        self.width = 1360
        self.height = 700
        self.setGeometry(self.left, self.top, self.width, self.height) 
        
    

 ###  Dock FileList 例子  
        self.itemsFile = QDockWidget("aProject", self)
        self.itemsFile.setWindowTitle("專案管理")
        self.itemsFile.setGeometry(QtCore.QRect(300,50,500, 600))
        self.itemsFile.setMinimumSize(300, 250)

        self.LBLea16 = QLabel(self.itemsFile)
        FonC = "font-size: 12pt; font: bold;font-family:微軟正黑體 ;text-decoration: underline;"
        self.LBLea16.setText("")
        self.LBLea16.setStyleSheet(FonC)
        self.LBLea16.setGeometry(660,30,600,50) 

        self.pushButton_L014 = QtWidgets.QPushButton(self.itemsFile)
        self.pushButton_L014.setGeometry(QtCore.QRect(10, 30, 45, 35))
        self.pushButton_L014.setObjectName("pushButton_014")
        self.pushButton_L014.setStyleSheet("background-color: #1F1F1F; color: white;font: 100 10pt \"Arial Narrow\"")
        self.pushButton_L014.setText("")
       # self.pushButton_014.setFont(QFont('Arial', 5))
     #   self.pushButton_L014.scaled(20,15, Qt.KeepAspectRatio, Qt.SmoothTransformation)
        self.pushButton_L014.setStyleSheet("QPushButton{color:white}"
                                  "QPushButton:hover{color:blue}"
 ##                                 "QPushButton{border-image: url(/FHEUI/fig/max1.png)}"
                                  "QPushButton{background-image: url(/FHEUI/fig/max1.png)}"
                                  "QPushButton{background-color:#1E1E1E}"
                                  "QPushButton:hover{background-image:url(/FHEUI/fig/max2.png)}"
                                  "QPushButton{border:1px}"
                                  "QPushButton{border-radius:2px}"
                                  "QPushButton{font: 10pt} "
                                  "QPushButton{padding:2px 4px}") 
                                   

        self.pushButton_L014.clicked.connect(self.itemsFile.showMaximized) 


       
        self.layoutFile = QWidget(self.itemsFile)
        self.layoutFile.setGeometry(0, 65,1300, 600) 





        self.hlay = QHBoxLayout()
        self.treeview = QTreeView()
        self.listview = QListView()
        
        self.listview.setContextMenuPolicy(3)
        self.listview.customContextMenuRequested[QPoint].connect(self.listWidgetContext002)

        


        self.hlay.addWidget(self.treeview)
        self.hlay.addWidget(self.listview)

       # self.setGeometry(10,10,1150,600)

       # path = QDir.rootPath()
        path = "d:\\FHEUI\\Project"
        self.dirModel = QFileSystemModel()
        #self.dirModel.setRootPath(QDir.rootPath())
        self.dirModel.setRootPath("d:\\FHEUI\\Project")
        self.dirModel.setFilter(QDir.NoDotAndDotDot | QDir.AllDirs)
        self.fileModel = QFileSystemModel()
        self.fileModel.setFilter(QDir.NoDotAndDotDot |  QDir.Files)
        
        self.treeview.setModel(self.dirModel)
        self.listview.setModel(self.fileModel)

        self.treeview.setRootIndex(self.dirModel.index(path))
        self.listview.setRootIndex(self.fileModel.index(path))
        self.treeview.clicked.connect(self.on_clicked)
    
        self.listview.clicked.connect(self.on_clicked003)
        self.addDockWidget(Qt.RightDockWidgetArea, self.itemsFile)
    #    self.itemsFile.setFloating(False)
        self.layoutFile.setLayout(self.hlay)

        self.itemsFile.close()

        
       
###### menubar

        menuBar = self.menuBar()
        #添加一個菜單項，在菜單項下課添加子菜單項
        fileMenu = menuBar.addMenu('檔案')
        menuBar.setFont(QFont('Arial', 12))

        #添加子功能表
        aAdd = QAction('新增', self)
        aAdd.setIcon(QtGui.QIcon("d:\\FHEUI\\icon\\add.png"))
        aAdd.triggered.connect(self.close)
        fileMenu.addAction(aAdd) 
    
        fileMenu.addSeparator()
#        aOpen = QAction('開啟', self)
#        aOpen.triggered.connect(self.close)
#        fileMenu.addAction(aOpen) 

        menuNew = QtWidgets.QMenu('開啟',fileMenu)

        menuNew.setIcon(QtGui.QIcon("d:\\FHEUI\\icon\\open.png"))
        aOpen1 = QAction('開啟1', self)
        aOpen1.setIcon(QtGui.QIcon("d:\\FHEUI\\icon\\open.png"))
        menuNew.addAction(aOpen1)
        aOpen1.triggered.connect(self.close)

        aOpen2 = QAction('開啟2', self)
        aOpen2.setIcon(QtGui.QIcon("d:\\FHEUI\\icon\\open.png"))
        menuNew.addAction(aOpen2)
        aOpen2.triggered.connect(self.close)

        fileMenu.addAction(menuNew.menuAction())


        aSave = QAction('儲存', self)
        aSave.setIcon(QtGui.QIcon("d:\\FHEUI\\icon\\save.png"))
        aSave.triggered.connect(self.close)
        fileMenu.addAction(aSave)
        aSaveAs = QAction('另存新檔', self)
        aSaveAs.setIcon(QtGui.QIcon("d:\\FHEUI\\icon\\saveas.png"))
        aSaveAs.triggered.connect(self.close)
        fileMenu.addAction(aSaveAs)         


        fileMenu.addSeparator()
        aID = QAction('帳戶', self)
        aID.setIcon(QtGui.QIcon("d:\\FHEUI\\icon\\account.png"))
        aID.triggered.connect(self.close)
        fileMenu.addAction(aID) 
        fileMenu.addSeparator()
        
        aExit = QAction('離開', self)
        aExit.setIcon(QtGui.QIcon("d:\\FHEUI\\icon\\quit.png"))
       # aExit.triggered.connect(self.close)
        aExit.triggered.connect(self.CLOSE4)
        fileMenu.addAction(aExit) 
       
       
       
       

        self.setWindowTitle('   FY109 軟性混合電子加值技術與系統應用開發計畫  (FY109 FHE Design Platform)   ')
        self.setWindowIcon(QIcon('d:\\FHEUI\\fig\\itrilogo.png'))
#### menubar

        #標籤條形狀
        
        dataMenu = menuBar.addMenu('資料庫')

        aIntegration = QAction('FHE系統整合設計', self)
        aIntegration.setIcon(QtGui.QIcon("d:\\FHEUI\\fig\\hand2-circle-cropped.png"))
        aIntegration.triggered.connect(lambda:self.changeTabShape(0))
        
        aSignal = QAction('訊號處理與補償設計', self)
        aSignal.setIcon(QtGui.QIcon("d:\\FHEUI\\fig\\pcb3-circle-cropped.png"))
        aSignal.triggered.connect(lambda:self.changeTabShape(1))
        
        aTrace = QAction('可拉伸線路佈局設計', self)
        aTrace.setIcon(QtGui.QIcon("d:\\FHEUI\\fig\\trace1-circle-cropped.png"))
        #aTrace.triggered.connect(lambda:self.changeTabShape(1))
        aTrace.triggered.connect(self.stretchable)

        aImpact = QAction('防水與耐衝擊設計', self)
        aImpact.setIcon(QtGui.QIcon("d:\\FHEUI\\fig\\droptest-circle-cropped.png"))
        aImpact.triggered.connect(lambda:self.changeTabShape(1))    

        aMaterial = QAction('FHE特殊材料', self)
        aMaterial.setIcon(QtGui.QIcon("d:\\FHEUI\\fig\\material-circle-cropped.png"))
        aMaterial.triggered.connect(lambda:self.changeTabShape(1))   





        dataGroup = QActionGroup(self)
        dataGroup.addAction(aIntegration)
        dataGroup.addAction(aSignal)
        dataGroup.addAction(aTrace)
        dataGroup.addAction(aImpact)
        dataGroup.addAction(aMaterial)
        
        dataMenu.addAction(aIntegration)
        dataMenu.addAction(aSignal)
        dataMenu.addAction(aTrace)
        dataMenu.addAction(aImpact)
        dataMenu.addAction(aMaterial)






        #標籤條位置控制
        posMenu = menuBar.addMenu('設定管理')
        
        aNorth = QAction('Tab置上', self)
        aNorth.setIcon(QtGui.QIcon("d:\\FHEUI\\icon\\top.png"))
        aNorth.setCheckable(True)
#        aNorth.setChecked(True)
        aNorth.triggered.connect(lambda:self.changeTabPos(0))
        aSouth = QAction('Tab置下', self)
        aSouth.setIcon(QtGui.QIcon("d:\\FHEUI\\icon\\bottom.png"))
        aSouth.setCheckable(True)
        aSouth.triggered.connect(lambda:self.changeTabPos(1))
        aWest = QAction('Tab置左', self)
        aWest.setIcon(QtGui.QIcon("d:\\FHEUI\\icon\\left.png"))
        aWest.setCheckable(True)
        aWest.triggered.connect(lambda:self.changeTabPos(2))
        aEast = QAction('Tab置右', self)
        aEast.setIcon(QtGui.QIcon("d:\\FHEUI\\icon\\right.png"))
        aEast.setCheckable(True)
        aEast.triggered.connect(lambda:self.changeTabPos(3))

        
        aFrameless = QAction('Frameless', self)
#        aFrameless.setCheckable(True)
        aFrameless.triggered.connect(self.Frameless)

        aFrameshow = QAction('Frameshow', self)
#        aFrameshow.setCheckable(True)
        aFrameshow.triggered.connect(self.Frameshow)    


        aStatusbarshow = QAction('Status Bar ON', self)
#        aFrameshow.setCheckable(True)
        aStatusbarshow.triggered.connect(self.statuson)    

        aStatusbaroff = QAction('Status Bar OFF', self)
#        aFrameshow.setCheckable(True)
        aStatusbaroff.triggered.connect(self.statusoff)  

        aRounded = QAction('圓角矩形', self)
#        aRounded.setCheckable(True)
#        aRounded.setChecked(True)
        aRounded.triggered.connect(lambda:self.changeTabShape(0))
        
        aTriangular = QAction('三角形', self)
#        aTriangular.setCheckable(True)
#        aRounded.setChecked(True)
        aTriangular.triggered.connect(lambda:self.changeTabShape(1))



  

        ImgCallBack002 = QAction('應變-電阻-應力表', self)
        ImgCallBack002.setCheckable(True)
        ImgCallBack002.triggered.connect(self.ImgBack002)

        ImgCallBack003 = QAction('應變-電阻關係圖', self)
        ImgCallBack003.setCheckable(True)
        ImgCallBack003.triggered.connect(self.ImgBack003)       
        
        ImgCallBack001 = QAction('POC1應力分布圖', self)
        ImgCallBack001.setCheckable(True)
        ImgCallBack001.triggered.connect(self.ImgBack001) 
        
        
        posGroup = QActionGroup(self)
        posGroup.addAction(aNorth)
        posGroup.addAction(aSouth)
        posGroup.addAction(aWest)
        posGroup.addAction(aEast)
        
        posGroup.addAction(aFrameless)
        posGroup.addAction(aFrameshow)
        
        posGroup.addAction(aStatusbarshow)
        posGroup.addAction(aStatusbaroff)


        posGroup.addAction(aRounded)
        posGroup.addAction(aTriangular)

        
        posGroup.addAction(ImgCallBack002)
        posGroup.addAction(ImgCallBack003)        
        posGroup.addAction(ImgCallBack001)
        
        
        posMenu.addAction(aNorth)
        posMenu.addAction(aSouth)
        posMenu.addAction(aWest)
        posMenu.addAction(aEast)
        posMenu.addSeparator()
        posMenu.addAction(aFrameless)
        posMenu.addAction(aFrameshow)
        posMenu.addSeparator()
        posMenu.addAction(aStatusbarshow)
        posMenu.addAction(aStatusbaroff)
        posMenu.addSeparator()
        posMenu.addAction(aRounded)
        posMenu.addAction(aTriangular)
        posMenu.addSeparator()
        posMenu.addAction(ImgCallBack002)
        posMenu.addAction(ImgCallBack003)
        posMenu.addAction(ImgCallBack001)
        
        



####浮動視窗控制
        floatMenu = menuBar.addMenu('浮動視窗')

        
        projectList1 = QAction('專案管理', self)
        projectList1.triggered.connect(self.itemsFileshow)

        floatGroup = QActionGroup(self)
        floatGroup.addAction(projectList1)
        floatMenu.addAction(projectList1)

      
        projectList2 = QAction('測試編號', self)
        projectList2.triggered.connect(self.items001show)

        floatGroup = QActionGroup(self)
        floatGroup.addAction(projectList2)
        floatMenu.addAction(projectList2)

        projectList3 = QAction('設定檔', self)
        projectList3.triggered.connect(self.items102show)

        floatGroup = QActionGroup(self)
        floatGroup.addAction(projectList3)
        floatMenu.addAction(projectList3)








####################################
###   TAB1
####################################
  
     #   flags = QtCore.Qt.WindowFlags(QtCore.Qt.FramelessWindowHint | QtCore.Qt.WindowStaysOnTopHint)
      #  self.setWindowFlags(flags)
        self.oldPos = self.pos()

        self.qtabwidget = QtWidgets.QTabWidget(self) 
        self.qtabwidget.setFont(QtGui.QFont("微軟正黑體", 7))
       
        widget  = QtWidgets.QPlainTextEdit("QPlainTextEdit 1")
        #label   = 'Tab &1'
        label   = ' FHE '
        
        #widget2 = QtWidgets.QPlainTextEdit("QPlainTextEdit 2")
       
        tab_index1 = self.qtabwidget.addTab(widget, label)
        
        
        
#############TAB2
        self.widgetA2 =QtWidgets.QWidget()
        
        tab_index2 = self.qtabwidget.addTab(self.widgetA2, ' 使用者設定 ')
        
        self.qtabwidget.setTabIcon(tab_index2, QtGui.QIcon('d:\\FHEUI\\fig\\usr-circle-cropped.png'))
        self.qtabwidget.setIconSize(QtCore.QSize(35, 35)) 
        
        FonA = "font-size: 40pt; font: bold;font-family:微軟正黑體 ;"
        
#### CHK btn      
      
        self.LBLa99 = QLabel(" CHECK ", self.widgetA2)
        self.LBLa99.setStyleSheet("font-size: 12pt; font-family: Arial;background-color:rgb(85, 170, 255);color:white;border-radius: 5px; text-align:center")
        self.LBLa99.setAlignment(QtCore.Qt.AlignCenter)
        self.LBLa99.setGeometry(1250, 515, 75, 30)
        buttona00 = QPushButton(" NEXT ", self.widgetA2)

         
        buttona00.setGeometry(1240, 550, 100, 45)
        buttona00.setStyleSheet("QPushButton{background-image : url(/FHEUI/icon/forward1.png);border-radius: 15px;  border: 2px groove gray; border-style: outset;}""QPushButton:hover{background-image:url(/FHEUI/fig/itrilogohover.png)}""QPushButton:pressed{background-color:rgb(85, 170, 255);color:white; border-style: inset; }")
        buttona00.clicked.connect(self.changetab2)
        

######################################################################        
        self.buttonT01 = QPushButton(' ', self.widgetA2)
        #self.buttonT01.setStyleSheet("QPushButton{color:white}";"QPushButton:hover{color:green};QPushButton{background-color:#1E1E1E};QPushButton{border:1px}; QPushButton{border-radius:2px};QPushButton{background-image : url(/FHEUI/fig/hand2-circle-cropped.png);QPushButton{padding:2px 4px};")
        #self.buttonT01.setStyleSheet("QPushButton{background-image:url(/FHEUI/fig/hand2-circle-cropped.png)")
        self.buttonT01.setStyleSheet("QPushButton{background-image : url(/FHEUI/fig/itrilogo7575.png);border-radius: 2px;  border: 2px groove gray; border-style: outset;}""QPushButton:hover{background-image:url(/FHEUI/fig/itrilogohover2.jpg)}""QPushButton:pressed{background-color:rgb(85, 170, 255);color:white; border-style: inset; }")   
        
        self.buttonT01.setMinimumHeight(80)
        self.buttonT01.setGeometry(0,100,80,80)
        self.buttonT01.setToolTip('分析記錄檔')
       # QToolTip.setFont(QFont('SansSerif', 10))
       # self.buttonT01.move(20, 150)
        self.buttonT01.clicked.connect(self.changetab7)
        
######################################################################         
        self.buttonT02 = QPushButton('補償模組', self.widgetA2)
        self.buttonT02.setStyleSheet("QPushButton{color:white}"
                                  "QPushButton:hover{color:yellow}"
                                  "QPushButton{background-color:#7F667F}"
                                  "QPushButton{border:1px}"
                                  "QPushButton{border-radius:2px}"
                                  "QPushButton{padding:2px 4px}")        
        
        
        self.buttonT02.setMinimumHeight(80)
        self.buttonT02.setGeometry(0,180,80,80)
        self.buttonT02.setToolTip('訊號處理與補償設計') 
        self.buttonT02.clicked.connect(self.changetab3)
######################################################################
        self.buttonT03 = QPushButton('拉伸線路', self.widgetA2)
        self.buttonT03.setStyleSheet("QPushButton{color:white}"
                                  "QPushButton:hover{color:yellow}"
                                  "QPushButton{background-color:#7F667F}"
                                  "QPushButton{border:1px}"
                                  "QPushButton{border-radius:2px}"
                                  "QPushButton{padding:2px 4px}")        
        
        
        self.buttonT03.setMinimumHeight(80)
        self.buttonT03.setGeometry(0,260,80,80)
        self.buttonT03.setToolTip('可拉伸線路設計')
        self.buttonT03.clicked.connect(self.changetab4)    
######################################################################
        self.buttonT04 = QPushButton('耐衝擊I', self.widgetA2)
        self.buttonT04.setStyleSheet("QPushButton{color:white}"
                                  "QPushButton:hover{color:yellow}"
                                  "QPushButton{background-color:#7F667F}"
                                  "QPushButton{border:1px}"
                                  "QPushButton{border-radius:2px}"
                                  "QPushButton{padding:2px 4px}")        
        
        
        self.buttonT04.setMinimumHeight(80)
        self.buttonT04.setGeometry(0,340,80,80)
        self.buttonT04.setToolTip('防水與耐衝擊')
        self.buttonT04.clicked.connect(self.changetab5)     

######################################################################
        self.buttonT05 = QPushButton('P_專案', self.widgetA2)
        self.buttonT05.setStyleSheet("QPushButton{color:white}"
                                  "QPushButton:hover{color:yellow}"
                                  "QPushButton{background-color:#7F667F}"
                                  "QPushButton{border:1px}"
                                  "QPushButton{border-radius:2px}"
                                  "QPushButton{padding:2px 4px}")        
        
        
        self.buttonT05.setMinimumHeight(80)
        self.buttonT05.setGeometry(0,420,80,80)
        self.buttonT05.setToolTip('POC_專案管理')
        self.buttonT05.clicked.connect(self.itemsFileshow)     
######################################################################
        self.buttonT06 = QPushButton('POC_設計', self.widgetA2)
        self.buttonT06.setStyleSheet("QPushButton{color:white}"
                                  "QPushButton:hover{color:yellow}"
                                  "QPushButton{background-color:#7F667F}"
                                  "QPushButton{border:1px}"
                                  "QPushButton{border-radius:2px}"
                                  "QPushButton{padding:2px 4px}")        
        
        
        self.buttonT06.setMinimumHeight(80)
        self.buttonT06.setGeometry(0,500,80,80)
        self.buttonT06.setToolTip('POC設計架構')   
        self.buttonT06.clicked.connect(self.changetab8) 
######################################################################
        self.buttonT07 = QPushButton('電路模型', self.widgetA2)
        self.buttonT07.setStyleSheet("QPushButton{color:white}"
                                  "QPushButton:hover{color:yellow}"
                                  "QPushButton{background-color:#7F667F}"
                                  "QPushButton{border:1px}"
                                  "QPushButton{border-radius:2px}"
                                  "QPushButton{padding:2px 4px}")        
        
        
        self.buttonT07.setMinimumHeight(80)
        self.buttonT07.setGeometry(0,580,80,80)
        self.buttonT07.setToolTip('POC電路模型') 
        self.buttonT07.clicked.connect(self.changetab9)  


        self.indexa00 = QLabel(self.widgetA2)
        self.ima00 = QPixmap('d:\\FHEUI\\fig\\index1.jpg') 
        self.indexa00.setPixmap(self.ima00) 
        self.indexa00.setGeometry(85,50,1150,600)    


                
###################################################################
        self.buttonTip01 = QPushButton(' ', self.widgetA2)
        self.buttonTip01.setStyleSheet("QPushButton{color:white}"
                                  "QPushButton:hover{color:yellow}"
                                  "QPushButton{background-color:transparent}"
                                  "QPushButton{border:1px}"
                                  "QPushButton{border-radius:2px}"
                                  "QPushButton{padding:2px 4px}")        
        
        
        self.buttonTip01.setMinimumHeight(320)
        self.buttonTip01.setGeometry(85,100,380,320)
        self.buttonTip01.setToolTip('智慧褲線路布局')
        self.buttonTip01.clicked.connect(self.ALL001) 

###################################################################
        self.buttonTip02 = QPushButton(' ', self.widgetA2)
        self.buttonTip02.setStyleSheet("QPushButton{color:white}"
                                  "QPushButton:hover{color:yellow}"
                                  "QPushButton{background-color:transparent}"
                                  "QPushButton{border:1px}"
                                  "QPushButton{border-radius:2px}"
                                  "QPushButton{padding:2px 4px}")        
        
        
        self.buttonTip02.setMinimumHeight(320)
        self.buttonTip02.setGeometry(470,100,700,320)
        self.buttonTip02.setToolTip('EXG系統板功能')    

###################################################################
        self.buttonTip03 = QPushButton(' ', self.widgetA2)
        self.buttonTip03.setStyleSheet("QPushButton{color:white}"
                                  "QPushButton:hover{color:yellow}"
                                  "QPushButton{background-color:transparent}"
                                  "QPushButton{border:1px}"
                                  "QPushButton{border-radius:2px}"
                                  "QPushButton{padding:2px 4px}")        
        
        
        self.buttonTip03.setMinimumHeight(210)
        self.buttonTip03.setGeometry(85,425,330,210)
        self.buttonTip03.setToolTip('可拉伸線路佈局')    


###################################################################
        self.buttonTip04 = QPushButton(' ', self.widgetA2)
        self.buttonTip04.setStyleSheet("QPushButton{color:white}"
                                  "QPushButton:hover{color:yellow}"
                                  "QPushButton{background-color:transparent}"
                                  "QPushButton{border:1px}"
                                  "QPushButton{border-radius:2px}"
                                  "QPushButton{padding:2px 4px}")        
        
        
        self.buttonTip04.setMinimumHeight(210)
        self.buttonTip04.setGeometry(390,425,355,210)
        self.buttonTip04.setToolTip('耐衝擊設計')      

###################################################################
        self.buttonTip05 = QPushButton(' ', self.widgetA2)
        self.buttonTip05.setStyleSheet("QPushButton{color:white}"
                                  "QPushButton:hover{color:yellow}"
                                  "QPushButton{background-color:transparent}"
                                  "QPushButton{border:1px}"
                                  "QPushButton{border-radius:2px}"
                                  "QPushButton{padding:2px 4px}")        
        
      
        self.buttonTip05.setMinimumHeight(210)
        self.buttonTip05.setGeometry(750,425,420,210)
        self.buttonTip05.setToolTip('耐彎曲設計')    

############### 標題移至最上
        self.LBLa00 = QLabel("使用者設定", self.widgetA2)
        #self.LBLa00.setStyleSheet("font-size: 40pt; font: bold;font-family:微軟正黑體 ;")
        self.LBLa00.setStyleSheet(FonA)
        self.LBLa00.setGeometry(450, 10, 700, 50) 
        self.LBLa00.setScaledContents(True)      
        self.LBLa00.show()
        self.labelitria = QLabel(self.widgetA2)
        self.imitria = QPixmap('d:\\FHEUI\\fig\\itrigray.jpg') #要確認 Lena.png 路徑
        self.labelitria.setPixmap(self.imitria) #將 image 加入 label
        self.labelitria.setGeometry(5,5,238,77)
       # self.labelitria.setGeometry(5,5,238,60)        
        
        #設定背景圖片
        #palette1 = QPalette()
        #palette1.setBrush(self.backgroundRole(), QBrush(QPixmap('background.jpg')))
        #self.setPalette(palette1)
        
        
        

        
        
        
        
        
        
        
        
        
        
        # TAB3 設定                       
        #self.qtabwidget.addTab(QtWidgets.QLabel("QLabel Tab &3", alignment=QtCore.Qt.AlignCenter), QtGui.QIcon('d:\itrilogo.png'),'  FHE系統整合設計  ')
       
        self.widgetA3 =QtWidgets.QWidget()
       
        tab_index3 = self.qtabwidget.addTab(self.widgetA3, '  FHE系統整合設計  ')
        self.qtabwidget.setTabIcon(tab_index3, QtGui.QIcon('d:\\FHEUI\\fig\\hand2-circle-cropped.png'))
        self.qtabwidget.setIconSize(QtCore.QSize(35, 35)) 
        
        self.buttonU01 = QPushButton(' ', self.widgetA3)
        self.buttonU01.setStyleSheet("QPushButton{background-image : url(/FHEUI/fig/itrilogo7575.png);border-radius: 2px;  border: 2px groove gray; border-style: outset;}""QPushButton:hover{background-image:url(/FHEUI/fig/itrilogohover2.jpg)}""QPushButton:pressed{background-color:rgb(85, 170, 255);color:white; border-style: inset; }")   
        self.buttonU01.setMinimumHeight(80)
        self.buttonU01.setGeometry(0,100,80,80)
        self.buttonU01.setToolTip('分析記錄檔')
        self.buttonU01.clicked.connect(self.changetab7)


        self.buttonU02 = QPushButton('補償模組', self.widgetA3)
        self.buttonU02.setStyleSheet("QPushButton{color:white}"
                                  "QPushButton:hover{color:yellow}"
                                  "QPushButton{background-color:#809980}"
                                  "QPushButton{border:1px}"
                                  "QPushButton{border-radius:2px}"
                                  "QPushButton{padding:2px 4px}")        
        
        
        self.buttonU02.setMinimumHeight(80)
        self.buttonU02.setGeometry(0,180,80,80)
        self.buttonU02.setToolTip('訊號處理與補償設計') 
        self.buttonU02.clicked.connect(self.changetab3) 
######################################################################
        self.buttonU03 = QPushButton('拉伸線路', self.widgetA3)
        self.buttonU03.setStyleSheet("QPushButton{color:white}"
                                  "QPushButton:hover{color:yellow}"
                                  "QPushButton{background-color:#809980}"
                                  "QPushButton{border:1px}"
                                  "QPushButton{border-radius:2px}"
                                  "QPushButton{padding:2px 4px}")        
        
        
        self.buttonU03.setMinimumHeight(80)
        self.buttonU03.setGeometry(0,260,80,80)
        self.buttonU03.setToolTip('可拉伸線路設計')
        self.buttonU03.clicked.connect(self.changetab4)     
######################################################################
        self.buttonU04 = QPushButton('耐衝擊I', self.widgetA3)
        self.buttonU04.setStyleSheet("QPushButton{color:white}"
                                  "QPushButton:hover{color:yellow}"
                                  "QPushButton{background-color:#809980}"
                                  "QPushButton{border:1px}"
                                  "QPushButton{border-radius:2px}"
                                  "QPushButton{padding:2px 4px}")        
        
        
        self.buttonU04.setMinimumHeight(80)
        self.buttonU04.setGeometry(0,340,80,80)
        self.buttonU04.setToolTip('防水與耐衝擊')
        self.buttonU04.clicked.connect(self.changetab5)    

######################################################################
        self.buttonU05 = QPushButton('P_專案', self.widgetA3)
        self.buttonU05.setStyleSheet("QPushButton{color:white}"
                                  "QPushButton:hover{color:yellow}"
                                  "QPushButton{background-color:#809980}"
                                  "QPushButton{border:1px}"
                                  "QPushButton{border-radius:2px}"
                                  "QPushButton{padding:2px 4px}")        
        
        
        self.buttonU05.setMinimumHeight(80)
        self.buttonU05.setGeometry(0,420,80,80)
        self.buttonU05.setToolTip('POC_專案管理')
        self.buttonU05.clicked.connect(self.itemsFileshow)    
######################################################################
        self.buttonU06 = QPushButton('POC_設計', self.widgetA3)
        self.buttonU06.setStyleSheet("QPushButton{color:white}"
                                  "QPushButton:hover{color:yellow}"
                                  "QPushButton{background-color:#809980}"
                                  "QPushButton{border:1px}"
                                  "QPushButton{border-radius:2px}"
                                  "QPushButton{padding:2px 4px}")        
        
        
        self.buttonU06.setMinimumHeight(80)
        self.buttonU06.setGeometry(0,500,80,80)
        self.buttonU06.setToolTip('POC設計架構')   
        self.buttonU06.clicked.connect(self.changetab8)   

######################################################################
        self.buttonU07 = QPushButton('電路模型', self.widgetA3)
        self.buttonU07.setStyleSheet("QPushButton{color:white}"
                                  "QPushButton:hover{color:yellow}"
                                  "QPushButton{background-color:#809980}"
                                  "QPushButton{border:1px}"
                                  "QPushButton{border-radius:2px}"
                                  "QPushButton{padding:2px 4px}")        
        
        
        self.buttonU07.setMinimumHeight(80)
        self.buttonU07.setGeometry(0,580,80,80)
        self.buttonU07.setToolTip('POC電路模型') 
        self.buttonU07.clicked.connect(self.changetab9)  








        

        self.LBL000 = QLabel("FHE系統整合設計", self.widgetA3)
        self.LBL000.setStyleSheet(FonA)
        self.LBL000.setGeometry(450,10, 700, 50)
        self.LBL999 = QLabel(" CHECK ", self.widgetA3)
        
        self.LBL999.setStyleSheet("font-size: 12pt; font-family: Arial;background-color:rgb(85, 170, 255);color:white;border-radius: 5px; text-align:center")
        self.LBL999.setAlignment(QtCore.Qt.AlignCenter)
        self.LBL999.setGeometry(1250, 515, 75, 30)
        
        button000 = QPushButton(" NEXT ", self.widgetA3)
        button000.setGeometry(1285, 550, 60, 45)
        button000.setStyleSheet("QPushButton{background-image : url(/FHEUI/icon/forward1.png);border-radius: 12px;  border: 2px groove gray; border-style: outset;}""QPushButton:hover{background-image:url(/FHEUI/fig/itrilogohover.png)}""QPushButton:pressed{background-color:rgb(85, 170, 255);color:white; border-style: inset; }")
        button000.clicked.connect(self.changetab3)

        button001 = QPushButton(" BACK ", self.widgetA3) 
        button001.setGeometry(1220,550, 60, 45)
        button001.setStyleSheet("QPushButton{background-image : url(/FHEUI/icon/backward1.png);border-radius: 12px;  border: 2px groove gray; border-style: outset;}""QPushButton:hover{background-image:url(/FHEUI/fig/itrilogohover.png)}""QPushButton:pressed{background-color:rgb(85, 170, 255);color:white; border-style: inset; }")
        button001.clicked.connect(self.changetab1)


        self.labelitri = QLabel(self.widgetA3)
        self.imitri = QPixmap('d:\\FHEUI\\fig\\itrigray.jpg') #要確認 Lena.png 路徑
        self.labelitri.setPixmap(self.imitri) #將 image 加入 label
        self.labelitri.setGeometry(5,5,238,77)

        w1=85
        h0=100
        h1=0
        h2=10
        h3=10
        hp001=50
        hcomb001=30 #Combobox 寬

        self.labelc01 = QLabel(self.widgetA3)
        self.moviec01 = QMovie("d:\\FHEUI\\fig\\baseball_0-787_3.gif")
        self.labelc01.setMovie(self.moviec01)
        self.labelc01.setGeometry(85,505,150,195) # 大小

        self.moviec01.start()
        
        self.LBL = QPushButton("測試載具", self.widgetA3)
        self.LBL.setStyleSheet("font-size: 16pt; font-family: Arial;")
        self.LBL.setGeometry(w1, h0, 150, hp001)
        self.LBL.clicked.connect(self.labellink003)
        
        self.combobox_1 = QComboBox(self.widgetA3)                   # 1
        self.combobox_1.setObjectName('myQComboBox')
       # self.combobox_1.setStyleSheet("font-size: 10pt; font-family: Arial;")
        self.combobox_1.setGeometry(w1,h0+h1+hp001,150,hcomb001) # 大小
      
        #self.LBL002 = QLabel("偵測肌群位置", self)
        self.LBL002 = QPushButton("偵測肌群位置", self.widgetA3)
        self.LBL002.setStyleSheet("font-size: 16pt; font-family: Arial; ")
        self.LBL002.setGeometry(w1, 200, 150, hp001)
        self.LBL002.clicked.connect(self.labellink004)
        
        self.combobox_2 = QComboBox(self.widgetA3)                   # 1
        self.combobox_2.setObjectName('myQComboBox2')
        self.combobox_2.setGeometry(w1,240,150,hcomb001) # 大小
        # self.v_layout = QVBoxLayout()
       
        self.LBL003 = QPushButton("電極型態", self.widgetA3)
        self.LBL003.setStyleSheet("font-size: 16pt; font-family: Arial; ")
        self.LBL003.setGeometry(w1, 300, 150, hp001)
        self.LBL003.clicked.connect(self.labellink003_1)
        
        self.combobox_3 = QComboBox(self.widgetA3)                   # 1
        self.combobox_3.setObjectName('myQComboBox3')
        self.combobox_3.setGeometry(w1,340,150,hcomb001) # 大小
        
        
        self.LBL004 = QPushButton("控制器位置", self.widgetA3)
        self.LBL004.setStyleSheet("font-size: 16pt; font-family: Arial; ")
        self.LBL004.setGeometry(w1, 400, 150, hp001)
        self.LBL004.clicked.connect(self.labellink003_2)
        
        self.combobox_4 = QComboBox(self.widgetA3)                   # 1
        self.combobox_4.setObjectName('myQComboBox4')
        self.combobox_4.setGeometry(w1,440,150,hcomb001) # 大小
        
        
        
        
        
        self.label01 = QLabel(self.widgetA3)
        self.im01 = QPixmap('d:\\FHEUI\\fig\\testvehicle.png') #要確認 Lena.png 路徑
        self.label01.setPixmap(self.im01) #將 image 加入 label
        self.label01.setGeometry(240,70,900,300)
#        self.label01.setStyleSheet("border-radius: 10px;background-color:rgb(85, 170, 255);")
        
       # self.label02 = QLabel(self.widgetA3)
       # self.label02.setGeometry(400,70,300,200) # 大小
        
        self.label03 = QLabel(self.widgetA3)
        self.im03 = QPixmap('d:\\FHEUI\\fig\\pants001.png') #要確認 Lena.png 路徑
        self.label03.setPixmap(self.im03) #將 image 加入 label
        self.label03.setGeometry(240,370,300,300) # 大小
        self.label03.setPixmap(self.im03.scaled(300,300,
                Qt.KeepAspectRatio, Qt.SmoothTransformation)) 

      
        self.label05 = QLabel(self.widgetA3)
        self.im05 = QPixmap('d:\\FHEUI\\fig\\electrode_Ag.jpg') #要確認 Lena.png 路徑
        self.label05.setPixmap(self.im05) #將 image 加入 label
        self.label05.setGeometry(550,370,200,300) # 大小 
        self.label05.setPixmap(self.im05.scaled(200,300,
                Qt.KeepAspectRatio, Qt.SmoothTransformation))    
      
      
      
        self.label07 = QLabel(self.widgetA3)
        self.im07 = QPixmap('d:\\FHEUI\\fig\\右腰.png') #要確認 Lena.png 路徑
        #self.label07.setPixmap(self.im07) #將 image 加入 label
        self.label07.setPixmap(self.im07.scaled(300,300,
                Qt.KeepAspectRatio, Qt.SmoothTransformation))
        self.label07.setGeometry(760,370,300,300) # 大

        
        self.combobox_init()
      
###################################################################
        self.buttonTipU01 = QPushButton(' ', self.widgetA3)
        self.buttonTipU01.setStyleSheet("QPushButton{color:white}"
                                  "QPushButton:hover{color:yellow}"
                                  #"QPushButton{background-color:#1E1E1E}"
                                  "QPushButton{background-color:transparent}"
                                  "QPushButton{border:1px}"
                                  "QPushButton{border-radius:2px}"
                                  "QPushButton{padding:2px 4px}")        
        
        
        self.buttonTipU01.setMinimumHeight(280)
        self.buttonTipU01.setGeometry(240,80,800,280)
        self.buttonTipU01.setToolTip('智慧育樂應用趨勢')
        self.buttonTipU01.clicked.connect(self.openFile) 

###################################################################
        self.buttonTipU03 = QPushButton(' ', self.widgetA3)
        self.buttonTipU03.setStyleSheet("QPushButton{color:white}"
                                  "QPushButton:hover{color:yellow}"
                                  "QPushButton{background-color:transparent}"
                                  "QPushButton{border:1px}"
                                  "QPushButton{border-radius:2px}"
                                  "QPushButton{padding:2px 4px}")        
        
        
        self.buttonTipU03.setMinimumHeight(280)
        self.buttonTipU03.setGeometry(240,365,300,250)
        self.buttonTipU03.setToolTip('感測訊號偵測部分')    


###################################################################
        self.buttonTipU04 = QPushButton(' ', self.widgetA3)
        self.buttonTipU04.setStyleSheet("QPushButton{color:white}"
                                  "QPushButton:hover{color:yellow}"
                                  "QPushButton{background-color:transparent}"
                                  "QPushButton{border:1px}"
                                  "QPushButton{border-radius:2px}"
                                  "QPushButton{padding:2px 4px}")        
        
        
        self.buttonTipU04.setMinimumHeight(280)
        self.buttonTipU04.setGeometry(550,365,200,250)
        self.buttonTipU04.setToolTip('感測材料與感測電極')      

###################################################################
        self.buttonTipU05 = QPushButton(' ', self.widgetA3)
        self.buttonTipU05.setStyleSheet("QPushButton{color:white}"
                                  "QPushButton:hover{color:yellow}"
                                  "QPushButton{background-color:transparent}"
                                  "QPushButton{border:1px}"
                                  "QPushButton{border-radius:2px}"
                                  "QPushButton{padding:2px 4px}")        
        
      
        self.buttonTipU05.setMinimumHeight(280)
        self.buttonTipU05.setGeometry(760,365,300,250)
        self.buttonTipU05.setToolTip('ExG感測線路及控制器')    

##################################################zq#################


















  
      # TAB4 設定                       
        #self.qtabwidget.addTab(QtWidgets.QLabel("QLabel Tab &3", alignment=QtCore.Qt.AlignCenter), QtGui.QIcon('d:\itrilogo.png'),'  FHE系統整合設計  ')
       
        self.widgetA4 =QtWidgets.QWidget()
       
        tab_index4 = self.qtabwidget.addTab(self.widgetA4, '  訊號處理與補償設計  ')
        
        self.qtabwidget.setTabIcon(tab_index4, QtGui.QIcon('d:\\FHEUI\\fig\\pcb3-circle-cropped.png'))
        self.qtabwidget.setIconSize(QtCore.QSize(35, 35)) 

        self.buttonV01 = QPushButton(' ', self.widgetA4)
        self.buttonV01.setStyleSheet("QPushButton{background-image : url(/FHEUI/fig/itrilogo7575.png);border-radius: 2px;  border: 2px groove gray; border-style: outset;}""QPushButton:hover{background-image:url(/FHEUI/fig/itrilogohover2.jpg)}""QPushButton:pressed{background-color:rgb(85, 170, 255);color:white; border-style: inset; }")   
        self.buttonV01.setMinimumHeight(80)
        self.buttonV01.setGeometry(0,100,80,80)

        self.buttonV01.setToolTip('分析記錄檔')
        self.buttonV01.clicked.connect(self.changetab7)

        self.buttonV02 = QPushButton('補償模組', self.widgetA4)
        self.buttonV02.setStyleSheet("QPushButton{color:white}"
                                  "QPushButton:hover{color:yellow}"
                                  "QPushButton{background-color:#D4BA3E}"
                                  "QPushButton{border:1px}"
                                  "QPushButton{border-radius:2px}"
                                  "QPushButton{padding:2px 4px}")        
        
        
        self.buttonV02.setMinimumHeight(80)
        self.buttonV02.setGeometry(0,180,80,80)
        self.buttonV02.setToolTip('訊號處理與補償設計') 
        self.buttonV02.clicked.connect(self.changetab3)
######################################################################
        self.buttonV03 = QPushButton('拉伸線路', self.widgetA4)
        self.buttonV03.setStyleSheet("QPushButton{color:white}"
                                  "QPushButton:hover{color:yellow}"
                                  "QPushButton{background-color:#D4BA3E}"
                                  "QPushButton{border:1px}"
                                  "QPushButton{border-radius:2px}"
                                  "QPushButton{padding:2px 4px}")        
        
        
        self.buttonV03.setMinimumHeight(80)
        self.buttonV03.setGeometry(0,260,80,80)
        self.buttonV03.setToolTip('可拉伸線路設計')
        self.buttonV03.clicked.connect(self.changetab4)     
######################################################################
        self.buttonV04 = QPushButton('耐衝擊I', self.widgetA4)
        self.buttonV04.setStyleSheet("QPushButton{color:white}"
                                  "QPushButton:hover{color:yellow}"
                                  "QPushButton{background-color:#D4BA3E}"
                                  "QPushButton{border:1px}"
                                  "QPushButton{border-radius:2px}"
                                  "QPushButton{padding:2px 4px}")        
        
        
        self.buttonV04.setMinimumHeight(80)
        self.buttonV04.setGeometry(0,340,80,80)
        self.buttonV04.setToolTip('防水與耐衝擊')
        self.buttonV04.clicked.connect(self.changetab5)   

######################################################################
        self.buttonV05 = QPushButton('P_專案', self.widgetA4)
        self.buttonV05.setStyleSheet("QPushButton{color:white}"
                                  "QPushButton:hover{color:yellow}"
                                  "QPushButton{background-color:#D4BA3E}"
                                  "QPushButton{border:1px}"
                                  "QPushButton{border-radius:2px}"
                                  "QPushButton{padding:2px 4px}")        
        
        
        self.buttonV05.setMinimumHeight(80)
        self.buttonV05.setGeometry(0,420,80,80)
        self.buttonV05.setToolTip('POC_專案管理')
        self.buttonV05.clicked.connect(self.itemsFileshow)     
######################################################################
        self.buttonV06 = QPushButton('POC_設計', self.widgetA4)
        self.buttonV06.setStyleSheet("QPushButton{color:white}"
                                  "QPushButton:hover{color:yellow}"
                                  "QPushButton{background-color:#D4BA3E}"
                                  "QPushButton{border:1px}"
                                  "QPushButton{border-radius:2px}"
                                  "QPushButton{padding:2px 4px}")        
        
        
        self.buttonV06.setMinimumHeight(80)
        self.buttonV06.setGeometry(0,500,80,80)
        self.buttonV06.setToolTip('POC設計架構')   
        self.buttonV06.clicked.connect(self.changetab8)  

######################################################################
        self.buttonV07 = QPushButton('電路模型', self.widgetA4)
        self.buttonV07.setStyleSheet("QPushButton{color:white}"
                                  "QPushButton:hover{color:yellow}"
                                  "QPushButton{background-color:#D4BA3E}"
                                  "QPushButton{border:1px}"
                                  "QPushButton{border-radius:2px}"
                                  "QPushButton{padding:2px 4px}")        
        
        
        self.buttonV07.setMinimumHeight(80)
        self.buttonV07.setGeometry(0,580,80,80)
        self.buttonV07.setToolTip('POC電路模型') 
        self.buttonV07.clicked.connect(self.changetab9)    




               
        self.pushButton_b5 = QtWidgets.QPushButton(self.widgetA4)
        self.pushButton_b5.setGeometry(QtCore.QRect(1100, 20, 250, 60))
        self.pushButton_b5.setObjectName("pushButton_b5")
     #   self.pushButton_b5.setStyleSheet("background-color: #F0F0F0; color: black;font: 100 15pt \"Arial Narrow\"")
        self.pushButton_b5.setText("EMG Module Schematics")
        self.pushButton_b5.setStyleSheet("border-radius: 5px;  border: 2px groove gray; border-style: outset;}""QPushButton:hover{background-image:url(/FHEUI/fig/itrilogohover.png)}""QPushButton:pressed{background-color:rgb(85, 170, 255);color:white; border-style: inset; }")
        self.pushButton_b5.setFont(QFont('Arial', 7)) 

        self.pushButton_b5.clicked.connect(self.pdfviewer) 

        self.LBLc00 = QLabel("訊號處理與補償設計", self.widgetA4)
        self.LBLc00.setStyleSheet(FonA)
        self.LBLc00.setGeometry(450,10, 550, 50)
        self.LBLc99 = QLabel(" CHECK ", self.widgetA4)
                
        self.LBLc99.setStyleSheet("font-size: 12pt; font-family: Arial;background-color:rgb(85, 170, 255);color:white;border-radius: 5px; text-align:center")
        self.LBLc99.setAlignment(QtCore.Qt.AlignCenter)
        self.LBLc99.setGeometry(1250, 515, 75, 30)
        
        

       
        buttonc00 = QPushButton(" NEXT ", self.widgetA4)
        buttonc00.setGeometry(1285, 550, 60, 45)
        buttonc00.setStyleSheet("QPushButton{background-image : url(/FHEUI/icon/forward1.png);border-radius: 12px;  border: 2px groove gray; border-style: outset;}""QPushButton:hover{background-image:url(/FHEUI/fig/itrilogohover.png)}""QPushButton:pressed{background-color:rgb(85, 170, 255);color:white; border-style: inset; }")
        buttonc00.clicked.connect(self.changetab4)

        buttonc01 = QPushButton(" BACK ", self.widgetA4) 
        buttonc01.setGeometry(1220,550, 60, 45)
        buttonc01.setStyleSheet("QPushButton{background-image : url(/FHEUI/icon/backward1.png);border-radius: 12px;  border: 2px groove gray; border-style: outset;}""QPushButton:hover{background-image:url(/FHEUI/fig/itrilogohover.png)}""QPushButton:pressed{background-color:rgb(85, 170, 255);color:white; border-style: inset; }")
        buttonc01.clicked.connect(self.changetab2) 
       
        self.labelitric = QLabel(self.widgetA4)
        self.imitric = QPixmap('d:\\FHEUI\\fig\\itrigray.jpg') #要確認 Lena.png 路徑
        self.labelitric.setPixmap(self.imitric) #將 image 加入 label
        self.labelitric.setGeometry(5,5,238,77)
       

         
        self.indexc00 = QLabel(self.widgetA4)
        self.imc00 = QPixmap('d:\\FHEUI\\fig\\signal.jpg') 
        self.indexc00.setPixmap(self.imc00) 
        self.indexc00.setGeometry(85,100,1000,600) 

###################################################################
        self.buttonTiQ01 = QPushButton(' ', self.widgetA4)
        self.buttonTiQ01.setStyleSheet("QPushButton{color:white}"
                                  "QPushButton:hover{color:yellow}"
                                  "QPushButton{background-color:transparent}"
                                  
                                  "QPushButton{border:1px}"
                                  "QPushButton{border-radius:2px}"
                                  "QPushButton{padding:2px 4px}")        
        
        
        self.buttonTiQ01.setMinimumHeight(260)
        self.buttonTiQ01.setGeometry(85,100,190,260)
        self.buttonTiQ01.setToolTip('導線拉伸條件')
        self.buttonTiQ01.clicked.connect(self.SIG001) 
 
        

###################################################################
        self.buttonTiQ01a = QPushButton(' ', self.widgetA4)
        self.buttonTiQ01a.setStyleSheet("QPushButton{color:white}"
                                  "QPushButton:hover{color:yellow}"
                                  "QPushButton{background-color:transparent}"
                                  
                                  "QPushButton{border:1px}"
                                  "QPushButton{border-radius:2px}"
                                  "QPushButton{padding:2px 4px}")        
        
        
        self.buttonTiQ01a.setMinimumHeight(260)
        self.buttonTiQ01a.setGeometry(280,100,190,260)
        self.buttonTiQ01a.setToolTip('電極距離條件')
        self.buttonTiQ01a.clicked.connect(self.SIG001) 

###################################################################
        self.buttonTiQ01b = QPushButton(' ', self.widgetA4)
        self.buttonTiQ01b.setStyleSheet("QPushButton{color:white}"
                                  "QPushButton:hover{color:yellow}"
                                  "QPushButton{background-color:transparent}"
                                  
                                  "QPushButton{border:1px}"
                                  "QPushButton{border-radius:2px}"
                                  "QPushButton{padding:2px 4px}")        
        
        
        self.buttonTiQ01b.setMinimumHeight(260)
        self.buttonTiQ01b.setGeometry(475,100,190,260)
        self.buttonTiQ01b.setToolTip('電極偏移條件')
        self.buttonTiQ01b.clicked.connect(self.SIG001) 

###################################################################
        self.buttonTiQ02 = QPushButton(' ', self.widgetA4)
        self.buttonTiQ02.setStyleSheet("QPushButton{color:white}"
                                  "QPushButton:hover{color:yellow}"
                                  "QPushButton{background-color:transparent}"
                                 # "QPushButton{background-color:transparent}"
                                  "QPushButton{border:1px}"
                                  "QPushButton{border-radius:2px}"
                                  "QPushButton{padding:2px 4px}")        
        
        
        self.buttonTiQ02.setMinimumHeight(260)
        self.buttonTiQ02.setGeometry(670,100,200,260)
        self.buttonTiQ02.setToolTip('訊號源條件') 
        self.buttonTiQ02.clicked.connect(self.SIG001)   

###################################################################
        self.buttonTiQ03 = QPushButton(' ', self.widgetA4)
        self.buttonTiQ03.setStyleSheet("QPushButton{color:white}"
                                  "QPushButton:hover{color:yellow}"
                                  "QPushButton{background-color:transparent}"
                                  "QPushButton{border:1px}"
                                  "QPushButton{border-radius:2px}"
                                  "QPushButton{padding:2px 4px}")        
        
        
        self.buttonTiQ03.setMinimumHeight(270)
        self.buttonTiQ03.setGeometry(85,365,400,270)
        self.buttonTiQ03.setToolTip('無補償設計輸出')
        self.buttonTiQ03.clicked.connect(self.ngSPICE)     

###################################################################
        self.buttonTiQ03a = QPushButton(' ', self.widgetA4)
        self.buttonTiQ03a.setStyleSheet("QPushButton{color:white}"
                                  "QPushButton:hover{color:yellow}"
                                  "QPushButton{background-color:transparent}"
                                  "QPushButton{border:1px}"
                                  "QPushButton{border-radius:2px}"
                                  "QPushButton{padding:2px 4px}")        
        
        
        self.buttonTiQ03a.setMinimumHeight(270)
        self.buttonTiQ03a.setGeometry(490,365,400,270)
        self.buttonTiQ03a.setToolTip('補償設計輸出')
        self.buttonTiQ03a.clicked.connect(self.ngSPICE2)     
###################################################################
       

  #      self.pushButton_c5 = QtWidgets.QPushButton(self.widgetA4)
  #      self.pushButton_c5.setGeometry(QtCore.QRect(1100, 5, 200, 60))
  #      self.pushButton_c5.setObjectName("pushButton_c5")
  #      self.pushButton_c5.setStyleSheet("background-color: #F0F0F0; color: black;font: 100 15pt \"Arial Narrow\"")
  #      self.pushButton_c5.setText("EMG Module Schematics")
  #      self.pushButton_c5.setFont(QFont('Arial', 7)) 

  #      self.pushButton_c5.clicked.connect(self.pdfviewer) 







        
     # TAB5 設定                       
       
       
        self.widgetA5 =QtWidgets.QWidget()
       
        tab_index5 = self.qtabwidget.addTab(self.widgetA5, '  可拉伸線路佈局設計  ')
        
        self.qtabwidget.setTabIcon(tab_index5, QtGui.QIcon('d:\\FHEUI\\fig\\trace1-circle-cropped.png'))
        self.qtabwidget.setIconSize(QtCore.QSize(35, 35)) 
     
        self.buttonW01 = QPushButton(' ', self.widgetA5)
        self.buttonW01.setStyleSheet("QPushButton{background-image : url(/FHEUI/fig/itrilogo7575.png);border-radius: 2px;  border: 2px groove gray; border-style: outset;}""QPushButton:hover{background-image:url(/FHEUI/fig/itrilogohover2.jpg)}""QPushButton:pressed{background-color:rgb(85, 170, 255);color:white; border-style: inset; }")   
        self.buttonW01.setMinimumHeight(80)
        self.buttonW01.setGeometry(0,100,80,80)

        self.buttonW01.setToolTip('分析記錄檔')
        self.buttonW01.clicked.connect(self.changetab7)




        self.buttonW02 = QPushButton('補償模組', self.widgetA5)
        self.buttonW02.setStyleSheet("QPushButton{color:white}"
                                  "QPushButton:hover{color:yellow}"
                                  "QPushButton{background-color:#B3B200}"
                                  "QPushButton{border:1px}"
                                  "QPushButton{border-radius:2px}"
                                  "QPushButton{padding:2px 4px}")        
        
        
        self.buttonW02.setMinimumHeight(80)
        self.buttonW02.setGeometry(0,180,80,80)
        self.buttonW02.setToolTip('訊號處理與補償設計') 
        self.buttonW02.clicked.connect(self.changetab3) 
######################################################################
        self.buttonW03 = QPushButton('拉伸線路', self.widgetA5)
        self.buttonW03.setStyleSheet("QPushButton{color:white}"
                                  "QPushButton:hover{color:yellow}"
                                  "QPushButton{background-color:#B3B200}"
                                  "QPushButton{border:1px}"
                                  "QPushButton{border-radius:2px}"
                                  "QPushButton{padding:2px 4px}")        
        
        
        self.buttonW03.setMinimumHeight(80)
        self.buttonW03.setGeometry(0,260,80,80)
        self.buttonW03.setToolTip('可拉伸線路設計')
        self.buttonW03.clicked.connect(self.changetab4)     
######################################################################
        self.buttonW04 = QPushButton('耐衝擊I', self.widgetA5)
        self.buttonW04.setStyleSheet("QPushButton{color:white}"
                                  "QPushButton:hover{color:yellow}"
                                  "QPushButton{background-color:#B3B200}"
                                  "QPushButton{border:1px}"
                                  "QPushButton{border-radius:2px}"
                                  "QPushButton{padding:2px 4px}")        
        
        
        self.buttonW04.setMinimumHeight(80)
        self.buttonW04.setGeometry(0,340,80,80)
        self.buttonW04.setToolTip('防水與耐衝擊')
        self.buttonW04.clicked.connect(self.changetab5)   

######################################################################
        self.buttonW05 = QPushButton('P_專案', self.widgetA5)
        self.buttonW05.setStyleSheet("QPushButton{color:white}"
                                  "QPushButton:hover{color:yellow}"
                                  "QPushButton{background-color:#B3B200}"
                                  "QPushButton{border:1px}"
                                  "QPushButton{border-radius:2px}"
                                  "QPushButton{padding:2px 4px}")        
        
        
        self.buttonW05.setMinimumHeight(80)
        self.buttonW05.setGeometry(0,420,80,80)
        self.buttonW05.setToolTip('POC_專案管理')
        self.buttonW05.clicked.connect(self.itemsFileshow)      
######################################################################
        self.buttonW06 = QPushButton('POC_設計', self.widgetA5)
        self.buttonW06.setStyleSheet("QPushButton{color:white}"
                                  "QPushButton:hover{color:yellow}"
                                  "QPushButton{background-color:#B3B200}"
                                  "QPushButton{border:1px}"
                                  "QPushButton{border-radius:2px}"
                                  "QPushButton{padding:2px 4px}")        
        
        
        self.buttonW06.setMinimumHeight(80)
        self.buttonW06.setGeometry(0,500,80,80)
        self.buttonW06.setToolTip('POC設計架構')   
        self.buttonW06.clicked.connect(self.changetab8)   

######################################################################
        self.buttonW07 = QPushButton('電路模型', self.widgetA5)
        self.buttonW07.setStyleSheet("QPushButton{color:white}"
                                  "QPushButton:hover{color:yellow}"
                                  "QPushButton{background-color:#B3B200}"
                                  "QPushButton{border:1px}"
                                  "QPushButton{border-radius:2px}"
                                  "QPushButton{padding:2px 4px}")        
        
        
        self.buttonW07.setMinimumHeight(80)
        self.buttonW07.setGeometry(0,580,80,80)
        self.buttonW07.setToolTip('POC電路模型') 
        self.buttonW07.clicked.connect(self.changetab9)  



        self.pushButton_d5 = QtWidgets.QPushButton(self.widgetA5)
        self.pushButton_d5.setGeometry(QtCore.QRect(1100, 20, 250, 60))
        self.pushButton_d5.setObjectName("pushButton_d5")
       # self.pushButton_d5.setStyleSheet("background-color: #F0F0F0; color: black;font: 100 15pt \"Arial Narrow\"")
        self.pushButton_d5.setText("3D Viewer")
        #self.pushButton_d5.setStyleSheet("font-size: 12pt; font-family: Arial;background-color:rgb(85, 170, 255);color:white;border-radius: 3px; text-align:center")
        self.pushButton_d5.setStyleSheet("border-radius: 5px;  border: 2px groove gray; border-style: outset;}""QPushButton:hover{background-image:url(/FHEUI/fig/itrilogohover.png)}""QPushButton:pressed{background-color:rgb(85, 170, 255);color:white; border-style: inset; }")
        self.pushButton_d5.setFont(QFont('Arial', 12)) 

        self.pushButton_d5.clicked.connect(self.APP) 

        self.LBLd00 = QLabel("可拉伸線路佈局設計", self.widgetA5)
        self.LBLd00.setStyleSheet(FonA)
        self.LBLd00.setGeometry(450,10, 550, 50)
        self.LBLd99 = QLabel(" CHECK ", self.widgetA5)
        
        
        
        self.LBLd99.setStyleSheet("font-size: 12pt; font-family: Arial;background-color:rgb(85, 170, 255);color:white;border-radius: 5px; text-align:center")
        self.LBLd99.setAlignment(QtCore.Qt.AlignCenter)
        self.LBLd99.setGeometry(1250, 515, 75, 30)
        
      
        buttond00 = QPushButton(" NEXT ", self.widgetA5)
        buttond00.setGeometry(1285, 550, 60, 45)
        buttond00.setStyleSheet("QPushButton{background-image : url(/FHEUI/icon/forward1.png);border-radius: 12px;  border: 2px groove gray; border-style: outset;}""QPushButton:hover{background-image:url(/FHEUI/fig/itrilogohover.png)}""QPushButton:pressed{background-color:rgb(85, 170, 255);color:white; border-style: inset; }")
        buttond00.clicked.connect(self.changetab5)

        buttond01 = QPushButton(" BACK ", self.widgetA5) 
        buttond01.setGeometry(1220,550, 60, 45)
        buttond01.setStyleSheet("QPushButton{background-image : url(/FHEUI/icon/backward1.png);border-radius: 12px;  border: 2px groove gray; border-style: outset;}""QPushButton:hover{background-image:url(/FHEUI/fig/itrilogohover.png)}""QPushButton:pressed{background-color:rgb(85, 170, 255);color:white; border-style: inset; }")
        buttond01.clicked.connect(self.changetab3)    
        
        
  
        
        self.labelitrid = QLabel(self.widgetA5)
        self.imitrid = QPixmap('d:\\FHEUI\\fig\\itrigray.jpg') #要確認 Lena.png 路徑
        self.labelitrid.setPixmap(self.imitrid) #將 image 加入 label
        self.labelitrid.setGeometry(5,5,238,77)
        self.indexd00 = QLabel(self.widgetA5)
        self.imd00 = QPixmap('d:\\FHEUI\\fig\\stretch.jpg') 
        self.indexd00.setPixmap(self.imd00) 
        self.indexd00.setGeometry(85,100,1000,600) 

###################################################################
        self.buttonTiS01 = QPushButton(' ', self.widgetA5)
        self.buttonTiS01.setStyleSheet("QPushButton{color:white}"
                                  "QPushButton:hover{color:yellow}"
#                                  "QPushButton{background-color:#1E1E1E}"
                                  "QPushButton{background-color:transparent}"
                                  "QPushButton{border:1px}"
                                  "QPushButton{border-radius:2px}"
                                  "QPushButton{padding:2px 4px}")        
        
        
        self.buttonTiS01.setMinimumHeight(320)
        self.buttonTiS01.setGeometry(85,100,500,320)
        self.buttonTiS01.setToolTip('智慧褲線路設計') 
###################################################################
        self.buttonTiS02 = QPushButton(' ', self.widgetA5)
        self.buttonTiS02.setStyleSheet("QPushButton{color:white}"
                                  "QPushButton:hover{color:yellow}"
                                  "QPushButton{background-color:transparent}"
                                  
                                  "QPushButton{border:1px}"
                                  "QPushButton{border-radius:2px}"
                                  "QPushButton{padding:2px 4px}")        
        
        
        self.buttonTiS02.setMinimumHeight(320)
        self.buttonTiS02.setGeometry(590,100,300,320)
        self.buttonTiS02.setToolTip('拉伸量-電阻值趨勢圖')    

###################################################################
        self.buttonTiS03 = QPushButton(' ', self.widgetA5)
        self.buttonTiS03.setStyleSheet("QPushButton{color:white}"
                                  "QPushButton:hover{color:yellow}"
                                  "QPushButton{background-color:transparent}"
                                  "QPushButton{border:1px}"
                                  "QPushButton{border-radius:2px}"
                                  "QPushButton{padding:2px 4px}")        
        
        
        self.buttonTiS03.setMinimumHeight(210)
        self.buttonTiS03.setGeometry(85,425,500,210)
        self.buttonTiS03.setToolTip('導線參數設定')    
        self.buttonTiS03.clicked.connect(self.TRACE001) 

###################################################################
        self.buttonTiS04 = QPushButton(' ', self.widgetA5)
        self.buttonTiS04.setStyleSheet("QPushButton{color:white}"
                                  "QPushButton:hover{color:yellow}"
                                  "QPushButton{background-color:transparent}"
                                  "QPushButton{border:1px}"
                                  "QPushButton{border-radius:2px}"
                                  "QPushButton{padding:2px 4px}")        
        
        
        self.buttonTiS04.setMinimumHeight(210)
        self.buttonTiS04.setGeometry(590,425,300,210)
        self.buttonTiS04.setToolTip('拉伸次數-電阻值趨勢圖')      




 ###  Dock 例子    
        self.layout02 = QHBoxLayout(self) 
       
        self.items001 = QDockWidget(self)
        self.items001.setWindowTitle("測試編號")
        self.items001.setGeometry(QtCore.QRect(1000, 50, 360, 300))
        
        
        self.listWidget = QListWidget()
        self.listWidget.setContextMenuPolicy(3)
        self.listWidget.customContextMenuRequested[QPoint].connect(self.listWidgetContext)

        self.listWidget.addItem("POC1")
        self.listWidget.addItem("POC2")
        self.listWidget.addItem("POC5")
        self.listWidget.setStyleSheet("font-size: 16pt; font-family: Arial; color: white; background-color:#1E1E1E;")
        
        self.items001.setWidget(self.listWidget)
       # self.items.setFloating(False)
        self.setCentralWidget(QTextEdit())
        self.addDockWidget(Qt.RightDockWidgetArea, self.items001)
        
        self.items001.setLayout(self.layout02)

        widget=QtWidgets.QWidget(self.widgetA5)
        self.layout003 = QtWidgets.QVBoxLayout()
        self.layout003.setContentsMargins(0, 0, 0, 0)
        self.layout003.setGeometry(QtCore.QRect(10, 10, 800, 600))
       
        widget.setStyleSheet("background-color: #F0F0F0; color: black;font: 50 12pt \"Arial Narrow\"")
        widget.setLayout(self.layout003)

        self.items001.close()

      ###  Dock 例子 設定檔 
 
        self.items102 = QDockWidget(self)
        self.items102.setWindowTitle("設定檔")
#        self.items102.setIcon(QtGui.QIcon("d:\\FHEUI\\fig\\itrilogo.png"))
#        self.items102.setWindowIcon(QIcon('d:\FHEUI\fig\itrilogo.png'))
        
###        self.items102.setStyleSheet("QIcon:"d:\\FHEUI\\fig\\itrilogo.png" ")
        self.items102.setGeometry(0,0,1300,650)
        self.items102.setMinimumSize(300, 250) 
       # self.items102.setStyleSheet("background-color: #F0F0F0; color: black;font: 50 12pt \"Arial Narrow\"")
        self.items102.setStyleSheet("background-color: #1E1E1E; color: white ;font: 50 12pt \"Arial Narrow\"")
        
        #self.addDockWidget(Qt.LeftDockWidgetArea,  self.items102)
        self.addDockWidget(Qt.RightDockWidgetArea,  self.items102)
        
        self.layout102 = QWidget(self.items102)  

#        self.layout103 = QtWidgets.QVBoxLayout()
#        self.layout103.setContentsMargins(0, 0, 0, 0)
    
#        self.layout103.setLayout(self.layout102)
        self.layout102.setGeometry(QtCore.QRect(0,0, 1300, 650))
        self.layout102.setStyleSheet("background-color: #1E1E1E; color: white ;")


        self.mdi= QMdiArea(self.layout102)  #產生實體QMdiarea區域
#        self.setCentralWidget(self.mdi)   #設置為中央視窗部件
        self.mdi.setStyleSheet("background-color: #1E1E1E; color: white ;")
        
        self.createFileActions()


################################################################################




        menuBar=self.menuBar()  #產生實體功能表列
        file=menuBar.addMenu('專案') #添加檔菜單
        #添加子功能表
        file.addAction(self.fileNewAction)
        file.addAction(self.separator)
        file.addAction(self.exitAction)
        
        self.windowMenu = menuBar.addMenu("&視窗管理")   #添加視窗功能表
        self.windowMenu.aboutToShow.connect(self.updateWindowMenu)#用於動態更新菜
#        #設置主視窗的標題
#        self.setWindowTitle("多重文檔介面示例")

        self.items102.close()


        
# TAB6 設定                       
        self.widgetA6=QtWidgets.QWidget()
       
        tab_index6 = self.qtabwidget.addTab(self.widgetA6, '  防水與耐衝擊結構設計  ')
        
        self.qtabwidget.setTabIcon(tab_index6, QtGui.QIcon('d:\\FHEUI\\fig\\droptest-circle-cropped.png'))
        self.qtabwidget.setIconSize(QtCore.QSize(35, 35)) 

        self.buttonX01 = QPushButton(' ', self.widgetA6)
        self.buttonX01.setStyleSheet("QPushButton{background-image : url(/FHEUI/fig/itrilogo7575.png);border-radius: 2px;  border: 2px groove gray; border-style: outset;}""QPushButton:hover{background-image:url(/FHEUI/fig/itrilogohover2.jpg)}""QPushButton:pressed{background-color:rgb(85, 170, 255);color:white; border-style: inset; }")   
        self.buttonX01.setMinimumHeight(80)
        self.buttonX01.setGeometry(0,100,80,80)

        self.buttonX01.setToolTip('分析記錄檔')
        self.buttonX01.clicked.connect(self.changetab7)


        self.buttonX02 = QPushButton('補償模組', self.widgetA6)
        self.buttonX02.setStyleSheet("QPushButton{color:white}"
                                  "QPushButton:hover{color:yellow}"
                                  "QPushButton{background-color:#807CFF}"
                                  "QPushButton{border:1px}"
                                  "QPushButton{border-radius:2px}"
                                  "QPushButton{padding:2px 4px}")        
        
        
        self.buttonX02.setMinimumHeight(80)
        self.buttonX02.setGeometry(0,180,80,80)
        self.buttonX02.setToolTip('訊號處理與補償設計') 
        self.buttonX02.clicked.connect(self.changetab3)
######################################################################
        self.buttonX03 = QPushButton('拉伸線路', self.widgetA6)
        self.buttonX03.setStyleSheet("QPushButton{color:white}"
                                  "QPushButton:hover{color:yellow}"
                                  "QPushButton{background-color:#807CFF}"
                                  "QPushButton{border:1px}"
                                  "QPushButton{border-radius:2px}"
                                  "QPushButton{padding:2px 4px}")        
        
        
        self.buttonX03.setMinimumHeight(80)
        self.buttonX03.setGeometry(0,260,80,80)
        self.buttonX03.setToolTip('可拉伸線路設計')
        self.buttonX03.clicked.connect(self.changetab4)    
######################################################################
        self.buttonX04 = QPushButton('耐衝擊I', self.widgetA6)
        self.buttonX04.setStyleSheet("QPushButton{color:white}"
                                  "QPushButton:hover{color:yellow}"
                                  "QPushButton{background-color:#807CFF}"
                                  "QPushButton{border:1px}"
                                  "QPushButton{border-radius:2px}"
                                  "QPushButton{padding:2px 4px}")        
        
        
        self.buttonX04.setMinimumHeight(80)
        self.buttonX04.setGeometry(0,340,80,80)
        self.buttonX04.setToolTip('防水與耐衝擊')
        self.buttonX04.clicked.connect(self.changetab5)    

######################################################################
        self.buttonX05 = QPushButton('P_專案', self.widgetA6)
        self.buttonX05.setStyleSheet("QPushButton{color:white}"
                                  "QPushButton:hover{color:yellow}"
                                  "QPushButton{background-color:#807CFF}"
                                  "QPushButton{border:1px}"
                                  "QPushButton{border-radius:2px}"
                                  "QPushButton{padding:2px 4px}")        
        
        
        self.buttonX05.setMinimumHeight(80)
        self.buttonX05.setGeometry(0,420,80,80)
        self.buttonX05.setToolTip('POC_專案管理')
        self.buttonX05.clicked.connect(self.itemsFileshow)      
######################################################################
        self.buttonX06 = QPushButton('POC_設計', self.widgetA6)
        self.buttonX06.setStyleSheet("QPushButton{color:white}"
                                  "QPushButton:hover{color:yellow}"
                                  "QPushButton{background-color:#807CFF}"
                                  "QPushButton{border:1px}"
                                  "QPushButton{border-radius:2px}"
                                  "QPushButton{padding:2px 4px}")        
        
        
        self.buttonX06.setMinimumHeight(80)
        self.buttonX06.setGeometry(0,500,80,80)
        self.buttonX06.setToolTip('POC設計架構')   
        self.buttonX06.clicked.connect(self.changetab8)   

######################################################################
        self.buttonX07 = QPushButton('電路模型', self.widgetA6)
        self.buttonX07.setStyleSheet("QPushButton{color:white}"
                                  "QPushButton:hover{color:yellow}"
                                  "QPushButton{background-color:#807CFF}"
                                  "QPushButton{border:1px}"
                                  "QPushButton{border-radius:2px}"
                                  "QPushButton{padding:2px 4px}")        
        
        
        self.buttonX07.setMinimumHeight(80)
        self.buttonX07.setGeometry(0,580,80,80)
        self.buttonX07.setToolTip('POC電路模型') 
        self.buttonX07.clicked.connect(self.changetab9)  






        self.pushButton_e5 = QtWidgets.QPushButton(self.widgetA6)
        self.pushButton_e5.setGeometry(QtCore.QRect(1100, 20, 250, 60))
        self.pushButton_e5.setObjectName("pushButton_d5")
#        self.pushButton_e5.setStyleSheet("background-color: #F0F0F0; color: black;font: 100 15pt \"Arial Narrow\"")
        self.pushButton_e5.setText("3D Design")
        self.pushButton_e5.setStyleSheet("border-radius: 5px;  border: 2px groove gray; border-style: outset;}""QPushButton:hover{background-image:url(/FHEUI/fig/itrilogohover.png)}""QPushButton:pressed{background-color:rgb(85, 170, 255);color:white; border-style: inset; }")
        self.pushButton_e5.setFont(QFont('Arial', 7)) 

        self.pushButton_e5.clicked.connect(self.Stepviewer) 

        self.LBLe00 = QLabel("防水與耐衝擊結構設計", self.widgetA6)
        self.LBLe00.setStyleSheet(FonA)
        self.LBLe00.setGeometry(450,10, 550, 50)
        self.LBLe99 = QLabel(" CHECK ", self.widgetA6)
        
        
        self.LBLe99.setStyleSheet("font-size: 12pt; font-family: Arial;background-color:rgb(85, 170, 255);color:white;border-radius: 5px; text-align:center")
        self.LBLe99.setAlignment(QtCore.Qt.AlignCenter)
     
     
        self.LBLe99.setGeometry(1250, 515, 75, 30)
        
       
        buttone00 = QPushButton(" NEXT ", self.widgetA6)
        buttone00.setGeometry(1285, 550, 60, 45)
        buttone00.setStyleSheet("QPushButton{background-image : url(/FHEUI/icon/forward1.png);border-radius: 12px;  border: 2px groove gray; border-style: outset;}""QPushButton:hover{background-image:url(/FHEUI/fig/itrilogohover.png)}""QPushButton:pressed{background-color:rgb(85, 170, 255);color:white; border-style: inset; }")
        buttone00.clicked.connect(self.changetab6)

        buttone01 = QPushButton(" BACK ", self.widgetA6) 
        buttone01.setGeometry(1220,550, 60, 45)
        buttone01.setStyleSheet("QPushButton{background-image : url(/FHEUI/icon/backward1.png);border-radius: 12px;  border: 2px groove gray; border-style: outset;}""QPushButton:hover{background-image:url(/FHEUI/fig/itrilogohover.png)}""QPushButton:pressed{background-color:rgb(85, 170, 255);color:white; border-style: inset; }")
        buttone01.clicked.connect(self.changetab4)     
        
        
        
        
        
        self.labelitrie = QLabel(self.widgetA6)
        self.imitrie = QPixmap('d:\\FHEUI\\fig\\itrigray.jpg') #要確認 Lena.png 路徑
        self.labelitrie.setPixmap(self.imitrie) #將 image 加入 label
        self.labelitrie.setGeometry(5,5,238,77)
       


        self.indexe00 = QLabel(self.widgetA6)
        self.ime00 = QPixmap('d:\\FHEUI\\fig\\impact.jpg') 
        self.indexe00.setPixmap(self.ime00) 
        self.indexe00.setGeometry(85,100,1000,600)  

###################################################################
        self.buttonTiR01 = QPushButton(' ', self.widgetA6)
        self.buttonTiR01.setStyleSheet("QPushButton{color:white}"
                                  "QPushButton:hover{color:yellow}"
                                  #"QPushButton{background-color:#1E1E1E}"
                                  "QPushButton{background-color:transparent}"
                                  "QPushButton{border:1px}"
                                  "QPushButton{border-radius:2px}"
                                  "QPushButton{padding:2px 4px}")        
        
        
        self.buttonTiR01.setMinimumHeight(260)
        self.buttonTiR01.setGeometry(85,100,430,260)
        self.buttonTiR01.setToolTip('連接器衝擊試驗圖示') 
###################################################################
        self.buttonTiR02 = QPushButton(' ', self.widgetA6)
        self.buttonTiR02.setStyleSheet("QPushButton{color:white}"
                                  "QPushButton:hover{color:yellow}"
                                  "QPushButton{background-color:transparent}"
                                  "QPushButton{border:1px}"
                                  "QPushButton{border-radius:2px}"
                                  "QPushButton{padding:2px 4px}")        
        
        
        self.buttonTiR02.setMinimumHeight(320)
        self.buttonTiR02.setGeometry(540,100,530,320)
        self.buttonTiR02.setToolTip('EXG系統板衝擊圖示')    

###################################################################
        self.buttonTiR03 = QPushButton(' ', self.widgetA6)
        self.buttonTiR03.setStyleSheet("QPushButton{color:white}"
                                  "QPushButton:hover{color:yellow}"
                                  "QPushButton{background-color:transparent}"
                                  "QPushButton{border:1px}"
                                  "QPushButton{border-radius:2px}"
                                  "QPushButton{padding:2px 4px}")        
        
        
        self.buttonTiR03.setMinimumHeight(270)
        self.buttonTiR03.setGeometry(85,360,300,270)
        self.buttonTiR03.setToolTip('耐衝擊設計條件')    
        

###################################################################
        self.buttonTiR04 = QPushButton(' ', self.widgetA6)
        self.buttonTiR04.setStyleSheet("QPushButton{color:white}"
                                  "QPushButton:hover{color:yellow}"
                                  "QPushButton{background-color:transparent}"
                                  "QPushButton{border:1px}"
                                  "QPushButton{border-radius:2px}"
                                  "QPushButton{padding:2px 4px}")        
        
        
        self.buttonTiR04.setMinimumHeight(270)
        self.buttonTiR04.setGeometry(390,360,140,270)
        self.buttonTiR04.setToolTip('衝擊試驗條件')      
        self.buttonTiR04.clicked.connect(self.IMPACT001) 
###################################################################
        self.buttonTiR05 = QPushButton(' ', self.widgetA6)
        self.buttonTiR05.setStyleSheet("QPushButton{color:white}"
                                  "QPushButton:hover{color:yellow}"
                                  "QPushButton{background-color:transparent}"
                                  "QPushButton{border:1px}"
                                  "QPushButton{border-radius:2px}"
                                  "QPushButton{padding:2px 4px}")        
        
      
        self.buttonTiR05.setMinimumHeight(210)
        self.buttonTiR05.setGeometry(535,425,400,210)
        self.buttonTiR05.setToolTip('衝擊試驗結果')    


###
#### TAB22                     
        
        self.widgetA22=QtWidgets.QWidget()
        tab_index22 = self.qtabwidget.addTab(self.widgetA22, '設計輸出')
#        self.widgetA22 =QtWidgets.QWidget() 
#        self.qtabwidget.addTab(self.widgetA22, '設計輸出') 
        self.qtabwidget.setTabIcon(tab_index22, QtGui.QIcon('d:\\FHEUI\\fig\\output-circle-cropped.png'))
        self.qtabwidget.setIconSize(QtCore.QSize(35, 35)) 

        self.LBLe018Z = QLabel("POC1 設計分析", self.widgetA22)
        self.LBLe018Z.setStyleSheet(FonA)
        self.LBLe018Z.setGeometry(450,10, 550, 50)
        
        #分頁內來個圖 
        self.labelitrid = QLabel(self.widgetA22) #於分頁內建立label
        self.imitrid = QPixmap('d:\\FHEUI\\fig\\itrigray.jpg') #設定img路徑
        self.labelitrid.setPixmap(self.imitrid) #將 image 加入 label
        self.labelitrid.setGeometry(5,5,238,77)
        
        FonB = "font-size: 16pt; font: bold;font-family:微軟正黑體 ;"
        FonD = "background-color: #1F1F1F; color: white;font: 100 10pt \"Arial Narrow\""
        #分頁內來個浮動視窗-表格的
        self.dockexcel = QtWidgets.QDockWidget(self.widgetA22) #於分頁內建立浮動視窗
        self.dockexcel.setWindowTitle("  應變-電阻-應力表 ") #設定字型與格式
        self.dockexcel.setGeometry(100, 80, 550, 200) #注意size設定


        #loadcsv002 要def
        self.model = QtGui.QStandardItemModel(self.dockexcel) #浮動視窗內來個表格
        self.model.setHorizontalHeaderLabels(['Deformation_Ux(mm)', 'Resistance(Ω)', 'Max. Equivalent Stress(MPa)', 'Max. Principal Stress(MPa)'])
        self.LBLe014 = QLabel("POC Data", self.dockexcel)
        self.LBLe014.setStyleSheet(FonB)
        self.LBLe014.setGeometry(200,30, 350, 50)





        
        self.tableView = QtWidgets.QTableView(self.dockexcel)
        
        self.tableView.setGeometry(5, 80, 1350, 600)

        
        self.pushButton_014 = QtWidgets.QPushButton(self.dockexcel)
        self.pushButton_014.setGeometry(QtCore.QRect(5, 30, 45, 35))
        self.pushButton_014.setObjectName("pushButton_014")
        self.pushButton_014.setStyleSheet("background-color: #1F1F1F; color: white;font: 100 10pt \"Arial Narrow\"")
        self.pushButton_014.setText("")
       # self.pushButton_014.setFont(QFont('Arial', 5))
        self.pushButton_014.setStyleSheet("QPushButton{color:white}"
                                  "QPushButton:hover{color:blue}"
                                  "QPushButton{background-image : url(/FHEUI/fig/max1.png)}"
                                  "QPushButton{background-color:#1E1E1E}"
                                  "QPushButton:hover{background-image:url(/FHEUI/fig/max2.png)}"
                                  "QPushButton{border:1px}"
                                  "QPushButton{border-radius:2px}"
                                  "QPushButton{font: 10pt} "
                                  "QPushButton{padding:2px 4px}")  
        self.pushButton_014.clicked.connect(self.dockexcel.showMaximized) 

#####開啟結果檔
        self.pushButtonLoad014 = QtWidgets.QPushButton("開啟結果檔",self.dockexcel,clicked=self.on_pushButtonLoad_clicked13)
        self.pushButtonLoad014.setGeometry(600, 30, 100, 35)
    #    self.tableViewA13.horizontalHeader().setStretchLastSection(True)
    #    self.tableViewA13.setColumnCount(5)              
        self.pushButtonLoad014.setStyleSheet(FonD)
        self.pushButtonWrite014 = QtWidgets.QPushButton("儲存結果檔",self.dockexcel,
           clicked=self.on_pushButtonWrite_clicked)
        self.pushButtonWrite014.setGeometry(750, 30, 100, 35) 
        self.pushButtonWrite014.setStyleSheet(FonD)
        
        FonC = "font-size: 8pt; font: bold;font-family:微軟正黑體 ;text-decoration: underline;"
        FileName015 ="POC1_Structral-Electric_Results_CSV.csv"
        self.LBLe015 = QLabel(FileName015, self.dockexcel)
        self.LBLe015.setStyleSheet(FonC)
        self.LBLe015.setGeometry(900,30, 350, 50)

        
        
        self.loadCsv014()
        self.tableView.setModel(self.model)
        
        self.tableView.setColumnWidth(0,250)
        self.tableView.setColumnWidth(1,250)
        self.tableView.setColumnWidth(2,250)
        self.tableView.setColumnWidth(3,250)

        #load csv button
 
#########################################################################################
        self.pushButtonLoad22 = QtWidgets.QPushButton(" ",self.widgetA22,clicked=self.on_pushButtonLoad_clicked13)
        self.pushButtonLoad22.setStyleSheet("QPushButton{color:white}"
                                  "QPushButton:hover{color:blue}"
                                  "QPushButton{background-image : url(/FHEUI/fig/itrilogo7575.png)}"
                                  "QPushButton{background-color:#1E1E1E}"
                                  "QPushButton:hover{background-image:url(/FHEUI/fig/itrilogohover2.jpg)}"
                                  "QPushButton{border:1px}"
                                  "QPushButton{border-radius:2px}"
                                  "QPushButton{font: 10pt} "
                                  "QPushButton{padding:2px 4px}")        
        
        
        self.pushButtonLoad22.setMinimumHeight(80)
        self.pushButtonLoad22.setGeometry(0,100,80,80)
        self.pushButtonLoad22.setToolTip('POC1模擬結果') 
#########################################################################################        
        self.pushButtonWrite = QtWidgets.QPushButton("儲存結果檔",self.widgetA22,clicked=self.on_pushButtonWrite_clicked)
      
        self.pushButtonWrite.setStyleSheet("QPushButton{color:white}"
                                  "QPushButton:hover{color:yellow}"
                                  "QPushButton{background-color:#1E1E1E}"
                                  "QPushButton{border:1px}"
                                  "QPushButton{border-radius:2px}"
                                  "QPushButton{font: 10pt} "
                                  "QPushButton{padding:2px 4px}")        
    
        
        self.pushButtonWrite.setMinimumHeight(80)
        self.pushButtonWrite.setGeometry(0,180,80,80)
        self.pushButtonWrite.setToolTip('儲存新結果') 
######################################################################################### 
        self.pushButtonMV = QtWidgets.QPushButton("模擬結果檔",self.widgetA22,clicked=self.MVplayer001)
      
        self.pushButtonMV.setStyleSheet("QPushButton{color:white}"
                                  "QPushButton:hover{color:yellow}"
                                  "QPushButton{background-color:#1E1E1E}"
                                  "QPushButton{border:1px}"
                                  "QPushButton{border-radius:2px}"
                                  "QPushButton{padding:2px 4px}"
                                  "QPushButton{font: 10pt} ")        
        
        
        self.pushButtonMV.setMinimumHeight(80)
        self.pushButtonMV.setGeometry(0,260,80,80)
        self.pushButtonMV.setToolTip('POC1模擬影片') 
######################################################################################### 


        self.dockexcel2 = QtWidgets.QDockWidget(self.widgetA22) #於分頁內建立浮動視窗
        self.dockexcel2.setWindowTitle("應變-電阻關係圖 ") #設定字型與格式
        self.dockexcel2.setGeometry(100, 280, 550, 350) #注意size設定

        self.pushButton_015 = QtWidgets.QPushButton(self.dockexcel2)
        self.pushButton_015.setGeometry(QtCore.QRect(5, 30, 45, 35))
        self.pushButton_015.setObjectName("pushButton_015")
        self.pushButton_015.setStyleSheet("background-color: #1F1F1F; color: white;font: 100 10pt \"Arial Narrow\"")
        self.pushButton_015.setText("")
       # self.pushButton_014.setFont(QFont('Arial', 5))
        self.pushButton_015.setStyleSheet("QPushButton{color:white}"
                                  "QPushButton:hover{color:blue}"
                                  "QPushButton{background-image : url(/FHEUI/fig/max1.png)}"
                                  "QPushButton{background-color:#1E1E1E}"
                                  "QPushButton:hover{background-image:url(/FHEUI/fig/max2.png)}"
                                  "QPushButton{border:1px}"
                                  "QPushButton{border-radius:2px}"
                                  "QPushButton{font: 10pt} "
                                  "QPushButton{padding:2px 4px}")  
        self.pushButton_015.clicked.connect(self.dockexcel2.showMaximized)
        
        
        
        
        self.graphWidget = pg.PlotWidget(self.dockexcel2)
        self.graphWidget.setGeometry(5,80,550,350)

        FonB = "font-size: 16pt; font: bold;font-family:微軟正黑體 ;"
        self.LBLeZ014 = QLabel("POC1 應變-電阻關係圖", self.dockexcel2)
        self.LBLeZ014.setStyleSheet(FonB)
        self.LBLeZ014.setGeometry(200,30, 350, 50)

       # self.graphWidget.resize(400,300)  
        t = []
        s = []
        hour = []
        temperature = []

        with open('d:\\FHEUI\\Project\\POC1\\Data\\POC1_Structral-Electric_Results_CSV.csv', "r",encoding='utf-8-sig') as csvDataFile: 
            csvReader = csv.reader(csvDataFile)
            for row in csvReader:
                t.append(row[0])
                s.append(row[1])
  
        for i in range(0, len(t)): 
            t[i] = float(t[i])
        for i in range(0, len(s)): 
            s[i] = float(s[i]) 

        maxValue = np.amax(s)
        minValue = np.amin(s)
        print(maxValue)
        print(minValue)


        #Add Background colour to white
        #self.graphWidget.setBackground('#bbccaa')
        self.graphWidget.setBackground('#1E1E1E')
        # Add Title

        self.graphWidget.setTitle("Strain-Resistance Correlation", color="w", size="15pt")
        # Add Axis Labels

        
        
        styles = {"color": "white", "font-size": "15px"}
        self.graphWidget.setLabel("left", "Resistance (Ω)", **styles)
        self.graphWidget.setLabel("bottom", "Displacement (mm)", **styles)
        #Add legend
        self.graphWidget.addLegend()
        #Add grid
        self.graphWidget.showGrid(x=False, y=False)
        #Set Range
        self.graphWidget.setXRange(0, 20, padding=0)
        self.graphWidget.setYRange(0, 10, padding=0)

        #pen = pg.mkPen(color=(0, 0, 0))
        pen = pg.mkPen(color=(255, 255, 255))
        self.graphWidget.plot(t, s, name="___L1",  pen=pen, symbol='+', symbolSize=10, symbolBrush=('w'), font = '微軟正黑體')


        self.pushButtonLoad017 = QtWidgets.QPushButton("開啟結果檔",self.dockexcel2,clicked=self.plotPOC)
        self.pushButtonLoad017.setGeometry(600, 30, 100, 35)
    #    self.tableViewA13.horizontalHeader().setStretchLastSection(True)
    #    self.tableViewA13.setColumnCount(5)              
        self.pushButtonLoad017.setStyleSheet(FonD)




        #分頁內來個浮動視窗-圖的
        self.dock = QtWidgets.QDockWidget(self.widgetA22) #於分頁內建立漂浮視窗
        self.dock.setWindowTitle("POC1應力分布圖 ") #設定字型與格式
        self.dock.setGeometry(660,80,640,600) #注意size設定
        self.dock.setMaximumSize(QtCore.QSize(1360,700))

        self.pushButton_022 = QtWidgets.QPushButton(self.dock)
        self.pushButton_022.setGeometry(QtCore.QRect(20, 25, 45, 35))
        self.pushButton_022.setObjectName("pushButton_022")
       # self.pushButton_022.setStyleSheet("background-color: #1F1F1F; color: white;font: 100 10pt \"Arial Narrow\"")
        self.pushButton_022.setText("")
        self.pushButton_022.setStyleSheet("QPushButton{color:white}"
                                  "QPushButton:hover{color:blue}"
                                  "QPushButton{background-image : url(/FHEUI/fig/max1.png)}"
                                  "QPushButton{background-color:#1E1E1E}"
                                  "QPushButton:hover{background-image:url(/FHEUI/fig/max2.png)}"
                                  "QPushButton{border:1px}"
                                  "QPushButton{border-radius:2px}"
                                  "QPushButton{font: 10pt} "
                                  "QPushButton{padding:2px 4px}") 






        self.pushButton_022.clicked.connect(self.dock.showMaximized)


        self.pushButtonLoadz017 = QtWidgets.QPushButton("開啟結果檔",self.dock,clicked=self.ImgPOC)
        self.pushButtonLoadz017.setGeometry(130, 25, 100, 35)
    #    self.tableViewA13.horizontalHeader().setStretchLastSection(True)
    #    self.tableViewA13.setColumnCount(5)              
        self.pushButtonLoadz017.setStyleSheet(FonD)

        FonB = "font-size: 16pt; font: bold;font-family:微軟正黑體 ;"
        self.LBLeZ022 = QLabel("POC1 可拉伸線路應力分布圖", self.dock)
        self.LBLeZ022.setStyleSheet(FonB)
        self.LBLeZ022.setGeometry(240,15, 300, 50)



        hbox = QHBoxLayout (self.dock)
        lbl = QLabel (self.dock, alignment=Qt.AlignCenter)

        self.pixmap = QPixmap ("d:\\FHEUI\\Project\\POC1\\Image\\POC1-S-1mm.jpg")  
      #  lbl.setPixmap (self.pixmap)  
      # 
       
        lbl.setPixmap(self.pixmap.scaled(self.pixmap.width(), self.pixmap.height(), QtCore.Qt.KeepAspectRatio))
        lbl.setGeometry(QtCore.QRect(20,70,800,700))
        lbl.setScaledContents (True)
        hbox.addWidget (lbl,alignment=Qt.AlignCenter)  
        self.dock.setLayout (hbox)

################ MV
############################################
        self.mediaPlayer = QMediaPlayer(None, QMediaPlayer.VideoSurface)

        videoWidget = QVideoWidget(self.dock)
        videoWidget.setGeometry(830, 70, 500, 400)
      #  self.playButton = QPushButton()

        self.playButton = QPushButton(self.dock)
        self.playButton.setGeometry(830, 480, 50, 50)


        self.playButton.setEnabled(False)
        self.playButton.setIcon(self.style().standardIcon(QStyle.SP_MediaPlay))
        
        self.mediaPlayer.setMedia(QMediaContent(QUrl.fromLocalFile("d:\\FHEUI\\Project\\POC1\\Video\\POC1-S-1mm.mp4")))
        self.playButton.setEnabled(True)
        self.playButton.clicked.connect(self.play)
        
        self.positionSlider = QSlider(Qt.Horizontal)
        
        self.positionSlider.setRange(0, 0)
        self.positionSlider.sliderMoved.connect(self.setPosition)

        self.errorLabel = QLabel()
        self.errorLabel.setSizePolicy(QSizePolicy.Preferred,
                QSizePolicy.Maximum)

        self.positionSlider.setGeometry(QtCore.QRect(885, 480, 445, 50))
        
        hbox.addWidget(self.positionSlider)    
        self.dock.setLayout(hbox)
        
        
        self.mediaPlayer.setVideoOutput(videoWidget)
        self.mediaPlayer.stateChanged.connect(self.mediaStateChanged)
        self.mediaPlayer.positionChanged.connect(self.positionChanged)
        self.mediaPlayer.durationChanged.connect(self.durationChanged)
        self.mediaPlayer.error.connect(self.handleError)
        















       

 


        


        #################################
        #TAB9
        FonB = "font-size: 20pt; font: bold;font-family:微軟正黑體 ;"
        self.widgetA9=QtWidgets.QWidget()
       
        tab_index9 = self.qtabwidget.addTab(self.widgetA9, ' 分析記錄檔 ')
        
        self.qtabwidget.setTabIcon(tab_index9, QtGui.QIcon('d:\\FHEUI\\fig\\itri-circle-cropped.png'))
        self.qtabwidget.setIconSize(QtCore.QSize(35, 35)) 
     
        self.LBLh00 = QLabel("分析記錄檔", self.widgetA9)
        self.LBLh00.setStyleSheet(FonB)
        self.LBLh00.setGeometry(300,25,300, 40)


        buttongha0 = QPushButton(" 開啟記錄檔 ", self.widgetA9) 
        buttongha0.setGeometry(30, 82, 200, 50)
        buttongha0.setStyleSheet("QPushButton{background-image : url(/FHEUI/fig/itrilogo7575.png);border-radius: 15px;  border: 2px groove gray; border-style: outset;}""QPushButton:hover{background-image:url(/FHEUI/fig/itrilogohover.png)}""QPushButton:pressed{background-color:rgb(85, 170, 255); border-style: inset; }")
        buttongha0.clicked.connect(self.on_pushButtonLoadtxt_clicked)
        
        buttongha1 = QPushButton(" 另存記錄檔 ", self.widgetA9) 
        buttongha1.setGeometry(240, 82, 200, 50)
        buttongha1.setStyleSheet("QPushButton{background-image : url(/FHEUI/fig/itrilogo7575.png);border-radius: 15px;  border: 2px groove gray; border-style: outset;}""QPushButton:hover{background-image:url(/FHEUI/fig/itrilogohover.png)}""QPushButton:pressed{background-color:rgb(85, 170, 255); border-style: inset; }")
        buttongha1.clicked.connect(self.on_pushButtonNewtxt_clicked)

        buttongha2 = QPushButton("清空", self.widgetA9) 
        buttongha2.setGeometry(450, 82, 50, 50)
        buttongha2.setStyleSheet("QPushButton{background-image : url(/FHEUI/fig/itrilogo7575.png);border-radius: 15px;  border: 2px groove gray; border-style: outset;}""QPushButton:hover{background-image:url(/FHEUI/fig/itrilogohover.png)}""QPushButton:pressed{background-color:rgb(85, 170, 255); border-style: inset; }")
        buttongha2.clicked.connect(self.on_pushButtonCleartxt_clicked)
        
        self.LBLh99 = QLabel(" CHECK ", self.widgetA9)
        self.LBLh99.setStyleSheet("font-size: 12pt; font-family: Arial;background-color:rgb(85, 170, 255);color:white;border-radius: 5px; text-align:center")
        self.LBLh99.setAlignment(QtCore.Qt.AlignCenter)
        self.LBLh99.setGeometry(1250, 515, 75, 30)
        
        buttongh0 = QPushButton("   ", self.widgetA9) 
        buttongh0.setGeometry(1240, 550, 100, 45)
        buttongh0.setStyleSheet("QPushButton{background-image : url(/FHEUI/fig/itrilogo7575.png);border-radius: 15px;  border: 2px groove gray; border-style: outset;}""QPushButton:hover{background-image:url(/FHEUI/fig/itrilogohover.png)}""QPushButton:pressed{background-color:rgb(85, 170, 255); border-style: inset; }")
        buttongh0.clicked.connect(self.changetab9)
        
        self.labelitrih = QLabel(self.widgetA9)
        self.imitrih = QPixmap('d:\\FHEUI\\fig\\itrigray.jpg')
        self.labelitrih.setPixmap(self.imitrih) 
        self.labelitrih.setGeometry(5,5,238,77)

        self.createGridGroupBox()
       # self.creatVboxGroupBox()
        self.creatFormGroupBox()
        mainLayout = QVBoxLayout(self.widgetA9)
        hboxLayout = QHBoxLayout(self.widgetA9)
        hboxLayout.addStretch()  
        hboxLayout.addWidget(self.gridGroupBox)
###        hboxLayout.addWidget(self.vboxGroupBox)
        mainLayout.addLayout(hboxLayout)
        mainLayout.addWidget(self.formGroupBox)
        self.setLayout(mainLayout)


################################# ################################# #################################

# Tab18 設定                       
        self.widgetA18=QtWidgets.QWidget()
       
        tab_index18 = self.qtabwidget.addTab(self.widgetA18, '  POC設計  ')
        
        self.qtabwidget.setTabIcon(tab_index18, QtGui.QIcon('d:\\FHEUI\\fig\\droptest-circle-cropped.png'))
        self.qtabwidget.setIconSize(QtCore.QSize(35, 35)) 
     
        

        self.LBLe018 = QLabel("POC設計", self.widgetA18)
        self.LBLe018.setStyleSheet(FonA)
        self.LBLe018.setGeometry(450,10, 550, 50)
        self.LBLe9918 = QLabel(" CHECK ", self.widgetA18)
        
        
        self.LBLe9918.setStyleSheet("font-size: 12pt; font-family: Arial;background-color:rgb(85, 170, 255);color:white;border-radius: 5px; text-align:center")
        self.LBLe9918.setAlignment(QtCore.Qt.AlignCenter)
     
     
        self.LBLe9918.setGeometry(1250, 515, 75, 30)
        
       
        buttone0018 = QPushButton(" NEXT ", self.widgetA18)
        buttone0018.setGeometry(1285, 550, 60, 45)
        buttone0018.setStyleSheet("QPushButton{background-image : url(/FHEUI/icon/forward1.png);border-radius: 12px;  border: 2px groove gray; border-style: outset;}""QPushButton:hover{background-image:url(/FHEUI/fig/itrilogohover.png)}""QPushButton:pressed{background-color:rgb(85, 170, 255);color:white; border-style: inset; }")
        buttone0018.clicked.connect(self.changetab6)

        buttone0118 = QPushButton(" BACK ", self.widgetA18) 
        buttone0118.setGeometry(1220,550, 60, 45)
        buttone0118.setStyleSheet("QPushButton{background-image : url(/FHEUI/icon/backward1.png);border-radius: 12px;  border: 2px groove gray; border-style: outset;}""QPushButton:hover{background-image:url(/FHEUI/fig/itrilogohover.png)}""QPushButton:pressed{background-color:rgb(85, 170, 255);color:white; border-style: inset; }")
        buttone0118.clicked.connect(self.changetab4)     
        
        
        
        
        
        
       


        self.indexe0018 = QLabel(self.widgetA18)
        self.ime0018 = QPixmap('d:\\FHEUI\\fig\\POCimage.JPG') 
        self.indexe0018.setPixmap(self.ime0018) 
        self.indexe0018.setGeometry(50,60,1100,600)   

        self.pushButton_e18 = QtWidgets.QPushButton(self.widgetA18)
        self.pushButton_e18.setGeometry(QtCore.QRect(1100, 50, 200, 60))
        self.pushButton_e18.setObjectName("pushButton_e18")
###         self.pushButton_e18.setStyleSheet("background-color: #F0F0F0; color: black;font: 100 28pt \"Arial Narrow\"")
        self.pushButton_e18.setText("Twin Builder")
        self.pushButton_e18.setFont(QFont('Arial', 7))
        self.pushButton_e18.setStyleSheet("border-radius: 5px;  border: 2px groove gray; border-style: outset;}""QPushButton:hover{background-image:url(/FHEUI/fig/itrilogohover.png)}""QPushButton:pressed{background-color:rgb(85, 170, 255);color:white; border-style: inset; }") 
        self.pushButton_e18.clicked.connect(self.Stepviewer) 

        self.labelitrie18 = QLabel(self.widgetA18)
        self.imitrie18 = QPixmap('d:\\FHEUI\\fig\\itrigray.jpg') #要確認  路徑
        self.labelitrie18.setPixmap(self.imitrie18) #將 image 加入 label
        self.labelitrie18.setGeometry(5,5,238,77)

# Tab19 設定                       
        self.widgetA19=QtWidgets.QWidget()
       
        tab_index19 = self.qtabwidget.addTab(self.widgetA19, '  POC系統模型  ')
        
        self.qtabwidget.setTabIcon(tab_index19, QtGui.QIcon('d:\\FHEUI\\fig\\droptest-circle-cropped.png'))
        self.qtabwidget.setIconSize(QtCore.QSize(35, 35)) 
     
        

        self.LBLe019 = QLabel("POC系統電路模型", self.widgetA19)
        self.LBLe019.setStyleSheet(FonA)
        self.LBLe019.setGeometry(450,10, 550, 50)
        self.LBLe9919 = QLabel(" CHECK ", self.widgetA19)
        
        
        self.LBLe9919.setStyleSheet("font-size: 12pt; font-family: Arial;background-color:rgb(85, 170, 255);color:white;border-radius: 5px; text-align:center")
        self.LBLe9919.setAlignment(QtCore.Qt.AlignCenter)
     
     
        self.LBLe9919.setGeometry(1250, 515, 75, 30)
        
       
        buttone0019 = QPushButton(" NEXT ", self.widgetA19)
        buttone0019.setGeometry(1285, 550, 60, 45)
        buttone0019.setStyleSheet("QPushButton{background-image : url(/FHEUI/icon/forward1.png);border-radius: 12px;  border: 2px groove gray; border-style: outset;}""QPushButton:hover{background-image:url(/FHEUI/fig/itrilogohover.png)}""QPushButton:pressed{background-color:rgb(85, 170, 255);color:white; border-style: inset; }")
        buttone0019.clicked.connect(self.changetab6)

        buttone0119 = QPushButton(" BACK ", self.widgetA19) 
        buttone0119.setGeometry(1220,550, 60, 45)
        buttone0119.setStyleSheet("QPushButton{background-image : url(/FHEUI/icon/backward1.png);border-radius: 12px;  border: 2px groove gray; border-style: outset;}""QPushButton:hover{background-image:url(/FHEUI/fig/itrilogohover.png)}""QPushButton:pressed{background-color:rgb(85, 170, 255);color:white; border-style: inset; }")
        buttone0119.clicked.connect(self.changetab4)     
        
        
        
        
        
        self.labelitrie19 = QLabel(self.widgetA19)
        self.imitrie19 = QPixmap('d:\\FHEUI\\fig\\itrigray.jpg') #要確認  路徑
        self.labelitrie19.setPixmap(self.imitrie19) #將 image 加入 label
        self.labelitrie19.setGeometry(5,5,238,77)
       



        self.indexe0019 = QLabel(self.widgetA19)
        self.ime0019 = QPixmap('d:\\FHEUI\\fig\\SYSmodeling.JPG') 
#self.indexe0019.setPixmap(self.ime0019) 
        self.indexe0019.setGeometry(300,55,800,600)         
        self.indexe0019.setPixmap(self.ime0019.scaled(800,600,
                Qt.KeepAspectRatio, Qt.SmoothTransformation)) 


        self.pushButton_e19 = QtWidgets.QPushButton(self.widgetA19)
        self.pushButton_e19.setGeometry(QtCore.QRect(1100, 50, 200, 60))
        self.pushButton_e19.setObjectName("pushButton_e19")
#        self.pushButton_e19.setStyleSheet("background-color: #F0F0F0; color: black;font: 100 28pt \"Arial Narrow\"")
        self.pushButton_e19.setText("Twin Builder")
        self.pushButton_e19.setStyleSheet("border-radius: 5px;  border: 2px groove gray; border-style: outset;}""QPushButton:hover{background-image:url(/FHEUI/fig/itrilogohover.png)}""QPushButton:pressed{background-color:rgb(85, 170, 255);color:white; border-style: inset; }")
        self.pushButton_e19.setFont(QFont('Arial', 7)) 
        self.pushButton_e19.clicked.connect(self.Stepviewer) 


        #TAB11
     #################################
        self.widgetA11=QtWidgets.QWidget()
       
        tab_index11 = self.qtabwidget.addTab(self.widgetA11, ' 分析3 ')
        
        self.qtabwidget.setTabIcon(tab_index11, QtGui.QIcon('d:\\FHEUI\\fig\\itri-circle-cropped.png'))
        self.qtabwidget.setIconSize(QtCore.QSize(35, 35)) 
     
       
       
        #url = 'D:/127.0.0.1.4582.htm'
        url = 'D:/FHEUI/Weebly.htm'
        
        self.browser = QWebEngineView(self.widgetA11)
        self.browser.setGeometry(5, 5, 1300, 650)
        self.browser.load(QUrl(url))
       # self.setCentralWidget(self.browser)

        controlLayoutA11 = QHBoxLayout()
    #    controlLayout.addStretch(1)
        controlLayoutA11.setContentsMargins(0, 0, 0, 0)
        controlLayoutA11.addWidget(self.browser)
    
        layoutA11 = QVBoxLayout()

        layoutA11.addLayout(controlLayoutA11)

        self.widgetA11.setLayout(layoutA11)







################################# ################################# #################################
        #TAB13
        FonB = "font-size: 16pt; font: bold;font-family:微軟正黑體 ;"
        self.widgetA13=QtWidgets.QWidget()
       
        tab_index13 = self.qtabwidget.addTab(self.widgetA13, ' POC_1 Results ')
        
        self.qtabwidget.setTabIcon(tab_index13, QtGui.QIcon('d:\\FHEUI\\fig\\itri-circle-cropped.png'))
        self.qtabwidget.setIconSize(QtCore.QSize(35, 35)) 
            
        
        self.model = QtGui.QStandardItemModel(self.widgetA13) 
        
        self.LBLe013 = QLabel("POC_1 Data", self.widgetA13)
        self.LBLe013.setStyleSheet(FonB)
        self.LBLe013.setGeometry(450,10, 550, 50)
        
        
        
        self.tableViewA13 = QTableView(self.widgetA13)
        self.tableViewA13.setGeometry(150, 80, 1000, 500)

        self.loadCsv013()
        self.tableViewA13.setModel(self.model)
        self.tableViewA13.setColumnWidth(0,250)
        self.tableViewA13.setColumnWidth(1,250)
        self.tableViewA13.setColumnWidth(2,250)
        self.tableViewA13.setColumnWidth(3,250)


        #self.tableViewA13 = QtWidgets.QTableView(self.widgetA13)


        self.tableViewA13.horizontalHeader().setStretchLastSection(True)
       
        self.pushButtonLoad = QtWidgets.QPushButton("開啟結果檔",self.widgetA13,
            clicked=self.on_pushButtonLoad_clicked)
        self.pushButtonLoad.setGeometry(10, 100, 100, 50)
    #    self.tableViewA13.horizontalHeader().setStretchLastSection(True)
    #    self.tableViewA13.setColumnCount(5)              




        self.pushButtonWrite = QtWidgets.QPushButton("儲存結果檔",self.widgetA13,
           clicked=self.on_pushButtonWrite_clicked)
        self.pushButtonWrite.setGeometry(10, 250, 100, 50) 
      #  layoutVertical = QtWidgets.QVBoxLayout(self.widgetA12)
       # 
      #  layoutVertical.addWidget(self.tableView)
      #  layoutVertical.addWidget(self.pushButtonLoad)
      #  layoutVertical.addWidget(self.pushButtonWrite)
       # self.setLayout(layoutVertical)

        self.pushButtonWrite = QtWidgets.QPushButton("模擬動畫檔",self.widgetA13,
           clicked=self.MVplayer001)
        self.pushButtonWrite.setGeometry(10, 400, 100, 50)

 

        self.qtabwidget.addTab(None, "No Widget")
        ### Tab 固定不移關閉
     #   self.qtabwidget.setTabsClosable(True)  
        self.qtabwidget.setTabsClosable(False) 
        self.qtabwidget.tabCloseRequested.connect(self.qtabwidget_tabcloserequested)
        ### 初始 Tab 形狀 
       # self.qtabwidget.setTabShape(QtWidgets.QTabWidget.Triangular)
        self.qtabwidget.setTabShape(QtWidgets.QTabWidget.Rounded)
        ### Tab 位置 
        #self.qtabwidget.setTabPosition(QtWidgets.QTabWidget.East)
        self.qtabwidget.setTabPosition(QtWidgets.QTabWidget.North)
        #self.qtabwidget.setTabPosition(QtWidgets.QTabWidget.South)
        #self.qtabwidget.setTabPosition(QtWidgets.QTabWidget.West)   
        #self.qtabwidget.setTabEnabled(0, False) 
        self.qtabwidget.setTabEnabled(2, True)   # enable tab       
        self.qtabwidget.setTabEnabled(1, True)   # enable tab
        self.qtabwidget.setTabEnabled(0, False)  # disable tab         
        self.qtabwidget.currentChanged.connect(self.qtabwidget_currentchanged)
       
        #設定背景顏色
        #self.qtabwidget.setStyleSheet("background-color: #3CAAF8 ; color: black;font-size: 12pt \"Arial Narrow\"")
        #self.qtabwidget.setStyleSheet("background-color: #1E1E1E ; color: black;font-size: 12pt \"標楷體\"")
        self.qtabwidget.setStyleSheet("background-color:  #F0F0F0 ; color: black;font-size: 12pt \"微軟正黑體\"")
        
        #Tab 按下時改變背景顏色
        stylesheet = """ 
        QTabBar::tab:selected {background: gray;}
        QTabWidget>QWidget>QWidget{background: gray;}
        """
        
        self.statusBar().show()
       
        timeStamp = int(time.time())
        if timeStamp%60==0: 
            timeStamp = int(time.time())
            timeArray = time.localtime(timeStamp)
            otherStyleTime = time.strftime('%Y-%m-%d', timeArray)
            self.statusBar().showMessage('FHE Designed by ITRI.   '+ otherStyleTime)         
        else:
            timeStamp = int(time.time()) 
            timeArray = time.localtime(timeStamp)
            otherStyleTime = time.strftime('%Y-%m-%d', timeArray)
            self.statusBar().showMessage('FHE Designed by ITRI.   '+ otherStyleTime)
        
        self.backend = BackendThread()
        self.backend.update_date.connect(self.handleDisplay)
        self.thread = QThread()
        self.backend.moveToThread(self.thread)
        self.thread.started.connect(self.backend.run)
        self.thread.start()


        
        self.setStyleSheet(stylesheet)
        
        
        self.setCentralWidget(self.qtabwidget)


        #QtCore.QMetaObject.connectSlotsByName(self)
        
        application.aboutToQuit.connect(self.CLOSE5)





        
        self.showMaximized() 





    def on_clicked(self, index):
        self.LBLea16.setText("") 
        path = self.dirModel.fileInfo(index).absoluteFilePath()
        self.listview.setRootIndex(self.fileModel.setRootPath(path))
        print(path)
        pathe016 = '"' + path + '"'
        #print(FileName016)
        
        FonC = "font-size: 12pt; font: bold;font-family:微軟正黑體 ;text-decoration: underline;"
       # self.LBLe016 = QLabel('"' + fileName + '"', self.dockexcel)
       # self.LBLea16 = QLabel("", self.itemsFile)

        self.LBLea16.setText(path)
      # self.LBLea16 = QLabel(path, self.itemsFile)
        
        #  self.LBLe016 = QLabel("999 POC5_Ball_Drop_Results_CSV.csv", self.dockexcel)
        self.LBLea16.setStyleSheet(FonC)
        self.LBLea16.setGeometry(660,30,600,50)                
        self.LBLea16.show()

    def on_clicked002(self, index):
        subprocess.Popen([r"C:\\Program Files\\VCG\\MeshLab\\meshlab.exe"])
    def on_clicked003(self,index):
 #       print(index)
 #       inf0003=str(index)
 #       print(inf0003)
        path003 = self.dirModel.fileInfo(index).absoluteFilePath()
        print(path003)
        self.apath003 = QLineEdit()
        self.apath003.setText(path003)
      #  return index
       # os.system( path003 )     
                  

    def MVplayer001(self,text):
        os.system("D:\\FHEUI\\videoplayer001.py")

    def loadCsv(self, fileName):
        self.model.clear()
        with open(fileName, "r", encoding='utf-8') as fileInput:                    
            for row in csv.reader(fileInput):
                items = [
                    QtGui.QStandardItem(field)
                    for field in row
                ]
                
                
                self.model.appendRow(items)
        print(items)

    
    def loadCsv13(self, fileName):
       
  
        self.model.clear()
        with open(fileName, "r", encoding='utf-8') as fileInput:                    
            for row in csv.reader(fileInput):
                items = [
                    QtGui.QStandardItem(field)
                    for field in row
                ]
                
                self.model.appendRow(items)

        
        self.tableView.setColumnWidth(0,250)
        self.tableView.setColumnWidth(1,250)
        self.tableView.setColumnWidth(2,250)
        self.tableView.setColumnWidth(3,250)
        self.tableView.setModel(self.model)
      #  print(items)
       
               

    def loadCsv001(self):
        
        self.model.clear()
        with open("D:\\test003.csv", "r",encoding='utf-8') as fileInput:                    
           # for row in csv.reader(fileInput):
           # for row in np.array(list(csv.reader(fileInput))):    
            for row in list(csv.reader(fileInput)):     
                items = [
                    QtGui.QStandardItem(field)
                          
                    for field in row
                ]
         #       items1=TableModel(items)
         #       self.model.appendRow(items1)
                #print(items)
                self.model.appendRow(items)
    
    def loadCsv013(self):
        
        self.model.clear()
        with open("D:\\FHEUI\\ANSYS\\POC1_Structral-Electric_Results.csv", "r",encoding='utf-8') as fileInput:                    
           # for row in csv.reader(fileInput):
           # for row in np.array(list(csv.reader(fileInput))):    
            for row in list(csv.reader(fileInput)):     
                items = [
                    QtGui.QStandardItem(field)
                          
                    for field in row
                ]
         #       items1=TableModel(items)
         #       self.model.appendRow(items1)
                #print(items)
                self.model.appendRow(items)
        FonB = "font-size: 16pt; font: bold;font-family:微軟正黑體 ;"
        self.LBLe013 = QLabel("POC_1 應變/應力/電性模擬結果", self.widgetA13)
        self.LBLe013.setStyleSheet(FonB)
        self.LBLe013.setGeometry(450,10, 550, 50)

    def loadCsv014(self):
        
        self.model.clear()
        with open("D:\\FHEUI\\Project\\POC1\\Data\\POC1_Structral-Electric_Results_CSV.csv", "r",encoding='utf-8') as fileInput:                    
           # for row in csv.reader(fileInput):
           # for row in np.array(list(csv.reader(fileInput))):
            rows=csv.reader(fileInput)
            headers = next(rows)    
            for row in list(csv.reader(fileInput)):
                  
                items = [
                    QtGui.QStandardItem(field)
                          
                    for field in row
                ]
         #       items1=TableModel(items)
         #       self.model.appendRow(items1)
                #print(items)
                
                self.model.appendRow(items)

        self.model.setHorizontalHeaderLabels(['Deformation_Ux(mm)', 'Resistance(Ω)', 'Max. Equivalent Stress(MPa)', 'Max. Principal Stress(MPa)'])        
            
        
        
        FonB = "font-size: 16pt; font: bold;font-family:微軟正黑體 ;"
        FonD = "background-color: #1F1F1F; color: white;font: 100 10pt \"Arial Narrow\""
        self.pushButton_014 = QtWidgets.QPushButton(self.dockexcel)
        self.pushButton_014.setGeometry(QtCore.QRect(5, 30, 45, 35))
        self.pushButton_014.setObjectName("pushButton_014")
        self.pushButton_014.setStyleSheet("background-color: #1F1F1F; color: white;font: 100 10pt \"Arial Narrow\"")
        self.pushButton_014.setText("")
       # self.pushButton_014.setFont(QFont('Arial', 5))
        self.pushButton_014.setStyleSheet("QPushButton{color:white}"
                                  "QPushButton:hover{color:blue}"
                                  "QPushButton{background-image : url(/FHEUI/fig/max1.png)}"
                                  "QPushButton{background-color:#1E1E1E}"
                                  "QPushButton:hover{background-image:url(/FHEUI/fig/max2.png)}"
                                  "QPushButton{border:1px}"
                                  "QPushButton{border-radius:2px}"
                                  "QPushButton{font: 10pt} "
                                  "QPushButton{padding:2px 4px}") 


        self.pushButton_014.clicked.connect(self.dockexcel.showMaximized)

        self.LBLe014 = QLabel("POC1 應變-電性-應力模擬結果", self.dockexcel)
        self.LBLe014.setStyleSheet(FonB)
        self.LBLe014.setGeometry(200,30, 350, 50)

        FonC = "font-size: 10pt; font: bold;font-family:微軟正黑體 ;"
        
        


        self.pushButtonLoad014 = QtWidgets.QPushButton("開啟結果檔",self.dockexcel,
            clicked=self.on_pushButtonLoad_clicked13)
        self.pushButtonLoad014.setStyleSheet(FonD)
        self.pushButtonLoad014.setGeometry(600, 30, 100, 35)
    #    self.tableViewA13.horizontalHeader().setStretchLastSection(True)
    #    self.tableViewA13.setColumnCount(5)              

        self.pushButtonWrite014 = QtWidgets.QPushButton("儲存結果檔",self.dockexcel,
           clicked=self.on_pushButtonWrite_clicked)
        self.pushButtonWrite014.setStyleSheet(FonD)
        self.pushButtonWrite014.setGeometry(750, 30, 100, 35) 




    def loadCsv015(self):

        data_path = 'd:\\test003.csv'
        with open(data_path, 'r',encoding='utf-8') as f:
            reader = csv.reader(f, delimiter=',')
            headers = next(reader)
            data = np.array(list(reader)).astype(float)
         
            print(data)
        #結果相同
       # print(list(data)) 
        self.model = TableModel(data)
        self.tableView.setModel(self.model)

       # self.setCentralWidget(self.tableView)
        self.tableView.show()



    def loadCsv002(self):
        self.model.clear()
        with open("D:\\test003.csv", "r",encoding='utf-8') as fileInput:                    
            for row in list(csv.reader(fileInput)):     
                items = [
                    QtGui.QStandardItem(field)
                    for field in row
                ]
                self.model.appendRow(items)
                
 
    def writeCsv(self, fileName):
        with open(fileName, "w",encoding='utf-8') as fileOutput:                   
            writer = csv.writer(fileOutput, lineterminator='\n')  
            print('rowCount->', self.model.rowCount())
            for rowNumber in range(self.model.rowCount()):
                fields = [
                    self.model.item(rowNumber, columnNumber).text()
                    for columnNumber in range(self.model.columnCount())
                ]
                print('fields->', fields)
                writer.writerow(fields)




    @QtCore.pyqtSlot()
    def on_pushButtonLoad_clicked(self):
        fileName, _ =  QtWidgets.QFileDialog.getOpenFileName(self, self.tr("  開啟分析結果檔   "), 
            QtCore.QDir.currentPath(), self.tr("CSV Files (*.csv)"))
        if fileName:
            self.loadCsv(fileName)

    def on_pushButtonLoadtxt_clicked(self):

        
        self.nameLineEdit.setText(" ")
        self.emitLineEdit.setText(" ")
        self.timeLineEdit.setText(" ")
        self.performanceEditor.setText(" ")
        self.planEditor.setText(" ")

        fileName, _ =  QtWidgets.QFileDialog.getOpenFileName(self, self.tr("  開啟記錄檔   "), 
            "D:\\FHEUI\\rec", self.tr("Rec Files (*.txt)"))
##        if fileName:
#        if fileName ==" ":
#            print("Reselect")
##       else:
#            os.system(fileName)        
        
        self.gridGroupBox = QGroupBox("記錄",self.widgetA9)
        lines=[]

        file1 = open(fileName,"r",encoding='utf-8') 
        lines = file1.readlines()
        layout = QGridLayout()

        line000=lines[0]
        line001=lines[1]
        line002=lines[2]
        line003=lines[3]
        line004=lines[4]
        line005=lines[5]



        self.nameLineEdit.setText(line000)

        self.emitLineEdit.setText(line001)

        self.timeLineEdit.setText(line002)



        self.performanceEditor.setText(lines[3])
           
        #txtoutput=line004+"\n"+line005
        self.txtoutput1=line004+line005
        self.planEditor.setText(self.txtoutput1)


        self.widgetA9.show()

    def on_pushButtonNewtxt_clicked(self):

        
        self.nameLineEdit.setText(" ")
        self.emitLineEdit.setText(" ")
        self.timeLineEdit.setText(" ")
        self.performanceEditor.setText(" ")
        self.planEditor.setText(" ")

        self.widgetA9.show()

    def on_pushButtonCleartxt_clicked(self):

        
        self.nameLineEdit.setText(" ")
        self.emitLineEdit.setText(" ")
        self.timeLineEdit.setText(" ")
        self.performanceEditor.setText(" ")
        self.planEditor.setText(" ")

        self.widgetA9.show()
 


    def creatVboxGroupBox(self):
       # self.vboxGroupBox = QGroupBox("Vbox layout",self.widgetA9)
        self.vboxGroupBox = QGroupBox("模擬結果",self.widgetA9)
        self.vboxGroupBox.setStyleSheet("font-size: 15pt; font-family: Arial;background-color:rgb(85, 170, 255);color:white;border-radius: 10px; text-align:center")
        self.layout = QVBoxLayout(self.vboxGroupBox)      
#####  PLOT 繪圖
        
        self.figure = plt.figure()
        self.canvas = FigureCanvas(self.figure)
        self.button_plot9 = QtWidgets.QPushButton("繪圖",self.vboxGroupBox)
        self.button_plot9.setStyleSheet("font-size: 12pt; font-family: Arial;background-color:rgb(85, 170, 255);color:white;border-radius: 10px; text-align:center")
        self.button_plot9.setGeometry(450,300, 150, 50)
      
        # 連接事件
        self.button_plot9.clicked.connect(self.plot_)
      
        # 設置佈局
     #   layout1 = QtWidgets.QVBoxLayout(self.layout)
       # layout.setGeometry(50,300,300,200)
        self.layout.addWidget(self.canvas)

        self.layout.addWidget(self.button_plot9)
        self.setLayout(self.layout)
       
        self.vboxGroupBox.setLayout(self.layout)
 


    def on_pushButtonLoad_clicked13(self,text):

        fileName, _ =  QtWidgets.QFileDialog.getOpenFileName(self, self.tr("  開啟分析結果檔   "),"D:\\FHEUI\\Project\\", self.tr("CSV Files (*.csv)"))
      
        if fileName:
            self.loadCsv13(fileName)

        
        self.model.setHorizontalHeaderLabels(['Deformation_Ux(mm)', 'Resistance(Ω)', 'Max. Equivalent Stress(MPa)', 'Max. Principal Stress(MPa)'])
#        self.tableViewA13.setModel(self.model)
         
        
#        self.tableViewA13.setColumnWidth(0,250)
#        self.tableViewA13.setColumnWidth(1,250)
#        self.tableViewA13.setColumnWidth(2,250)
#        self.tableViewA13.setColumnWidth(3,250) 

       

        
        FonD = "background-color: #1F1F1F; color: white;font: 100 10pt \"Arial Narrow\""
        self.pushButton_014 = QtWidgets.QPushButton(self.dockexcel)
        self.pushButton_014.setGeometry(QtCore.QRect(50, 30, 45, 35))
        self.pushButton_014.setObjectName("pushButton_014")
        self.pushButton_014.setStyleSheet("background-color: #1F1F1F; color: white;font: 100 10pt \"Arial Narrow\"")
        self.pushButton_014.setText("")
       # self.pushButton_014.setFont(QFont('Arial', 5)) 
        self.pushButton_014.setStyleSheet("QPushButton{color:white}"
                                  "QPushButton:hover{color:blue}"
                                  "QPushButton{background-image : url(/FHEUI/fig/max1.png)}"
                                  "QPushButton{background-color:#1E1E1E}"
                                  "QPushButton:hover{background-image:url(/FHEUI/fig/max2.png)}"
                                  "QPushButton{border:1px}"
                                  "QPushButton{border-radius:2px}"
                                  "QPushButton{font: 10pt} "
                                  "QPushButton{padding:2px 4px}")

        self.pushButton_014.clicked.connect(self.dockexcel.showMaximized) 

        self.pushButtonLoad014 = QtWidgets.QPushButton("開啟結果檔",self.dockexcel,clicked=self.on_pushButtonLoad_clicked13)
        self.pushButtonLoad014.setGeometry(600, 30, 100, 35)
        self.pushButtonLoad014.setStyleSheet(FonD)
        self.pushButtonWrite014 = QtWidgets.QPushButton("儲存結果檔",self.dockexcel,
           clicked=self.on_pushButtonWrite_clicked)
        self.pushButtonWrite014.setGeometry(750, 30, 100, 35) 
        self.pushButtonWrite014.setStyleSheet(FonD)
       
        FileName016 = '"' + fileName + '"'
        print(FileName016)
        
        FonC = "font-size: 8pt; font: bold;font-family:微軟正黑體 ;text-decoration: underline;"
       # self.LBLe016 = QLabel('"' + fileName + '"', self.dockexcel)
        self.LBLe016 = QLabel(fileName, self.dockexcel)
        
        #  self.LBLe016 = QLabel("999 POC5_Ball_Drop_Results_CSV.csv", self.dockexcel)
        self.LBLe016.setStyleSheet(FonC)
        self.LBLe016.setGeometry(900,30,400,50)                
        self.LBLe016.show()

    @QtCore.pyqtSlot()
    def on_pushButtonWrite_clicked(self):
        fileName, _ =  QtWidgets.QFileDialog.getSaveFileName(self, self.tr("   儲存分析結果檔"),"D:\\FHEUI\\Project\\", self.tr("CSV Files (*.csv)"))
        if fileName:
            self.writeCsv(fileName)



#center
    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def mousePressEvent(self, event):
        self.oldPos = event.globalPos()

    def mouseMoveEvent(self, event):
        delta = QPoint (event.globalPos() - self.oldPos)
        #print(delta)
        self.move(self.x() + delta.x(), self.y() + delta.y())
        self.oldPos = event.globalPos() 


    def layout_init(self):
        self.v_layout.addWidget(self.combobox_1)
        self.setLayout(self.v_layout)
    
    def combobox_init(self):
        self.combobox_1.addItem(self.choice)              # 4
        self.combobox_1.addItems(self.choice_list)        # 5
      #  self.combobox_1.currentIndexChanged.connect(lambda: self.on_combobox_func(self.combobox_1))   # 6
        self.combobox_1.setStyleSheet("background-color: #1E1E1E ; color: white;font-size: 12pt; font-family: Arial;")
        self.combobox_1.activated[str].connect(self.labellink001)
        
        self.combobox_2.addItem(self.choice002)              # 4
        self.combobox_2.addItems(self.choice_list002)        # 5
      #  self.combobox_1.currentIndexChanged.connect(lambda: self.on_combobox_func(self.combobox_1))   # 6
        self.combobox_2.setStyleSheet("background-color: #1E1E1E ; color: white;font-size: 12pt; font-family: Arial; ")   
        self.combobox_2.activated[str].connect(self.labellink002)
      
        self.combobox_3.addItem(self.choice003)              # 4
        self.combobox_3.addItems(self.choice_list003)        # 5
      #  self.combobox_1.currentIndexChanged.connect(lambda: self.on_combobox_func(self.combobox_1))   # 6
        self.combobox_3.setStyleSheet("background-color: #1E1E1E ; color: white;font-size: 12pt; font-family: Arial; ")   
        self.combobox_3.activated[str].connect(self.labellink005)  

        self.combobox_4.addItem(self.choice004)              # 4
        self.combobox_4.addItems(self.choice_list004)        # 5
      #  self.combobox_1.currentIndexChanged.connect(lambda: self.on_combobox_func(self.combobox_1))   # 6
        self.combobox_4.setStyleSheet("background-color: #1E1E1E ; color: white;font-size: 12pt; font-family: Arial; ")   
        self.combobox_4.activated[str].connect(self.labellink006)  
    
    def combobox8_init(self):
        self.combobox_f1.addItem(self.paraf01)              # 4
        self.combobox_f1.addItems(self.paraf01_list)        # 5
      #  self.combobox_1.currentIndexChanged.connect(lambda: self.on_combobox_func(self.combobox_1))   # 6
        self.combobox_f1.setStyleSheet("background-color: #1E1E1E ; color: white;font-size: 12pt; font-family: Arial;")
        self.combobox_f1.activated[str].connect(self.labellinkg01)

        self.combobox_f2.addItem(self.paraf02)              # 4
        self.combobox_f2.addItems(self.paraf02_list)        # 5
      #  self.combobox_1.currentIndexChanged.connect(lambda: self.on_combobox_func(self.combobox_1))   # 6
        self.combobox_f2.setStyleSheet("background-color: #1E1E1E ; color: white;font-size: 12pt; font-family: Arial;")
        self.combobox_f2.activated[str].connect(self.labellinkg02)

    def changetab1(self):
        self.qtabwidget.setCurrentIndex(1)
    def changetab2(self):
        self.qtabwidget.setCurrentIndex(2)
    def changetab3(self):
        self.qtabwidget.setCurrentIndex(3)
    def changetab4(self):
        self.qtabwidget.setCurrentIndex(4)
    def changetab5(self):
        self.qtabwidget.setCurrentIndex(5)
    def changetab6(self):
        self.qtabwidget.setCurrentIndex(6)
    def changetab7(self):
        self.qtabwidget.setCurrentIndex(7)
    def changetab8(self):
        self.qtabwidget.setCurrentIndex(8)
    def changetab9(self):
        self.qtabwidget.setCurrentIndex(9)
    def changetab22(self):
        self.qtabwidget.setCurrentIndex(14)
        

    def ALL001(self,text):
        os.system("D:\\FHEUI\\Comboclick004.py")
    def SIG001(self,text):
        os.system("D:\\FHEUI\\Signalclick001.py")        
    def ngSPICE(self,text):
        subprocess.Popen([r"D:\\FHEUI\\ngspice\\Spice64\\ngspice.exe"])
        os.system("D:\\FHEUI\\ngspice\\ng_commnad.txt")
    def ngSPICE2(self,text):
        subprocess.Popen([r"D:\\FHEUI\\ngspice\\Spice64\\ngspice.exe"])
        os.system("D:\\FHEUI\\ngspice\\ng_commnad2.txt")

    def TRACE001(self,text):
        os.system("D:\\FHEUI\\Traceclick001.py")
    
    def IMPACT001(self,text):
        os.system("D:\\FHEUI\\Impactclick001.py")

    def Stepviewer(self,text):      
        subprocess.Popen('"C:\\Program Files\\FreeCAD 0.18\\bin\\FreeCAD.exe" d:\\FHEUI\\MB_20200729-0935.step')

    def Linkviewer(self,text):      
        ur3 = 'https://www.google.com.tw'
        self.browser3.load(QUrl(ur3))

    def labellink003(self):
     #   self.label01 = QLabel(self.widgetA3)      
        self.im01 = QPixmap('d:\\FHEUI\\fig\\testvehicle.png') #要確認 Lena.png 路徑
        #self.im01 = QPixmap('d:\\FHEUI\\figitrilogo.png')
        self.label01.setPixmap(self.im01) #將 image 加入 label
    
    
    
    def labellink003_1(self):
      
            self.im05 = QPixmap('d:\\FHEUI\\fig\\electrode_Ag.jpg') #要確認 Lena.png 路徑
           # self.label05.setPixmap(self.im05) #將 image 加入 label
            self.label05.setPixmap(self.im05.scaled(200,300,  
                Qt.KeepAspectRatio, Qt.SmoothTransformation))

    def labellink003_2(self):
      
            self.im07 = QPixmap('d:\\FHEUI\\fig\\右腰.png') #要確認 Lena.png 路徑
            #self.label07.setPixmap(self.im07) #將 image 加入 label
            self.label07.setPixmap(self.im07.scaled(200,300,  
                Qt.KeepAspectRatio, Qt.SmoothTransformation))
    
    def labellink004(self):
      
            self.im03 = QPixmap('d:\\FHEUI\\fig\\pants001.png') #要確認 Lena.png 路徑
            self.label03.setPixmap(self.im03) #將 image 加入 labeldef labellink001(self,text):
            self.label03.setPixmap(self.im03.scaled(300,300,
                Qt.KeepAspectRatio, Qt.SmoothTransformation)) 
       
       
    def labellink001(self,text):   
       # self.labelc01 = QLabel(self)
      #  self.moviec01 = QMovie("d:\spin bike 431.gif")
      #  self.labelc01.setMovie(self.moviec01)
      #  self.labelc01.setGeometry(200,100,300,250) # 大小
      #  self.moviec01.start()
        txt= self.combobox_1.currentText()
        if txt=="智慧褲":
           # self.label01.setStyleSheet("border-radius: 10px;background-color:rgb(85, 170, 255);")
            self.im01 = QPixmap('d:\\FHEUI\\fig\\pants.jpg') #要確認 Lena.png 路徑
            self.label01.setPixmap(self.im01) #將 image 加入 label
            self.label01.setAlignment(Qt.AlignCenter)
        elif txt=="智慧護具": 
           # self.label01.setStyleSheet("border-radius: 10px;background-color:rgb(85, 170, 255);")
            self.im01 = QPixmap('d:\\FHEUI\\fig\\protector.jpg') #要確認 Lena.png 路徑
            self.label01.setPixmap(self.im01) #將 image 加入 label
           # self.label01.setStyleSheet("image: url(d:\\FHEUI\\fig\\itrilogo.png);border-radius: 10px")
            self.label01.setAlignment(Qt.AlignCenter)
        elif txt=="智慧袖套": 
          #  self.label01.setStyleSheet("border-radius: 10px;background-color:rgb(85, 170, 255);")
            self.im01 = QPixmap('d:\\FHEUI\\fig\\sleeve.jpg') #要確認 Lena.png 路徑
            self.label01.setPixmap(self.im01) #將 image 加入 label
            self.label01.setAlignment(Qt.AlignCenter)
        elif txt=="智慧衣": 
           # self.label01.setStyleSheet("border-radius: 10px;background-color:rgb(85, 170, 255);")
            self.im01 = QPixmap('d:\\FHEUI\\fig\\clothing1.jpg') #要確認 Lena.png 路徑
            self.label01.setPixmap(self.im01) #將 image 加入 label
            self.label01.setAlignment(Qt.AlignCenter)
    def labellink002(self,text):
      # self.labelc01 = QLabel(self)
      #  self.moviec01 = QMovie("d:\spin bike 431.gif")
      #  self.labelc01.setMovie(self.moviec01)
      #  self.labelc01.setGeometry(200,100,300,250) # 大小
      #  self.moviec01.start()
        txt= self.combobox_2.currentText()
        if txt=="股四頭肌":
           # self.label03.setStyleSheet("border-radius: 10px;background-color:rgb(85, 170, 255);")
            self.im03 = QPixmap('d:\\FHEUI\\fig\\frontleg.png') #要確認 Lena.png 路徑
            self.label03.setPixmap(self.im03) #將 image 加入 label
            self.label03.setPixmap(self.im03.scaled(300,300,
                Qt.KeepAspectRatio, Qt.SmoothTransformation)) 
        elif txt=="股二頭肌": 
          #  self.label03.setStyleSheet("border-radius: 10px;background-color:rgb(85, 170, 255);")
            self.im03 = QPixmap('d:\\FHEUI\\fig\\backleg.png') #要確認 Lena.png 路徑
            self.label03.setPixmap(self.im03) #將 image 加入 label
            self.label03.setPixmap(self.im03.scaled(300,300,
                Qt.KeepAspectRatio, Qt.SmoothTransformation))     
        elif txt=="臀大肌": 
         #   self.label03.setStyleSheet("border-radius: 10px;background-color:rgb(85, 170, 255);")
            self.im03 = QPixmap('d:\\FHEUI\\fig\\hip.png') #要確認 Lena.png 路徑
            self.label03.setPixmap(self.im03) #將 image 加入 label
            self.label03.setPixmap(self.im03.scaled(300,300,
                Qt.KeepAspectRatio, Qt.SmoothTransformation)) 
    
    def labellink005(self):
      
        txt= self.combobox_3.currentText()
        if txt=="銀膠":
            self.im05 = QPixmap('d:\\FHEUI\\fig\\electrode_Ag.jpg') #要確認 Lena.png 路徑
            self.label05.setPixmap(self.im05) #將 image 加入 label
            #self.label03.setScaledContents(1)
            self.label05.setPixmap(self.im05.scaled(200,300,
                Qt.KeepAspectRatio, Qt.SmoothTransformation))
        elif txt=="織物": 
            self.im05 = QPixmap('d:\\FHEUI\\fig\\electrode_t.jpg') #要確認 Lena.png 路徑
            self.label05.setPixmap(self.im05) #將 image 加入 label
            self.label05.setPixmap(self.im05.scaled(200,300,
                Qt.KeepAspectRatio, Qt.SmoothTransformation))
    def labellink006(self):
      
        txt= self.combobox_4.currentText()
        if txt=="右腰":
            self.im07 = QPixmap('d:\\FHEUI\\fig\\右腰.png') #要確認 Lena.png 路徑
            self.label07.setPixmap(self.im07) #將 image 加入 label
            #self.label03.setScaledContents(1)
            self.label07.setPixmap(self.im07.scaled(200,300,
                Qt.KeepAspectRatio, Qt.SmoothTransformation))
        elif txt=="左腰": 
            self.im07 = QPixmap('d:\\FHEUI\\fig\\左腰.png') #要確認 Lena.png 路徑
            self.label07.setPixmap(self.im07) #將 image 加入 label
            self.label07.setPixmap(self.im07.scaled(200,300,
                Qt.KeepAspectRatio, Qt.SmoothTransformation))
        elif txt=="右大腿前側": 
            self.im07 = QPixmap('d:\\FHEUI\\fig\\pants001R.png') #要確認 Lena.png 路徑
            self.label07.setPixmap(self.im07) #將 image 加入 label
        elif txt=="左大腿前側": 
            self.im07 = QPixmap('d:\\FHEUI\\fig\\pants001L.png') #要確認 Lena.png 路徑
            self.label07.setPixmap(self.im07) #將 image 加入 label

    def labellinkg01(self,text):   
        txtg00=self.e1g01.text()
        ag00=int(txtg00)
        txtg01= self.combobox_f1.currentText()
        ag01=int(txtg01)
        txtg02= self.combobox_f2.currentText()
        ag02=int(txtg02)
        txt=str(ag00+ag01+ag02)
        self.LBLg01.setText(txt)
        self.LBLg01.setStyleSheet("font-size: 12pt; font-family: Arial;background-color:rgb(85, 170, 255);color:white;border-radius: 10px; text-align:center")
        self.LBLg01.setAlignment(QtCore.Qt.AlignCenter)
        self.LBLg01.setGeometry(400, 140, 300, 200)
        print(txt)
    
    def labellinkg02(self,text): 
        txtg00=self.e1g01.text() 
        ag00=int(txtg00) 
        txtg01= self.combobox_f1.currentText()
        ag01=int(txtg01)
        txtg02= self.combobox_f2.currentText()
        ag02=int(txtg02)

        txt=str(ag00+ag01+ag02)
        #self.LBLg01 = QLabel(txt, self.widgetA8)
        self.LBLg01.setText(txt)
        self.LBLg01.setStyleSheet("font-size: 12pt; font-family: Arial;background-color:rgb(85, 170, 255);color:white;border-radius: 10px; text-align:center")
        self.LBLg01.setAlignment(QtCore.Qt.AlignCenter)
        self.LBLg01.setGeometry(400, 140, 300, 200)
       
        print(txt)
    
    
    def do_action001(self): 
       # txtg00= self.self.e1g99.text()
       # self.e1g99 = QLabel("XXX", self.widgetA8)
       ## self.e1g99.setText(txtg00) 
        ur3= self.e1f01.text()

        if str(ur3) == "":
            ur3=self.e1f01.setText('https://www.yahoo.com.tw')
            self.browser3.load(QUrl(ur3))
        else:
            ur3= self.e1f01.text()
            self.browser3.load(QUrl(ur3))

    def Linkviewer2(self,text):      
        ur3= self.e1f01.text()

        if str(ur3) == "":
            ur3=self.e1f01.setText('https://www.yahoo.com.tw')
            self.browser3.load(QUrl(ur3))
        else:
            ur3= self.e1f01.text()
            self.browser3.load(QUrl(ur3))


        
    def do_action(self): 
       # txtg00= self.self.e1g99.text()
       # self.e1g99 = QLabel("XXX", self.widgetA8)
       ## self.e1g99.setText(txtg00) 
         
        txtg00= self.e1g01.text()

        if str(txtg00) == "":
            self.e1g01.setText('0')
        
        else: 
            ag00=int(txtg00) 
            txtg01= self.combobox_f1.currentText()
            ag01=int(txtg01)
            txtg02= self.combobox_f2.currentText()
            ag02=int(txtg02)

            txt=str(ag00+ag01+ag02)
        #self.LBLg01 = QLabel(txt, self.widgetA8)
            self.LBLg01.setText(txt)
            self.LBLg01.setStyleSheet("font-size: 12pt; font-family: Arial;background-color:rgb(85, 170, 255);color:white;border-radius: 10px; text-align:center")
            self.LBLg01.setAlignment(QtCore.Qt.AlignCenter)
            self.LBLg01.setGeometry(400, 140, 300, 200)
            print(txt)      

    def calc01(self,text):
        txtg01= self.combobox_f1.currentText()
        ag01=int(txtg01)
        txtg02= self.combobox_f2.currentText()
        ag02=int(txtg02)
        self.txt999=str(ag01+ag02)

    def changeTabPos(self, index):
        switcher = {
            0: QtWidgets.QTabWidget.North,
            1: QtWidgets.QTabWidget.South,
            2: QtWidgets.QTabWidget.West,
            3: QtWidgets.QTabWidget.East
        }
        self.qtabwidget.setTabPosition(switcher.get(index))
        
    
    def Frameless(self):
        flags = QtCore.Qt.WindowFlags(QtCore.Qt.FramelessWindowHint | QtCore.Qt.WindowStaysOnTopHint)
        self.setWindowFlags(flags)
        self.showMaximized()
        


    def Frameshow(self):
        flags2 = QtCore.Qt.WindowFlags(QtCore.Qt.WindowStaysOnTopHint)
        self.setWindowFlags(flags2)
        self.showMaximized()

    def ImgBack001(self):
        FonD = "background-color: #1F1F1F; color: white;font: 100 10pt \"Arial Narrow\""
        self.dock = QtWidgets.QDockWidget(self.widgetA22) #於分頁內建立漂浮視窗
        self.dock.setWindowTitle("POC1應力分布圖") #設定字型與格式
        self.dock.setGeometry(660,80,640,600) #注意size設定
        self.dock.setMaximumSize(QtCore.QSize(1360,700))

        self.pushButton_022 = QtWidgets.QPushButton(self.dock)
        self.pushButton_022.setGeometry(QtCore.QRect(20, 25, 45, 35))
        self.pushButton_022.setObjectName("pushButton_022")
        self.pushButton_022.setStyleSheet("background-color: #1F1F1F; color: white;font: 100 10pt \"Arial Narrow\"")
        self.pushButton_022.setText("")
        self.pushButton_022.setStyleSheet("QPushButton{color:white}"
                                  "QPushButton:hover{color:blue}"
                                  "QPushButton{background-image : url(/FHEUI/fig/max1.png)}"
                                  "QPushButton{background-color:#1E1E1E}"
                                  "QPushButton:hover{background-image:url(/FHEUI/fig/max2.png)}"
                                  "QPushButton{border:1px}"
                                  "QPushButton{border-radius:2px}"
                                  "QPushButton{font: 10pt} "
                                  "QPushButton{padding:2px 4px}")
        self.pushButton_022.clicked.connect(self.dock.showMaximized)


        self.pushButtonLoadz017 = QtWidgets.QPushButton("開啟結果檔",self.dock,clicked=self.ImgPOC)
        self.pushButtonLoadz017.setGeometry(130, 25, 100, 35)
    #    self.tableViewA13.horizontalHeader().setStretchLastSection(True)
    #    self.tableViewA13.setColumnCount(5)              
        self.pushButtonLoadz017.setStyleSheet(FonD)

        FonB = "font-size: 16pt; font: bold;font-family:微軟正黑體 ;"
        

        self.LBLeZ022 = QLabel("POC1 可拉伸線路應力分布圖", self.dock)
        self.LBLeZ022.setStyleSheet(FonB)
        self.LBLeZ022.setGeometry(240,15, 300, 50)



        hbox = QHBoxLayout (self.dock)
        lbl = QLabel (self.dock, alignment=Qt.AlignCenter)

       # self.pixmap = QPixmap ("d:\\FHEUI\\Project\\POC1\\Image\\POC1-S-1mm.jpg")  
      #  lbl.setPixmap (self.pixmap)  
      # 
       
        lbl.setPixmap(self.pixmap.scaled(self.pixmap.width(), self.pixmap.height(), QtCore.Qt.KeepAspectRatio))
        lbl.setGeometry(QtCore.QRect(20,70,800,700))
        lbl.setScaledContents (True)
        hbox.addWidget (lbl,alignment=Qt.AlignCenter)  
        self.dock.setLayout (hbox)
################ MV
############################################
        self.mediaPlayer = QMediaPlayer(None, QMediaPlayer.VideoSurface)

        videoWidget = QVideoWidget(self.dock)
        videoWidget.setGeometry(830, 70, 500, 400)
      #  self.playButton = QPushButton()

        self.playButton = QPushButton(self.dock)
        self.playButton.setGeometry(830, 480, 50, 50)


        self.playButton.setEnabled(False)
        self.playButton.setIcon(self.style().standardIcon(QStyle.SP_MediaPlay))
        
        self.mediaPlayer.setMedia(QMediaContent(QUrl.fromLocalFile("d:\\FHEUI\\Project\\POC1\\Video\\POC1-S-1mm.mp4")))
        self.playButton.setEnabled(True)
        self.playButton.clicked.connect(self.play)
        
        self.positionSlider = QSlider(Qt.Horizontal)
        
        self.positionSlider.setRange(0, 0)
        self.positionSlider.sliderMoved.connect(self.setPosition)

        self.errorLabel = QLabel()
        self.errorLabel.setSizePolicy(QSizePolicy.Preferred,
                QSizePolicy.Maximum)

        self.positionSlider.setGeometry(QtCore.QRect(885, 480, 445, 50))
        
        hbox.addWidget(self.positionSlider)    
        self.dock.setLayout(hbox)
        
        
        self.mediaPlayer.setVideoOutput(videoWidget)
        self.mediaPlayer.stateChanged.connect(self.mediaStateChanged)
        self.mediaPlayer.positionChanged.connect(self.positionChanged)
        self.mediaPlayer.durationChanged.connect(self.durationChanged)
        self.mediaPlayer.error.connect(self.handleError)


        self.dock.show()

    
    
    def ImgBack002(self):

        FonB = "font-size: 16pt; font: bold;font-family:微軟正黑體 ;"
        FonD = "background-color: #1F1F1F; color: white;font: 100 10pt \"Arial Narrow\""

        self.dockexcel = QtWidgets.QDockWidget(self.widgetA22) #於分頁內建立浮動視窗
        self.dockexcel.setWindowTitle("  應變-電阻-應力表 ") #設定字型與格式
        self.dockexcel.setGeometry(100, 80, 550, 200) #注意size設定
        #loadcsv002 要def
        self.model = QtGui.QStandardItemModel(self.dockexcel) #浮動視窗內來個表格
        self.LBLe014 = QLabel("POC Data", self.dockexcel)
        self.LBLe014.setStyleSheet(FonB)
        self.LBLe014.setGeometry(200,30, 350, 50)


        self.tableView = QtWidgets.QTableView(self.dockexcel)
        
        self.tableView.setGeometry(5, 80, 1350, 600)

        
        self.pushButton_014 = QtWidgets.QPushButton(self.dockexcel)
        self.pushButton_014.setGeometry(QtCore.QRect(5, 30, 45, 35))
        self.pushButton_014.setObjectName("pushButton_014")
        self.pushButton_014.setStyleSheet("background-color: #1F1F1F; color: white;font: 100 10pt \"Arial Narrow\"")
        self.pushButton_014.setText("")
       # self.pushButton_014.setFont(QFont('Arial', 5))
        self.pushButton_014.setStyleSheet("QPushButton{color:white}"
                                  "QPushButton:hover{color:blue}"
                                  "QPushButton{background-image : url(/FHEUI/fig/max1.png)}"
                                  "QPushButton{background-color:#1E1E1E}"
                                  "QPushButton:hover{background-image:url(/FHEUI/fig/max2.png)}"
                                  "QPushButton{border:1px}"
                                  "QPushButton{border-radius:2px}"
                                  "QPushButton{font: 10pt} "
                                  "QPushButton{padding:2px 4px}")  
       
        self.pushButton_014.clicked.connect(self.dockexcel.showMaximized) 


        self.pushButtonLoad014 = QtWidgets.QPushButton("開啟結果檔",self.dockexcel,clicked=self.on_pushButtonLoad_clicked13)
        self.pushButtonLoad014.setGeometry(600, 30, 100, 35)
    #    self.tableViewA13.horizontalHeader().setStretchLastSection(True)
    #    self.tableViewA13.setColumnCount(5)              
        self.pushButtonLoad014.setStyleSheet(FonD)
        self.pushButtonWrite014 = QtWidgets.QPushButton("儲存結果檔",self.dockexcel,
           clicked=self.on_pushButtonWrite_clicked)
        self.pushButtonWrite014.setGeometry(750, 30, 100, 35) 
        self.pushButtonWrite014.setStyleSheet(FonD)
        
        FonC = "font-size: 8pt; font: bold;font-family:微軟正黑體 ;text-decoration: underline;"
        FileName015 ="POC1_Structral-Electric_Results_CSV.csv"
        self.LBLe015 = QLabel(FileName015, self.dockexcel)
        self.LBLe015.setStyleSheet(FonC)
        self.LBLe015.setGeometry(900,30, 350, 50)

        
        self.loadCsv014()
        self.tableView.setModel(self.model)
       # self.dockexcel.setCentralWidget(self.tableView) 
        self.tableView.setColumnWidth(0,250)
        self.tableView.setColumnWidth(1,250)
        self.tableView.setColumnWidth(2,250)
        self.tableView.setColumnWidth(3,250)

        self.dockexcel.show()
             

    def ImgBack003(self):
        FonD = "background-color: #1F1F1F; color: white;font: 100 10pt \"Arial Narrow\""
        self.dockexcel2 = QtWidgets.QDockWidget(self.widgetA22) #於分頁內建立浮動視窗
        self.dockexcel2.setWindowTitle("  應變-電阻關係圖 ") #設定字型與格式
        self.dockexcel2.setGeometry(100, 280, 550, 350) #注意size設定

        self.pushButton_015 = QtWidgets.QPushButton(self.dockexcel2)
        self.pushButton_015.setGeometry(QtCore.QRect(5, 30, 45, 35))
        self.pushButton_015.setObjectName("pushButton_015")
        self.pushButton_015.setStyleSheet("background-color: #1F1F1F; color: white;font: 100 10pt \"Arial Narrow\"")
        self.pushButton_015.setText("")
       # self.pushButton_014.setFont(QFont('Arial', 5))
        self.pushButton_015.setStyleSheet("QPushButton{color:white}"
                                  "QPushButton:hover{color:blue}"
                                  "QPushButton{background-image : url(/FHEUI/fig/max1.png)}"
                                  "QPushButton{background-color:#1E1E1E}"
                                  "QPushButton:hover{background-image:url(/FHEUI/fig/max2.png)}"
                                  "QPushButton{border:1px}"
                                  "QPushButton{border-radius:2px}"
                                  "QPushButton{font: 10pt} "
                                  "QPushButton{padding:2px 4px}")  
        self.pushButton_015.clicked.connect(self.dockexcel2.showMaximized)
        
        
        
        
        self.graphWidget = pg.PlotWidget(self.dockexcel2)
        self.graphWidget.setGeometry(5,80,550,350)

        FonB = "font-size: 16pt; font: bold;font-family:微軟正黑體 ;"
        self.LBLeZ014 = QLabel("POC1 應變-電阻關係圖", self.dockexcel2)
        self.LBLeZ014.setStyleSheet(FonB)
        self.LBLeZ014.setGeometry(200,30, 350, 50)

       # self.graphWidget.resize(400,300)  
        t = []
        s = []
        hour = []
        temperature = []

        with open('d:\\FHEUI\\Project\\POC1\\Data\\POC1_Structral-Electric_Results_CSV.csv', "r",encoding='utf-8-sig') as csvDataFile: 
            csvReader = csv.reader(csvDataFile)
            for row in csvReader:
                t.append(row[0])
                s.append(row[1])
  
        for i in range(0, len(t)): 
            t[i] = float(t[i])
        for i in range(0, len(s)): 
            s[i] = float(s[i]) 

        maxValue = np.amax(s)
        minValue = np.amin(s)
        print(maxValue)
        print(minValue)


        #Add Background colour to white
        #self.graphWidget.setBackground('#bbccaa')
        self.graphWidget.setBackground('#1E1E1E')
        # Add Title

        self.graphWidget.setTitle("Strain-Resistance Correlation", color="w", size="15pt")
        # Add Axis Labels

        
        
        styles = {"color": "white", "font-size": "15px"}
        self.graphWidget.setLabel("left", "Resistance (Ω)", **styles)
        self.graphWidget.setLabel("bottom", "Displacement (mm)", **styles)
        #Add legend
        self.graphWidget.addLegend()
        #Add grid
        self.graphWidget.showGrid(x=False, y=False)
        #Set Range
        self.graphWidget.setXRange(0, 20, padding=0)
        self.graphWidget.setYRange(0, 10, padding=0)

        #pen = pg.mkPen(color=(0, 0, 0))
        pen = pg.mkPen(color=(255, 255, 255))
        self.graphWidget.plot(t, s, name="___L1",  pen=pen, symbol='+', symbolSize=10, symbolBrush=('w'), font = '微軟正黑體')


        self.pushButtonLoad017 = QtWidgets.QPushButton("開啟結果檔",self.dockexcel2,clicked=self.plotPOC)
        self.pushButtonLoad017.setGeometry(600, 30, 100, 35)
    #    self.tableViewA13.horizontalHeader().setStretchLastSection(True)
    #    self.tableViewA13.setColumnCount(5)              
        self.pushButtonLoad017.setStyleSheet(FonD)


        self.dockexcel2.show()
      






    
    def changeTabShape(self, index):
        if index == 0:
            self.qtabwidget.setTabShape(QtWidgets.QTabWidget.Rounded)
        else:
            self.qtabwidget.setTabShape(QtWidgets.QTabWidget.Triangular)

    def plot_(self):
        ax = self.figure.add_axes([0.1,0.1,0.8,0.8])
        ax.plot([2,4,6,8,10])
        self.canvas.draw()
    def plot_1(self):
        ax = self.figure7.add_axes([0.1,0.1,0.8,0.8])
        ax.plot([1,2,3,4,5])
        self.canvas7.draw()   



    def createGridGroupBox(self):
        self.gridGroupBox = QGroupBox("記錄",self.widgetA9)
        lines=[]

        file1 = open("D:\\FHEUI\\rec\\Proj1005.txt","r",encoding='utf-8') 
        lines = file1.readlines()
        layout = QGridLayout()

        line000=lines[0]
        line001=lines[1]
        line002=lines[2]
        line003=lines[3]
        line004=lines[4]
        line005=lines[5]


        self.nameLabel = QLabel("案例編號",self.widgetA9)
        self.nameLineEdit = QLineEdit(line000,self.widgetA9)
        self.emitLabel = QLabel("案例名稱",self.widgetA9)
        self.emitLineEdit = QLineEdit(line001,self.widgetA9)
        self.timeLabel = QLabel("更新日期",self.widgetA9)
        self.timeLineEdit = QLineEdit(line002,self.widgetA9)

        layout.setSpacing(10) 
        layout.addWidget(self.nameLabel,1,0)
        layout.addWidget(self.nameLineEdit,1,1)
        layout.addWidget(self.emitLabel,2,0)
        layout.addWidget(self.emitLineEdit,2,1)
        layout.addWidget(self.timeLabel,3,0)
        layout.addWidget(self.timeLineEdit,3,1)
     #   layout.addWidget(imgeLabel,0,2,4,1)
        layout.setColumnStretch(1, 10)
        self.gridGroupBox.setLayout(layout)
     #   self.setWindowTitle('Basic Layout')

    def creatVboxGroupBox(self):
       # self.vboxGroupBox = QGroupBox("Vbox layout",self.widgetA9)
        self.vboxGroupBox = QGroupBox("模擬結果",self.widgetA9)
        self.vboxGroupBox.setStyleSheet("font-size: 15pt; font-family: Arial;background-color:rgb(85, 170, 255);color:white;border-radius: 10px; text-align:center")
        self.layout = QVBoxLayout(self.vboxGroupBox)      
#####  PLOT 繪圖
        
        self.figure = plt.figure()
        self.canvas = FigureCanvas(self.figure)
        self.button_plot9 = QtWidgets.QPushButton("繪圖",self.vboxGroupBox)
        self.button_plot9.setStyleSheet("font-size: 12pt; font-family: Arial;background-color:rgb(85, 170, 255);color:white;border-radius: 10px; text-align:center")
        self.button_plot9.setGeometry(450,300, 150, 50)
      
        # 連接事件
        self.button_plot9.clicked.connect(self.plot_)
      
        # 設置佈局
     #   layout1 = QtWidgets.QVBoxLayout(self.layout)
       # layout.setGeometry(50,300,300,200)
        self.layout.addWidget(self.canvas)

        self.layout.addWidget(self.button_plot9)
        self.setLayout(self.layout)
       
        self.vboxGroupBox.setLayout(self.layout)

    def creatFormGroupBox(self):

        lines=[]

        file1 = open("D:\\FHEUI\\Proj1005.txt","r",encoding='utf-8') 
        lines = file1.readlines()
   
        line000=lines[0]
        line001=lines[1]
        line002=lines[2]
        line003=lines[3]
        line004=lines[4]
        line005=lines[5]

        self.formGroupBox = QGroupBox("DRC檢查結果",self.widgetA9)
        layout = QFormLayout(self.widgetA9)
        performanceLabel = QLabel("本設計要點：",self.widgetA9)
        self.performanceEditor = QLineEdit(lines[3],self.widgetA9)
        planLabel = QLabel("本設計流程檢查：",self.widgetA9)
        self.planEditor = QTextEdit(self.widgetA9)
        self.planEditor.setPlainText("Step1: OK.")
        
        #txtoutput=line004+"\n"+line005
        txtoutput=line004+line005
        self.planEditor.setPlainText(txtoutput)
       # self.planEditor.setPlainText(line005)
        layout.addRow(performanceLabel,self.performanceEditor)
        layout.addRow(planLabel,self.planEditor)

        self.formGroupBox.setLayout(layout)







    @QtCore.pyqtSlot(int)
    def qtabwidget_tabcloserequested(self, index):
        # gets the widget
        widget = self.qtabwidget.widget(index)
        # if the widget exists
        if widget:
            widget.deleteLater()
        # removes the tab of the QTabWidget
        self.qtabwidget.removeTab(index)
        
    @QtCore.pyqtSlot(int)
    def qtabwidget_currentchanged(self, index):
        print(f"\n New index of current page: {index}")

    #center
    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def mousePressEvent(self, event):
        self.oldPos = event.globalPos()

    def mouseMoveEvent(self, event):
     #   delta = QPoint (event.globalPos() - self.oldPos)
        delta = 0
        #print(delta)
       # self.move(self.x() + delta.x(), self.y() + delta.y())
      #  self.oldPos = event.globalPos() 


    def APP(self):
        subprocess.Popen([r"C:\\Program Files\\FreeCAD 0.18\\bin\\FreeCAD.exe"])
    def TABLocation(self):
        self.qtabwidget.setTabPosition(QtWidgets.QTabWidget.South) 
    def TABLocation2(self):
        self.qtabwidget.setTabPosition(QtWidgets.QTabWidget.North)
    def TABLocation3(self):
        self.qtabwidget.setTabPosition(QtWidgets.QTabWidget.East) 
    def TABLocation4(self):
        self.qtabwidget.setTabPosition(QtWidgets.QTabWidget.West) 

    def pdfviewer(self,text):      
        os.system("D:\\Twinbuilder.pdf") 

    def retranslateUi(self,Window):
        _translate = QtCore.QCoreApplication.translate
        self.pushButton_5.setText(_translate("Window", "COMSOL"))
    
################################################
    def openFile(self):
        #fileName, _ = QFileDialog.getOpenFileName(self, "Open Movie",
        #        QDir.homePath())
        fileName, _ = QFileDialog.getOpenFileName(self, "選擇影片檔","D:\\FHEUI\\ANSYS","Video Files (*.mp4 *.flv *.ts *.mts *.avi)")

        ###fileName, _ = QFileDialog.getOpenFileName(self, "選擇影片檔",QDir.homePath("c:\\FHEmake\\MV"),
        ###        ".", "Video Files (*.mp4 *.flv *.ts *.mts *.avi)")          
        
        #if fileName != '':
        #    self.mediaPlayer.setMedia(
        #            QMediaContent(QUrl.fromLocalFile(fileName)))
        #    self.playButton.setEnabled(True)
        if fileName != '':
            self.mediaPlayer.setMedia(
                    QMediaContent(QUrl.fromLocalFile(fileName)))
            self.playButton.setEnabled(True)
            #self.statusBar.showMessage(fileName)
            #self.play()

    def exitCall(self):
        sys.exit(app.exec_())

    def play(self):
        if self.mediaPlayer.state() == QMediaPlayer.PlayingState:
            self.mediaPlayer.pause()
        else:
            self.mediaPlayer.play()

    def mediaStateChanged(self, state):
        if self.mediaPlayer.state() == QMediaPlayer.PlayingState:
            self.playButton.setIcon(
                    self.style().standardIcon(QStyle.SP_MediaPause))
        else:
            self.playButton.setIcon(
                    self.style().standardIcon(QStyle.SP_MediaPlay))

    def positionChanged(self, position):
        self.positionSlider.setValue(position)

    def durationChanged(self, duration):
        self.positionSlider.setRange(0, duration)

    def setPosition(self, position):
        self.mediaPlayer.setPosition(position)

    def handleError(self):
        self.playButton.setEnabled(False)
        self.errorLabel.setText("Error: " + self.mediaPlayer.errorString())

############# 多重視窗

    def createAction(self, text,icon=None,checkable=False,slot=None,tip=None,shortcut=None):
        action = QAction(text,self)
        if icon is not None:
            action.setIcon(QIcon(icon))
        if checkable:
            action.setCheckable(True)#可切換
            if slot is not None: action.toggled.connect(slot)
        else:
            if slot is not None: action.triggered.connect(slot)
        if tip is not None:
            action.setToolTip(tip)#工具列提示
            action.setStatusTip(tip)#狀態列提示
        if shortcut is not None:
            action.setShortcut(shortcut)#快速鍵
   
        return action
    
    
    def createFileActions(self): #創建檔相關動作
        #動作分隔符號
        self.fileNewAction = self.createAction("&新增專案",icon="filenew.png",checkable=False,
                                                slot=self.fileNew,tip="新建文件",shortcut=QKeySequence.New)
        self.separator  = QAction(self)
        self.separator.setSeparator(True)
        self.exitAction = self.createAction("&離開專案",icon="",checkable=False,
                                                slot=self.close,tip="退出",shortcut=QKeySequence.Close)
    def fileNew(self):
        windowNew =MdiSubWindow()   #產生實體多重文件介面對象
        windowNew.setWidget(QTextEdit())   #設置sub內部部件
        windowNew.setWindowTitle('  POC模擬- %d' % len(self.mdi.subWindowList()))  #設置新建子視窗的標題
        print(windowNew.windowTitle())
        self.mdi.addSubWindow(windowNew) #將子視窗添加到Mdi區域
        windowNew.setGeometry(QtCore.QRect(0,0, 300, 300))
        windowNew.setStyleSheet("background-color: #1E1E1E; color: white ;font: 50 12pt \"Arial Narrow\"")
#        windowNew.setIcon(QtGui.QIcon("hand-A.png"))
        windowNew.setWindowIcon(QIcon('d:\\FHEUI\\fig\\itrilogo.png'))
        windowNew.setMaximumSize(650, 300) 
        
        windowNew.show()  #子視窗顯示.
        
    def updateWindowMenu(self):#動態顯示視窗功能表
        self.windowMenu.clear() # 先清空已有的功能表項目
        self.windowMenu.addAction('併排 Cascade')
        self.windowMenu.addAction('標題 Tiled')
        self.windowMenu.addAction("前一視窗 Previous Window")
        self.windowMenu.addAction("下一視窗 Next Window")
        self.windowMenu.addSeparator()
        
        for windowNew in self.mdi.subWindowList():
            action = self.windowMenu.addAction(windowNew.windowTitle())
            action.setData(windowNew)# 關聯窗口和action
            
        self.windowMenu.addSeparator()
        self.windowMenu.addAction("關閉 close Active Window")
        self.windowMenu.addAction("關閉 close All Windows")
        
        #點擊QAction綁定自訂的槽函數（傳遞有值【QAction】）
        self.windowMenu.triggered[QAction].connect(self.windowAction)
        
    def windowAction(self,q):
        if q.text()=='併排 Cascade':
            self.mdi.cascadeSubWindows()  #層疊顯示
        elif q.text()=='標題 Tiled':
            self.mdi.tileSubWindows()  #平鋪顯示
        elif q.text() == "前一視窗 Previous Window":
            self.mdi.activatePreviousSubWindow()
        elif q.text() == "下一視窗 Next Window":
            self.mdi.activateNextSubWindow()
        elif q.text() == "關閉 close Active Window":
            self.mdi.closeActiveSubWindow()   
        elif q.text() == "關閉 close All Windows":
            self.mdi.closeAllSubWindows()
        else: #啟動窗口
            self.mdi.setActiveSubWindow(q.data())


    def CLOSE4(self):
        closec = QMessageBox()
        closec.setGeometry(500, 400, 300, 220)
        #self.setWindowTitle('關閉程式')
         # 主視窗 加入ICON
        closec.setWindowTitle('關閉程式')
        closec.setWindowIcon(QIcon('d:\\FHEUI\\fig\\itrilogo.png'))
        closec.setText("關閉程式?")
        closec.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        closed = closec.exec()
        #showup =
        if closed == QMessageBox.Yes:
            #MainWindow.colse()
           
            timeStamp = int(time.time())
            #轉換為其他日期格式,如:”%Y-%m-%d %H:%M:%S”
            timeArray = time.localtime(timeStamp)
            otherStyleTime = time.strftime('%Y-%m-%d %H:%M:%S', timeArray)

            print ('current_time',otherStyleTime)
        
            f = open('D:\\FHEUI\\FHE2021.log', 'a')
            #f.write("Try to use file.write()\nHail HYDRA")
        
            f.write("\n登出時間:  ")
            f.write(otherStyleTime)
            f.write("\n------------------------------------------")
            f.close()

            print("bye-bye")
            Window.close()

        if closed == QMessageBox.No:
           # os.system("D:\\FHEUI\\Mdi001d.py")
            print("Keep Running.")

    def CLOSE5(self):
        closec = QMessageBox()
        closec.setGeometry(500, 400, 300, 220)
        #self.setWindowTitle('關閉程式')
         # 主視窗 加入ICON
        closec.setWindowTitle('關閉程式')
        closec.setWindowIcon(QIcon('d:\\FHEUI\\fig\\itrilogo.png'))
        closec.setText("關閉程式?")
        closec.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        closed = closec.exec()
        #showup =
        if closed == QMessageBox.Yes:
            #MainWindow.colse()
           
            timeStamp = int(time.time())
            #轉換為其他日期格式,如:”%Y-%m-%d %H:%M:%S”
            timeArray = time.localtime(timeStamp)
            otherStyleTime = time.strftime('%Y-%m-%d %H:%M:%S', timeArray)

            print ('current_time',otherStyleTime)
        
            f = open('D:\\FHEUI\\FHE2021.log', 'a')
            #f.write("Try to use file.write()\nHail HYDRA")
        
            f.write("\n登出時間:  ")
            f.write(otherStyleTime)
            f.write("\n------------------------------------------")
            f.close()

            print("bye-bye")
            Window.close()

        if closed == QMessageBox.No:
            os.system("D:\\FHEUI\\Mdi001h2.py")
            print("Keep Running.")
    
    
    def stretchable(self):
        os.system("D:\\FHEUI\\FHEmake\\FHE-1017-5e.py")
    
    
    def explore(self):

        path004= self.apath003.text()
                
        print(path004)
        os.system( path004 )  
       
        

    def listWidgetContext(self,point):
        popMenu = QMenu()
        popMenu.addAction("Go to POC1",self.changetab6)
        popMenu.addAction("Go to POC2",self.changetab6)
        popMenu.addAction("Go to POC5",self.changetab6)
        popMenu.exec_(QCursor.pos())

    def listWidgetContext002(self,point):
        popMenu = QMenu()
        popMenu.addAction("執行",self.explore)
        popMenu.addAction("修改")
        popMenu.addAction("删除")
        popMenu.exec_(QCursor.pos())

   # def mouseDoubleClickEvent(self, event):    
        
   #     self.explore  

    def items001show(self):
        
        self.items001.show()
        self.addDockWidget(Qt.RightDockWidgetArea, self.items001)

    def itemsFileshow(self):
        self.itemsFile.show()
        self.addDockWidget(Qt.RightDockWidgetArea, self.itemsFile)


    def items102show(self):
        
        self.items102.show()
        self.addDockWidget(Qt.RightDockWidgetArea, self.items102)

    def ImgPOC(self):     
        
        fileName, _ =  QtWidgets.QFileDialog.getOpenFileName(self, self.tr("  開啟分析圖片檔   "),"D:\\FHEUI\\Project\\POC1\\Image", self.tr("Image Files (*.jpg)"))

        hbox = QHBoxLayout (self.dock)
        self.lblZ = QLabel (self.dock, alignment=Qt.AlignCenter)

        self.pixmap = QPixmap (fileName)  
      #  lbl.setPixmap (self.pixmap)  
      # 
       
        self.lblZ.setPixmap(self.pixmap.scaled(self.pixmap.width(), self.pixmap.height(), QtCore.Qt.KeepAspectRatio))
        self.lblZ.setGeometry(QtCore.QRect(20,70,800,700))
        self.lblZ.setScaledContents (True)
        hbox.addWidget (self.lblZ,alignment=Qt.AlignCenter)  
        self.dock.setLayout (hbox)
        self.lblZ.show()
        
        FonE = "font-size: 12pt; font: bold;font-family:微軟正黑體 ;text-decoration: underline;"
       # self.LBLe016 = QLabel('"' + fileName + '"', self.dockexcel)
        self.LBLeZ016 = QLabel(fileName, self.dock)
        
        #  self.LBLe016 = QLabel("999 POC5_Ball_Drop_Results_CSV.csv", self.dockexcel)
        self.LBLeZ016.setStyleSheet(FonE)
        self.LBLeZ016.setGeometry(550,15,600,50)                
        self.LBLeZ016.show()

    def plotPOC(self):   
         
        t = []
        s = []

        fileNamePOC, _ =  QtWidgets.QFileDialog.getOpenFileName(self, self.tr("  開啟分析結果檔   "), 
            QtCore.QDir.currentPath(), self.tr("CSV Files (*.csv)"))
        
        
        with open(fileNamePOC, "r",encoding='utf-8-sig') as csvDataFile: 
            
            csvReader = csv.reader(csvDataFile)
            for row in csvReader:
                t.append(row[0])
                s.append(row[1])
  
        for i in range(0, len(t)): 
            t[i] = float(t[i])
        for i in range(0, len(s)): 
            s[i] = float(s[i]) 

        maxValue = np.amax(s)
        minValue = np.amin(s)
        print(maxValue)
        print(minValue)


        #Add Background colour to white
        #self.graphWidget.setBackground('#bbccaa')
        self.graphWidget.setBackground('#1E1E1E')
        # Add Title

        self.graphWidget.setTitle("Strain-Resistance Correlation", color="w", size="15pt")
        # Add Axis Labels

        
        
        styles = {"color": "white", "font-size": "15px"}
        self.graphWidget.setLabel("left", "Resistance (Ω)", **styles)
        self.graphWidget.setLabel("bottom", "Displacement (mm)", **styles)
        #Add legend
        self.graphWidget.addLegend()
        #Add grid
        self.graphWidget.showGrid(x=False, y=False)
        #Set Range
        self.graphWidget.setXRange(0, 20, padding=0)
        self.graphWidget.setYRange(0, 10, padding=0)

        #pen = pg.mkPen(color=(0, 0, 0))
        pen = pg.mkPen(color=(255, 255, 255))
        self.graphWidget.plot(t, s, name="___L1",  pen=pen, symbol='+', symbolSize=10, symbolBrush=('w'), font = '微軟正黑體')

        self.graphWidget.show()

    def statuson(self):
        self.statusBar().show()
        timeStamp = int(time.time())
        #轉換為其他日期格式,如:”%Y-%m-%d %H:%M:%S”
        timeArray = time.localtime(timeStamp)
      #  otherStyleTime = time.strftime('%Y-%m-%d %H:%M:%S', timeArray)
        otherStyleTime = time.strftime('%Y-%m-%d ', timeArray)
        self.statusBar().showMessage('FHE Designed by ITRI.   '+ otherStyleTime) 
       
    def statusoff(self):
        self.statusBar().close()

    def handleDisplay(self, data001):
        self.statusBar().showMessage('FHE Designed by ITRI.   '+ data001)
        #self.input.setText(data001)

        

if __name__ == '__main__':
    application = QtWidgets.QApplication(sys.argv)
    Window = Window()


    Window.show()

   
   # mdi= Window()
   # mdi.show()
    sys.exit(application.exec_()) 

