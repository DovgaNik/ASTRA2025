import time
import serial

# Pins of servos must be set up in the arduino code, while in python code the letter corresponding to each servo must be specified.
#A
#B
#C
#D - clamp servo in the current setup
CLAMP_SIGNAL='D'

# Clamp is closed at ≈50º, we assume that the open position is ≈100º


def clamp_open():
    send_text(CLAMP_SIGNAL, 100)

def clamp_close():
    send_text(CLAMP_SIGNAL, 42)

def send_text(servo_code, angle):
    ser.write((servo_code + str(angle) + '\n').encode())

ser = serial.Serial('/dev/ttyACM0', 9600)  # open serial port
time.sleep(3)
print(ser.name)

ser.close()


