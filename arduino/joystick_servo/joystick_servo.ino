#include <Servo.h>

#define ANALOG_X1_PIN A0
#define ANALOG_Y1_PIN A1
#define ANALOG_X2_PIN A2
#define ANALOG_Y2_PIN A3
	 
#define ANALOG_X1_CORRECTION 108
#define ANALOG_Y1_CORRECTION 106
#define ANALOG_X2_CORRECTION 111
#define ANALOG_Y2_CORRECTION 109
	 
struct analog { 
	  float x, y; 
}; 

Servo servo1;
Servo servo2;
Servo servo3;

void setup() 
{ 
	 Serial.begin(9600); 
   servo1.attach(2);
   servo2.attach(3);
   servo3.attach(4);
} 
	 
void loop() 
{ 
	analog analog1;
  analog analog2; 
	 
	analog1.x = readAnalogAxisLevel(ANALOG_X1_PIN) - ANALOG_X1_CORRECTION; 
	analog1.y = readAnalogAxisLevel(ANALOG_Y1_PIN) - ANALOG_Y1_CORRECTION; 

  analog2.x = readAnalogAxisLevel(ANALOG_X2_PIN) - ANALOG_X2_CORRECTION; 
	analog2.y = readAnalogAxisLevel(ANALOG_Y2_PIN) - ANALOG_Y2_CORRECTION; 

  Serial.print("x_1 = ");
  Serial.println(analog1.x);

  Serial.print("y_1 = ");
  Serial.println(analog1.y);

  Serial.print("x_2 = ");
  Serial.println(analog2.x);

  Serial.print("y_2 = ");
  Serial.println(analog2.y);

  float pos_servo1;
  if (analog1.x == 0) {
    pos_servo1 = 90;
  } else {
    if (analog1.x > 0) {
      pos_servo1 = ((analog1.x / 112.0) * 90) + 90;
    } else {
      pos_servo1 = ((analog1.x / 108.0) * 90) + 90;
    }
  }
  servo1.write(pos_servo1);
  Serial.print("Requested position 1 = ");
  Serial.println(pos_servo1);


  float pos_servo2;
  if (analog1.y == 0) {
    pos_servo2 = 90;
  } else {
    if (analog1.y > 0) {
      pos_servo2 = ((analog1.y / 114.0) * 90) + 90;
    } else {
      pos_servo2 = ((analog1.y / 106.0) * 90) + 90;
    }
  }
  servo2.write(pos_servo2);
  Serial.print("Requested position 2 = ");
  Serial.println(pos_servo2);


  float pos_servo3;
  if (analog2.x == 0) {
    pos_servo3 = 90;
  } else {
    if (analog2.x > 0) {
      pos_servo3 = ((analog2.x / 109.0) * 90) + 90;
    } else {
      pos_servo3 = ((analog2.x / 111.0) * 90) + 90;
    }
  }
  servo3.write(pos_servo3);
  Serial.print("Requested position 3 = ");
  Serial.println(pos_servo3);
} 
	 
byte readAnalogAxisLevel(int pin) 
{ 
  return map(analogRead(pin), 0, 1023, 0, 255); 
} 
