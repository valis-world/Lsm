# LSM: Lego Sorting Machine

The Lego Sorting Machine (LSM) is a project designed to sort not only Lego bricks but also other objects based on color automatically. It consists of a Raspberry Pi 5 and an Arduino Uno communicating via a serial bus. The Arduino controls the stepper motors responsible for sorting the objects, while the Raspberry Pi processes images captured by the webcam in the scanning box.
# Files:

scanning.py: This Python script runs on the Raspberry Pi and is responsible for capturing images and processing them to identify objects by color.
sorting.ino: This Arduino sketch is uploaded to the Arduino Uno and controls the stepper motors based on commands received from the Raspberry Pi.
other_files/: This directory contains additional files used for fine-tuning, development, and supporting the main functionality of the Lego Sorting Machine.

# How it works:

Image Capture: The webcam installed in the scanning box captures images of objects placed inside.
Image Processing: The Raspberry Pi analyzes the captured images using the scanning.py script to identify the color of each object.
Communication: The Raspberry Pi sends commands to the Arduino Uno via a serial bus, instructing it to move the stepper motors to sort the identified objects by color.
Sorting: The Arduino Uno receives commands from the Raspberry Pi and controls the stepper motors accordingly, sorting the objects into designated bins based on their colors.

This project aims to automate the sorting process of objects by color, making it efficient and convenient for various applications beyond just Lego bricks.
