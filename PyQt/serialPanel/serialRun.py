## Task 1, arduino serial. This is the simplest way to collect serial data using Arduino + Windows PC, save it and visulize it. Not live plot
#import serial
#import matplotlib.pyplot as plt
#
#ser = serial.Serial('COM34', 9600)
#n=0
#dataLst=[]
#while n<200: # collect 200 data points and stop
#    print (ser.readline())
#    dataPoint=ser.readline()
#    dataPoint=int(dataPoint) # the data received are strings
#    dataLst.append(dataPoint)
#    n+=1
##print(type(dataPoint))
##print(dataPoint)
#ser.close() # don't forget to close the serial port
#
#plt.plot(dataLst) # plot the received data afterwards
#plt.show() # if you run this code in Spyder, you don't need this line
#f=open("serialData.dat", "w") # save the data to a file
#f.write(str(dataLst)) # string is the only legal format to be written into a file
#f.close()
#f=open('serialData.dat','r')
#print(f.read())
#

## Task 2, use pyqtgraph to plot the data instead of using matplotlib
#import pyqtgraph as pg
#from pyqtgraph.Qt import QtCore, QtGui
#from pyqtgraph import PlotWidget
#import numpy as np
#
#x = np.array([1,2,3])
#y = np.array([1,2,3])
#pg.setConfigOption('background','w')
#penn=pg.mkPen('k', width=2, style=QtCore.Qt.SolidLine) 
#p1=pg.plot(x, y, pen=penn, title='The firts pyqtgraph plot', symbol='t', symbolSize=20)
#p1.setXRange(0,4)
#p1.setYRange(0,4)
#p1.setLabel('left','Voltage', 'V')
#p1.setLabel('bottom','Time', 's')
#
#QtGui.QApplication.exec_()

### try to plot something in a simple GUI
#from PyQt5 import QtGui, QtCore
#import pyqtgraph as pg
#
### Always start by initializing Qt (only once per application)
#app = QtGui.QApplication([])
### Define a top-level widget to hold everything
#w = QtGui.QWidget()
### Create some widgets to be placed inside
#btn = QtGui.QPushButton('press me')
#text = QtGui.QLineEdit('enter text')
#listw = QtGui.QListWidget()
#pg.setConfigOption('background','w')
#plt = pg.PlotWidget() # pg.PlotWidget allows the use of the properties below, but pg.plot doesn't
#penn=pg.mkPen('k', width=2, style=QtCore.Qt.SolidLine) 
#plt.plot([1,2,3],[1,2,3], pen=penn, title='The firts pyqtgraph plot', symbol='t', symbolSize=20)
#
#labelStyle={'color':'#000','font-size':'30px'}
#plt.setLabel('bottom','Time','s',**labelStyle)
#plt.setLabel('left','Voltage','V',**labelStyle)
#plt.setYRange(0,5)
#plt.setXRange(0,5)
### Create a grid layout to manage the widgets size and position
#layout = QtGui.QGridLayout()
#w.setLayout(layout)
### Add widgets to the layout in their proper positions
#layout.addWidget(btn, 0, 0) # button goes in upper-left
#layout.addWidget(text, 1, 0) # text edit goes in middle-left
#layout.addWidget(listw, 2, 0) # list widget goes in bottom-left
#layout.addWidget(plt, 0, 1, 3, 1) # plot goes on right side, spanning 3 rows and 1 column
### Display the widget as a new window
#w.show()
### Start the Qt event loop
#app.exec_()

##### Task 3, live plot the serial data the with pyqtgraph
##from PyQt5 import QtCore, QtGui, QtWidgets
##from pyqtgraph import PlotWidget
##import serial
##from PyQt5 import QtGui,QtCore
##import sys
##import numpy as np
##import pyqtgraph
##
##ser = serial.Serial('COM34', 9600)
##
##class ExampleApp(QtGui.QMainWindow):
##    def __init__(self):
##        super().__init__()
##        pyqtgraph.setConfigOption('background', 'w') # 
##        self.setupUi(self) 
##
##    def setupUi(self, MainWindow):
##        MainWindow.setObjectName("MainWindow")
##        MainWindow.resize(900, 900)
##        self.centralwidget = QtWidgets.QWidget(MainWindow)
##        self.centralwidget.setObjectName("centralwidget")
##        # the plot widget
##        self.graphicsView = PlotWidget(self.centralwidget) # assign this PlotWidget to the graphicsView. 
##        self.graphicsView.setGeometry(QtCore.QRect(200, 200, 500, 500))
##        self.graphicsView.setObjectName("graphicsView")
##        #
##        MainWindow.setCentralWidget(self.centralwidget)
##
##    def update(self):
##        points=100 #number of data points
##        X=np.arange(points)
##        n=0
##        dataLst=[]
##        while n<100:
##            dataPoint=ser.readline()
##            dataPoint=int(dataPoint)
##            dataLst.append(dataPoint)
##            n+=1
##        Y=dataLst
##        penn=pyqtgraph.mkPen('k', width=3, style=QtCore.Qt.SolidLine) 
##        self.graphicsView.setYRange(0,1200, padding=0)
##        labelStyle={'color':'#000','font-size':'20px'}
##        self.graphicsView.setLabel('bottom','Number of Points','',**labelStyle)
##        self.graphicsView.setLabel('left','Voltage','',**labelStyle)
##        self.graphicsView.plot(X,Y,pen=penn, clear=True)
##        QtCore.QTimer.singleShot(1, self.update) # 1 ms, QUICKLY repeat, recursively. Use this timer to invoke the 'update()' function recursively. 
##
##app = QtGui.QApplication(sys.argv)
##form = ExampleApp()
##form.show()
##form.update() #start with something
##app.exec_()


#### Task 4, ADC (SPI Communication) to RPI Communication, works
##import spidev
##from numpy import interp
##from time import sleep
##
##spi=spidev.SpiDev()
##spi.open(0,0)
##
##def analogInput(channel):
##    spi.max_speed_hz=1350000
##    adc=spi.xfer2([1,(8+channel)<<4,0])
##    data=((adc[1]&3)<<8)+adc[2]
##    return data
##
##while True:
##    output=analogInput(0) # Reading from CH0
##    #output=interp(output, [0,1023], [0,100])
##    print(output)
##    sleep(0.1)

## Task 5, live plot SPI data in the GUI
import spidev
from numpy import interp
from time import sleep
from PyQt5 import QtCore, QtGui, QtWidgets
from pyqtgraph import PlotWidget
##import serial
from PyQt5 import QtGui,QtCore
import sys
import numpy as np
import pyqtgraph

spi=spidev.SpiDev()
spi.open(0,0)

class ExampleApp(QtGui.QMainWindow):
    def __init__(self):
        super().__init__()
        pyqtgraph.setConfigOption('background', 'w') # 
        self.setupUi(self) 

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(350, 300)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        # the plot widget
        self.graphicsView = PlotWidget(self.centralwidget) # assign this PlotWidget to the graphicsView. 
        self.graphicsView.setGeometry(QtCore.QRect(20, 20, 300, 300))
        self.graphicsView.setObjectName("graphicsView")
        #
        MainWindow.setCentralWidget(self.centralwidget)
        
    def analogInput(self, channel):
        spi.max_speed_hz=1350000
        adc=spi.xfer2([1,(8+channel)<<4,0])
        data=((adc[1]&3)<<8)+adc[2]
        return data
    
    def update(self):
        points=100 #number of data points
        X=np.arange(points)
        n=0
        dataLst=[]
        while n<100:
            dataPoint=self.analogInput(0) # Reading from CH0
            #dataPoint=int(dataPoint)
            dataLst.append(dataPoint)
            n+=1
        Y=dataLst
        penn=pyqtgraph.mkPen('k', width=3, style=QtCore.Qt.SolidLine) 
        self.graphicsView.setYRange(0,1200, padding=0)
        labelStyle={'color':'#000','font-size':'20px'}
        self.graphicsView.setLabel('bottom','Number of Points','',**labelStyle)
        self.graphicsView.setLabel('left','Voltage','',**labelStyle)
        self.graphicsView.plot(X,Y,pen=penn, clear=True)
        QtCore.QTimer.singleShot(1, self.update) # 1 ms, QUICKLY repeat, recursively. Use this timer to invoke the 'update()' function recursively. 

app = QtGui.QApplication(sys.argv)
form = ExampleApp()
form.show()
form.update() #start with something
app.exec_()

## Task 5_x, inherit the GUI class made by Qt Designer and add things to it
#from PyQt5 import QtGui, QtCore
#import serialPanel_serial
#import sys
#import pyqtgraph
#
#class ExampleApp(QtGui.QMainWindow, serialPanel_serial.Ui_MainWindow):
#    def __init__(self):
#        pyqtgraph.setConfigOption('background','w')
#        #pyqtgraph.setConfigOption('background','k') # change it to black
#        super().__init__()
#        self.setupUi(self)
#
#app=QtGui.QApplication(sys.argv)
#form=ExampleApp()
#form.show()
#app.exec_()

## Task 6, live plot in the GUI
#from PyQt5 import QtGui,QtCore
#import sys
#import pyqtgraph
#import serialPanel_serial
#
#import numpy as np
#import time
#
#class ExampleApp(QtGui.QMainWindow, serialPanel_serial.Ui_MainWindow):
#    def __init__(self):
#        pyqtgraph.setConfigOption('background', 'w') #before loading widget
#        super().__init__()
#        self.setupUi(self)
#
#    def update(self):
#        points=100 #number of data points
#        X=np.arange(points)
#        Y=np.sin(np.arange(points)/points*4*np.pi+time.time())
#        penn=pyqtgraph.mkPen('k', width=3, style=QtCore.Qt.SolidLine) 
#        self.graphicsView.plot(X,Y,pen=penn, clear=True)
#        QtCore.QTimer.singleShot(1, self.update) # 1 ms, QUICKLY repeat, recursively
#
#app = QtGui.QApplication(sys.argv)
#form = ExampleApp()
#form.show()
#form.update() #start with something
#app.exec_()


## Task 6_x, plot the received data in the GUI. Works
#import serial
#ser = serial.Serial('COM34', 9600)
#
#from PyQt5 import QtGui,QtCore
#import sys
#import serialPanel_serial
#import numpy as np
#import pyqtgraph
#
#class ExampleApp(QtGui.QMainWindow, serialPanel_serial.Ui_MainWindow):
#    def __init__(self):
#        pyqtgraph.setConfigOption('background', 'w') # before loading any widget
#        super().__init__()
#        self.setupUi(self)
#
#    def update(self):
#        points=100 #number of data points
#        X=np.arange(points)
#        n=0
#        dataLst=[]
#        while n<100:
#            dataPoint=ser.readline()
#            dataPoint=int(dataPoint)
#            dataLst.append(dataPoint)
#            n+=1
#        Y=dataLst
#        penn=pyqtgraph.mkPen('k', width=3, style=QtCore.Qt.SolidLine) 
#        self.graphicsView.plot(X,Y,pen=penn, clear=True)
##        time.sleep(1)
#        QtCore.QTimer.singleShot(1, self.update) # 1 ms, QUICKLY repeat, recursively
#
#app = QtGui.QApplication(sys.argv)
#form = ExampleApp()
#form.show()
#form.update() #start with something
#app.exec_()








