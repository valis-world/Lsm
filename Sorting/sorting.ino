#include <Stepper.h>
#define vcc2 2
#define gnd2 1

const int STEPS_PER_REV = 32;
const int GEAR_RED = 64;
const int STEPS_PER_OUT_REV = STEPS_PER_REV * GEAR_RED;

Stepper steppermotor(STEPS_PER_REV, 8, 10, 9, 11);
int current_position = 0;

void setup() {
  Serial.begin(9600);
  steppermotor.setSpeed(1000);
  moveToPosition(3);  // Start at the white (home) position
  pinMode(vcc2,OUTPUT);
  digitalWrite(vcc2 ,HIGH);
  pinMode(gnd2,OUTPUT);
  digitalWrite(gnd2 ,LOW);

}

void loop() {
  if (Serial.available() > 0) {
    char serialData = Serial.read();

    if (serialData == '1') {
      digitalWrite(vcc2 ,LOW);
      moveToPosition(1);  // Blue Box
      digitalWrite(vcc2 ,HIGH);
      delay(2000);  // Wait for 2 seconds
      digitalWrite(vcc2 ,LOW);
      moveToPosition(3);  // Return to White (Home) position
      digitalWrite(vcc2 ,HIGH);
      Serial.write('D');  // Send confirmation
    } else if (serialData == '2') {
      digitalWrite(vcc2 ,LOW);
      moveToPosition(2);  // Yellow Box
      digitalWrite(vcc2 ,HIGH);
      delay(2000);
      digitalWrite(vcc2 ,LOW);
      moveToPosition(3);
      digitalWrite(vcc2 ,HIGH);
      Serial.write('D');
    } else if (serialData == '3') {
      digitalWrite(vcc2 ,LOW);
      moveToPosition(0);  // Red Box
      digitalWrite(vcc2 ,HIGH);
      delay(2000);
      digitalWrite(vcc2 ,LOW);
      moveToPosition(3);
      digitalWrite(vcc2 ,HIGH);
      Serial.write('D');
    }
  }
}

void moveToPosition(int position) {
  int target_position = position * (STEPS_PER_OUT_REV / 4); // Divide by 4 since there are 4 positions
  
  if (target_position > current_position) {
    steppermotor.step(target_position - current_position);
  } else if (target_position < current_position) {
    steppermotor.step(-(current_position - target_position));
  }
  
  current_position = target_position;
}
