#include <AccelStepper.h>

const int STEPS_PER_REV = 32;
const int GEAR_RED = 64;
const int STEPS_PER_OUT_REV = STEPS_PER_REV * GEAR_RED;

AccelStepper stepper1(5, 0, 1, 2, 3);
AccelStepper stepper2(5, 4, 5, 6, 7);
AccelStepper stepper3(5, 8, 9, 10, 11);

int current_position = 0;

void setup() {
  Serial.begin(9600);

  stepper1.setMaxSpeed(1000.0); // Max speed of the first motor - modify if needed
  stepper1.setAcceleration(1000.0); // Acceleration rate of the first motor - modify if needed

  stepper2.setMaxSpeed(1000.0);
  stepper2.setAcceleration(1000.0);

  stepper3.setMaxSpeed(1000.0);
  stepper3.setAcceleration(1000.0);
}

void loop() {
  if (Serial.available() > 0) {
    char serialData = Serial.read();
    

    if (serialData == '1') {
      moveToPosition(1, stepper3);  // Move stepper3 to position 1
      delay(2000);  // Wait for 2 seconds
      moveToPosition(0, stepper3);  // Return to position 0
      Serial.write('D');  // Send confirmation
    } else if (serialData == '2') {
      moveToPosition(2, stepper3);  // Move stepper3 to position 2
      delay(2000);
      moveToPosition(0, stepper3);  // Return to position 0
      Serial.write('D');
    } else if (serialData == '3') {
      moveToPosition(3, stepper3);  // Move stepper3 to position 3
      delay(2000);
      moveToPosition(0, stepper3);  // Return to position 0
      Serial.write('D');
    }else if (serialData == '4') {
      moveToPosition(4, stepper3);  // Move stepper3 to position 4
      delay(2000);
      moveToPosition(0, stepper3);  // Return to position 0
      Serial.write('D');
    }else if (serialData == '5') {
      moveToPosition(5, stepper3);  // Move stepper3 to position 5
      delay(2000);
      moveToPosition(0, stepper3);  // Return to position 0
      Serial.write('D');
    }
    // Add more conditions for other stepper motors if needed
  }
}

void moveToPosition(int position, AccelStepper &stepper) {
  int target_position = position * (STEPS_PER_OUT_REV / 6); // Divide by 6 since there are 6 positions
  
  stepper.moveTo(target_position);
  stepper.runToPosition();
}
