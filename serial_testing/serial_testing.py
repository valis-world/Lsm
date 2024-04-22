import serial
import time

ser = serial.Serial('/dev/ttyACM0', 9600)

# Wait for a moment to ensure the serial connection is established
time.sleep(2)

try:
    while True:
        # Send data to Arduino
        data = input("Enter command (1, 2, 3, 4, or 5): ")
        ser.write(data.encode())
        
        # Wait for a short time before sending the next command
        time.sleep(2)

except KeyboardInterrupt:
    print("\nExiting...")
    ser.close()
