#include <Servo.h>
// 5 9 6
Servo servo1; // B
Servo servo2; // C
Servo servo3; // D

String inputString = "";
char servoId = 0;

void setup() {
  servo1.attach(5);
  servo2.attach(9);
  servo3.attach(6);

  Serial.begin(9600);
}

void loop() {
  while (Serial.available()) {
    char inChar = (char)Serial.read();

    if (servoId == 0 && (inChar == 'B' || inChar == 'C' || inChar == 'D')) {
      servoId = inChar;
      inputString = "";
    } else if (isDigit(inChar)) {
      inputString += inChar;
    } else if ((inChar == '\n' || inChar == '\r') && inputString.length() > 0 && servoId != 0) {
      int angle = inputString.toInt();
      angle = constrain(angle, 10, 160);

      switch (servoId) {
        case 'B':
          servo1.write(angle);
          break;
        case 'C':
          servo2.write(angle);
          break;
        case 'D':
          servo3.write(angle);
          break;
      }

      Serial.println(angle);
      inputString = "";
      servoId = 0;
    }
  }
}
