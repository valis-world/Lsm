
#include <Stepper.h>

const float STEPS_PER_REV = 32;
const float GEAR_RED = 64;
const float STEPS_PER_OUT_REV = STEPS_PER_REV * GEAR_RED;

int StepsRequired;

void setup() {
  Serial.begin(9600);
  Stepper steppermotor(STEPS_PER_REV, 8, 10, 9, 11);
  steppermotor.setSpeed(1000);
}

void loop() {
  if (Serial.available() > 0) {
    char serialData = Serial.read();
    Serial.print(serialData);

    if (serialData == '1') {
      StepsRequired = 2000;
      Stepper steppermotor(STEPS_PER_REV, 8, 10, 9, 11);
      steppermotor.setSpeed(1000);
      steppermotor.step(StepsRequired);
    }
    if (serialData == '2') {
      StepsRequired = -2000;
      Stepper steppermotor(STEPS_PER_REV, 8, 10, 9, 11);
      steppermotor.setSpeed(1000);
      steppermotor.step(StepsRequired);
    }
    if (serialData == '3') {
      StepsRequired = 1453;
      Stepper steppermotor(STEPS_PER_REV, 8, 10, 9, 11);
      steppermotor.setSpeed(1000);
      steppermotor.step(StepsRequired);
    }
  }
}
