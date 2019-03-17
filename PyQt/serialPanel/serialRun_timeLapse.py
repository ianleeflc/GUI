from PyQt5 import QtGui,QtCore
import sys
import serialPanel_serial
import numpy as np
#import pylab
import time
import pyqtgraph

class ExampleApp(QtGui.QMainWindow, serialPanel_serial.Ui_MainWindow):
    def __init__(self):
        pyqtgraph.setConfigOption('background', 'w') #before loading widget
        super().__init__()
        self.setupUi(self)

    def update(self):
        points=100 #number of data points
        X=np.arange(points)
        Y=np.sin(np.arange(points)/points*4*np.pi+time.time())
        penn=pyqtgraph.mkPen('k', width=3, style=QtCore.Qt.SolidLine) 
        self.graphicsView.plot(X,Y,pen=penn, clear=True)
  
        QtCore.QTimer.singleShot(0.1, self.update) # QUICKLY repeat

app = QtGui.QApplication(sys.argv)
form = ExampleApp()
form.show()
form.update() #start with something
app.exec_()
