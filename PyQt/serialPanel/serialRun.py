## Task 1, arduino serial
#import serial
#import matplotlib.pyplot as plt
#
#ser = serial.Serial('COM34', 9600)
#n=0
#dataLst=[]
#while n<1000:
#    print (ser.readline())
#    dataPoint=ser.readline()
#    dataPoint=int(dataPoint)
#    dataLst.append(dataPoint)
#    n+=1
##print(type(dataPoint))
##print(dataPoint)
#plt.plot(dataLst)
#ser.close()

# Task 2, save data to an external file and then plot it out
# not done yet

## Task 3, live plot, need serialPanel.serial.py
#from PyQt5 import QtGui,QtCore
#import sys
#import serialPanel_serial
#import numpy as np
##import pylab
#import time
#import pyqtgraph
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
##        time.sleep(1)
#        QtCore.QTimer.singleShot(1, self.update) # 1 ms, QUICKLY repeat, recursively
#
#app = QtGui.QApplication(sys.argv)
#form = ExampleApp()
#form.show()
#form.update() #start with something
#app.exec_()

# Task 4, plot the received data in the GUI
import serial
ser = serial.Serial('COM34', 9600)

from PyQt5 import QtGui,QtCore
import sys
import serialPanel_serial
import numpy as np
import pyqtgraph

class ExampleApp(QtGui.QMainWindow, serialPanel_serial.Ui_MainWindow):
    def __init__(self):
        pyqtgraph.setConfigOption('background', 'w') #before loading widget
        super().__init__()
        self.setupUi(self)

    def update(self):
        points=100 #number of data points
        X=np.arange(points)
        n=0
        dataLst=[]
        while n<100:
            dataPoint=ser.readline()
            dataPoint=int(dataPoint)
            dataLst.append(dataPoint)
            n+=1
        Y=dataLst
        penn=pyqtgraph.mkPen('k', width=3, style=QtCore.Qt.SolidLine) 
        self.graphicsView.plot(X,Y,pen=penn, clear=True)
#        time.sleep(1)
        QtCore.QTimer.singleShot(1, self.update) # 1 ms, QUICKLY repeat, recursively

app = QtGui.QApplication(sys.argv)
form = ExampleApp()
form.show()
form.update() #start with something
app.exec_()








