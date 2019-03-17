import serial
ser = serial.Serial('COM34', 9600)
while True:
    print (ser.readline())