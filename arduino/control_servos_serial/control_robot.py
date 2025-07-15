import time
import serial

ser = serial.Serial('/dev/ttyACM0', 9600)  # open serial port
time.sleep(3)

def send_text(servo_code, angle):
    ser.write((servo_code + str(angle) + '\n').encode())


# Pins of servos must be set up in the arduino code, while in python code the letter corresponding to each servo must be specified.
#A - is the servo that control rotation of the whole arm (movement left-right)
LR_SIGNAL='A'
#B
#C
#D - clamp servo in the current setup
CLAMP_SIGNAL='D'
def clamp_open():
    send_text(CLAMP_SIGNAL, 100)

def clamp_close():
    send_text(CLAMP_SIGNAL, 42)

# Clamp is closed at ≈50º, we assume that the open position is ≈100º


print(ser.name)

ser.close()


