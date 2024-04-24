#include <AccelStepper.h>

const int STEPS_PER_REV = 32;
const int GEAR_RED = 64;
const int STEPS_PER_OUT_REV = STEPS_PER_REV * GEAR_RED;

// Define stepper motors and their pin configurations
AccelStepper stepper1(5, A0, A1, A2, A3);
AccelStepper stepper2(5, 6, 7, 8, 9);
AccelStepper stepper3(5, 10, 11, 12, 13);
AccelStepper stepper4(5, 2, 3, 4, 5);

void setup() {
  Serial.begin(9600);

  // Set maximum speed and acceleration for each stepper motor
  stepper1.setMaxSpeed(1000.0);
  stepper1.setAcceleration(1000.0);

  stepper2.setMaxSpeed(1000.0);
  stepper2.setAcceleration(1000.0);

  stepper3.setMaxSpeed(1000.0);
  stepper3.setAcceleration(1000.0);

  stepper4.setMaxSpeed(500.0); // Set speed for stepper 4 to 500 steps per second
  stepper4.setAcceleration(1000.0);

  // Move stepper 1 to position 0
  stepper1.moveTo(0);
  stepper1.runToPosition();

  // Set the speed for steppers 2 and 3 to 1000 steps per second
  stepper2.setSpeed(1000.0);
  stepper3.setSpeed(1000.0);

  // Set the speed for stepper 4 to 500 steps per second
  stepper4.setSpeed(500.0);
}

void loop() {
  // If serial data is available, read it and move stepper 1 accordingly
  if (Serial.available() > 0) {
    char serialData = Serial.read();
    switch (serialData) {
      case '1':
        moveStepper(stepper1, 1);
        break;
      case '2':
        moveStepper(stepper1, 2);
        break;
      case '3':
        moveStepper(stepper1, 3);
        break;
      case '4':
        moveStepper(stepper1, 4);
        break;
      case '5':
        moveStepper(stepper1, 5);
        break;
      default:
        break;
    }
  }

  // Run steppers 2, 3, and 4 continuously
  stepper2.runSpeed();
  stepper3.runSpeed();
  stepper4.runSpeed();
}

// Function to move stepper 1 to a specified position
void moveStepper(AccelStepper &stepper, int position) {
  int targetPosition = position * (STEPS_PER_OUT_REV / 6); // Divide by 6 since there are 6 positions

  // Move the stepper motor to the target position and wait for it to complete
  stepper.moveTo(targetPosition);
  stepper.runToPosition();

  // Run steppers 2 and 3 during the wait time
  unsigned long startTime = millis();
  while (millis() - startTime < 2000) {
    stepper2.runSpeed();
    stepper3.runSpeed();
    stepper4.runSpeed();
  }

  // Return the stepper motor to position 0
  stepper.moveTo(0);
  stepper.runToPosition();

  // Send confirmation
  Serial.write('D');
}
