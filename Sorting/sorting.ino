#include <Stepper.h>

const int STEPS_PER_REV = 32;
const int GEAR_RED = 64;
const int STEPS_PER_OUT_REV = STEPS_PER_REV * GEAR_RED;

Stepper steppermotor(STEPS_PER_REV, 8, 10, 9, 11);
int current_position = 0;

void setup() {
  Serial.begin(9600);
  steppermotor.setSpeed(1000);
  moveToPosition(3);  // Start at the white (home) position
}

void loop() {
  if (Serial.available() > 0) {
    char serialData = Serial.read();

    if (serialData == '1') {
      moveToPosition(1);  // Blue Box
      delay(2000);        // Wait for 2 seconds
      moveToPosition(3);  // Return to White (Home) position
      delay(2000);        // Wait for 2 seconds
      Serial.write('D');  // Send confirmation
    } else if (serialData == '2') {
      moveToPosition(2);  // Yellow Box
      delay(2000);
      moveToPosition(3);
      delay(2000);
      Serial.write('D');
    } else if (serialData == '3') {
      moveToPosition(0);  // Red Box
      delay(2000);
      moveToPosition(3);
      delay(2000);
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
