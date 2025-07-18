import time
import serial

class RobotController:
    # Constants for servo signals
    FB_SIGNAL = 'B'  # servo that controls movements forward and backward
    UPDOWN_SIGNAL = 'C'  # servo that controls the up-down movements of the arm
    CLAMP_SIGNAL = 'D'  # clamp servo

    # Angle limits
    MIN_ANGLE = 10
    MAX_ANGLE = 160
    STEP_SIZE = 10

    def __init__(self, port, baud_rate=9600):
        """Initialize the robot controller with a specified port.

        Args:
            port (str): Serial port connected to the Arduino (default: '/dev/ttyACM0')
            baud_rate (int): Baud rate for serial communication (default: 9600)
        """
        self.ser = serial.Serial(port, baud_rate)
        time.sleep(3)  # Wait to ensure the connection is established
        print(f"Connected to {self.ser.name}")

        # Initialize current positions
        self.fb_position = 90  # Starting at middle position
        self.updown_position = 90  # Starting at middle position

        # Add a small delay before sending initial commands
        time.sleep(0.5)

        # Set servos to initial positions
        self.send_text(self.FB_SIGNAL, self.fb_position)
        self.send_text(self.UPDOWN_SIGNAL, self.updown_position)

    def send_text(self, servo_code, angle):
        """Send command to servo via serial.

        Args:
            servo_code (str): Single character code for the servo
            angle (int): Angle to set the servo to (0-180)
        """
        # Ensure angle is within allowed limits
        angle = max(self.MIN_ANGLE, min(self.MAX_ANGLE, angle))
        self.ser.write((servo_code + str(angle) + '\n').encode())
        return angle  # Return the actual angle sent (after constraining)

    def up(self):
        """Move the arm up by 10 degrees within limits."""
        self.updown_position = min(self.MAX_ANGLE, self.updown_position + self.STEP_SIZE)
        self.send_text(self.UPDOWN_SIGNAL, self.updown_position)
        return self.updown_position

    def down(self):
        """Move the arm down by 10 degrees within limits."""
        self.updown_position = max(self.MIN_ANGLE, self.updown_position - self.STEP_SIZE)
        self.send_text(self.UPDOWN_SIGNAL, self.updown_position)
        return self.updown_position

    def clamp_open(self):
        """Open the clamp."""
        self.send_text(self.CLAMP_SIGNAL, 100)

    def clamp_close(self):
        """Close the clamp."""
        self.send_text(self.CLAMP_SIGNAL, 42)

    def forward(self):
        """Move the arm forward by 10 degrees within limits."""
        self.fb_position = min(self.MAX_ANGLE, self.fb_position + self.STEP_SIZE)
        self.send_text(self.FB_SIGNAL, self.fb_position)
        return self.fb_position

    def backward(self):
        """Move the arm backward by 10 degrees within limits."""
        self.fb_position = max(self.MIN_ANGLE, self.fb_position - self.STEP_SIZE)
        self.send_text(self.FB_SIGNAL, self.fb_position)
        return self.fb_position

    def set_forward_backward(self, angle):
        """Set the forward-backward position to a specific angle within limits."""
        self.fb_position = max(self.MIN_ANGLE, min(self.MAX_ANGLE, angle))
        self.send_text(self.FB_SIGNAL, self.fb_position)
        return self.fb_position

    def set_up_down(self, angle):
        """Set the up-down position to a specific angle within limits."""
        self.updown_position = max(self.MIN_ANGLE, min(self.MAX_ANGLE, angle))
        self.send_text(self.UPDOWN_SIGNAL, self.updown_position)
        return self.updown_position

    def close(self):
        """Close the serial connection."""
        self.ser.close()
        print("Serial connection closed.")

# Example usage
if __name__ == "__main__":
    # Create a robot controller with default port
    robot = RobotController("/dev/ttyACM0")

    # Example of incremental movements
    print("Moving forward in steps:")
    for _ in range(3):
        position = robot.forward()
        print(f"New position: {position}")
        time.sleep(0.5)

    print("Moving up in steps:")
    for _ in range(3):
        position = robot.up()
        print(f"New position: {position}")
        time.sleep(0.5)

    # Close connection
    robot.close()
