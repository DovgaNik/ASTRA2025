import time
import serial

class RobotController:
    # Constants for servo signals
    LR_SIGNAL = 'A'  # servo that controls rotation of the whole arm (movement left-right)
    FB_SIGNAL = 'B'  # servo that controls movements forward and backward
    UPDOWN_SIGNAL = 'C'  # servo that controls the up-down movements of the arm
    CLAMP_SIGNAL = 'D'  # clamp servo

    def __init__(self, port, baud_rate=9600):
        """Initialize the robot controller with a specified port.

        Args:
            port (str): Serial port connected to the Arduino (default: '/dev/ttyACM0')
            baud_rate (int): Baud rate for serial communication (default: 9600)
        """
        self.ser = serial.Serial(port, baud_rate)
        time.sleep(3)  # Wait to ensure the connection is established
        print(f"Connected to {self.ser.name}")

    def send_text(self, servo_code, angle):
        """Send command to servo via serial.

        Args:
            servo_code (str): Single character code for the servo
            angle (int): Angle to set the servo to (0-180)
        """
        self.ser.write((servo_code + str(angle) + '\n').encode())

    def left(self):
        """Move the arm to the left position (180 degrees)."""
        self.send_text(self.LR_SIGNAL, 180)

    def right(self):
        """Move the arm to the right position (0 degrees)."""
        self.send_text(self.LR_SIGNAL, 0)

    def center(self):
        """Center the arm (90 degrees)."""
        self.send_text(self.LR_SIGNAL, 90)

    def up(self):
        """Move the arm up."""
        self.send_text(self.UPDOWN_SIGNAL, 160)

    def down(self):
        """Move the arm down."""
        self.send_text(self.UPDOWN_SIGNAL, 70)

    def clamp_open(self):
        """Open the clamp."""
        self.send_text(self.CLAMP_SIGNAL, 100)

    def clamp_close(self):
        """Close the clamp."""
        self.send_text(self.CLAMP_SIGNAL, 42)

    def forward(self):
        """Move the arm forward."""
        self.send_text(self.FB_SIGNAL, 160)  # Assuming forward is at 160 degrees

    def backward(self):
        """Move the arm backward."""
        self.send_text(self.FB_SIGNAL, 20)  # Assuming backward is at 20 degrees

    def close(self):
        """Close the serial connection."""
        self.ser.close()
        print("Serial connection closed.")

# Example usage
if __name__ == "__main__":
    # Create a robot controller with default port
    robot = RobotController()

    # Example movements
    robot.left()
    time.sleep(1)
    robot.right()
    time.sleep(1)
    robot.center()

    # Close connection
    robot.close()
