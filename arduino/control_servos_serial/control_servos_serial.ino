#include <Servo.h>

Servo servo1; // A
Servo servo2; // B
Servo servo3; // C

String inputString = "";
char servoId = 0;

void setup() {
  servo1.attach(9);
  servo2.attach(10);
  servo3.attach(11); 

  Serial.begin(9600);
}

void loop() {
  while (Serial.available()) {
    char inChar = (char)Serial.read();

    if (servoId == 0 && (inChar == 'A' || inChar == 'B' || inChar == 'C')) {
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
      }

      Serial.println(angle);
      inputString = "";
      servoId = 0;
    }
  }
}
