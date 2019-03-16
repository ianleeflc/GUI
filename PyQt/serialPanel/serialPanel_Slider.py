# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'serialPanel_Slider.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
'''usr code'''
import RPi.GPIO as GPIO
from gpiozero import LED
from time import sleep

GPIO.setmode(GPIO.BCM)

led=LED(23) # for the led toggling project

led_pin=24 # for the led dimmer project
GPIO.setup(led_pin, GPIO.OUT)
pwm=GPIO.PWM(led_pin,100)
pwm.start(100)

def ledToggle():
    if led.is_lit:
        led.off()
    else: 
        led.on()
'''usr code'''

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(615, 310)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(70, 50, 171, 151))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")

        self.verticalSlider = QtWidgets.QSlider(self.centralwidget)

        '''usr code'''
        self.verticalSlider.setMinimum(0)
        self.verticalSlider.setMaximum(100)
        self.verticalSlider.setValue(100)
        '''usr code'''

        self.verticalSlider.setGeometry(QtCore.QRect(410, 50, 22, 160))
        self.verticalSlider.setOrientation(QtCore.Qt.Vertical)
        self.verticalSlider.setObjectName("verticalSlider")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(380, 220, 101, 22))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEdit.setFont(font)
        self.lineEdit.setObjectName("lineEdit")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "Toggle LED"))
        self.lineEdit.setText(_translate("MainWindow", "LED Brightness"))
        '''usr code'''
        self.pushButton.clicked.connect(ledToggle)
        self.verticalSlider.valueChanged.connect(self.sliderMov)

    def sliderMov(self):
        value=self.verticalSlider.value()
        print(value)
        pwm.ChangeDutyCycle(value)
        '''usr code'''

'''usr code'''
import sys
app=QtWidgets.QApplication(sys.argv)
MainWindow=QtWidgets.QMainWindow()
ui=Ui_MainWindow()
ui.setupUi(MainWindow)
MainWindow.show()
sys.exit(app.exec_())
'''usr code'''
