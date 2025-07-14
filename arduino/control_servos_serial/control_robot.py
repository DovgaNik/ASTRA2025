import time
import serial

# Pins of servos must be set up in the arduino code, while in python code the letter corresponding to each servo must be specified.
#A
#B
#C
#D - clamp servo in the current setup

# Clamp is closed at ≈50º, we assume that the open position is ≈100º

ser = serial.Serial('/dev/ttyACM0', 9600)  # open serial port
time.sleep(3)
print(ser.name)
ser.write('D100\n'.encode())
time.sleep(2)
ser.write('D50\n'.encode())
ser.close()

def clamp_open():
    send_text()

def send_text(command):
    ser.write((command + '\n').encode())