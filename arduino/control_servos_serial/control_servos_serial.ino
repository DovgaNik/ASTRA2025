#include <Servo.h>
// 3 5 9 6
Servo servo1; // A
Servo servo2; // B
Servo servo3; // C
Servo servo4;

String inputString = "";
char servoId = 0;

void setup() {
  servo1.attach(3);
  servo2.attach(5);
  servo3.attach(9); 
  servo4.attach(6);

  Serial.begin(9600);
}

void loop() {
  while (Serial.available()) {
    char inChar = (char)Serial.read();

    if (servoId == 0 && (inChar == 'A' || inChar == 'B' || inChar == 'C' || inChar == 'D')) {
      servoId = inChar;
      inputString = "";
    } else if (isDigit(inChar)) {
      inputString += inChar;
    } else if ((inChar == '\n' || inChar == '\r') && inputString.length() > 0 && servoId != 0) {
      int angle = inputString.toInt();
      angle = constrain(angle, 0, 180);

      switch (servoId) {
        case 'A':
          servo1.write(angle);
          break;
        case 'B':
          servo2.write(angle);
          break;
        case 'C':
          servo3.write(angle);
          break;
        case 'D':
          servo4.write(angle);
          break;
      }

      Serial.println(angle);
      inputString = "";
      servoId = 0;
    }
  }
}
