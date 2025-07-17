import time
import serial

# Initializing serial
ser = serial.Serial('/dev/ttyACM0', 9600)
time.sleep(3) # Gotta wait 3 second to make sure the connection is established

def send_text(servo_code, angle):
    ser.write((servo_code + str(angle) + '\n').encode())


# Pins of servos must be set up in the arduino code, while in python code the letter corresponding to each servo must be specified.
#A - is the servo that control rotation of the whole arm (movement left-right)
LR_SIGNAL='A'
#B
#C - is the server that control the up-down movements of the arm
UPDOWN_SIGNAL='C'
def up():
    send_text(UPDOWN_SIGNAL, 180)

def down():
    send_text(UPDOWN_SIGNAL, 70)

#D - clamp servo in the current setup
CLAMP_SIGNAL='D'
def clamp_open():
    send_text(CLAMP_SIGNAL, 100)

def clamp_close():
    send_text(CLAMP_SIGNAL, 42)

# Clamp is closed at ≈50º, we assume that the open position is ≈100º


print(ser.name)

while True:
    up()
    time.sleep(0.5)
    clamp_open()
    time.sleep(2)
    down()
    time.sleep(0.5)
    clamp_close()
    time.sleep(2)

ser.close()