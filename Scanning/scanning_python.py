import cv2
import serial
import time
import numpy as np

ser = serial.Serial('COM1', 9600)  # replace COM3 with the port where your Arduino is connected
time.sleep(2)

cap = cv2.VideoCapture(1)  # replace 1 with the index of your external webcam

last_update = 0

while True:
    ret, frame = cap.read()
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    
    # define range of blue color in HSV
    lower_blue = np.array([100, 50, 50])
    upper_blue = np.array([130, 255, 255])
    
    # define range of yellow color in HSV
    lower_yellow = np.array([20, 100, 100])
    upper_yellow = np.array([30, 255, 255])
    
    # define range of red color in HSV
    lower_red = np.array([0, 70, 50])
    upper_red = np.array([10, 255, 255])

    
    # threshold the HSV image to get only blue colors
    mask_blue = cv2.inRange(hsv, lower_blue, upper_blue)
    
    # threshold the HSV image to get only yellow colors
    mask_yellow = cv2.inRange(hsv, lower_yellow, upper_yellow)
    
    # threshold the HSV image to get only red colorsqq
    mask_red = cv2.inRange(hsv, lower_red, upper_red)
    
    cv2.imshow("Blue Mask", mask_blue)
    cv2.imshow("Yellow Mask", mask_yellow)
    cv2.imshow("Red Mask", mask_red)
    
    count_blue = np.count_nonzero(mask_blue)
    count_yellow = np.count_nonzero(mask_yellow)
    count_red = np.count_nonzero(mask_red)
    
    if time.perf_counter() - last_update > 2:
    
        if (count_blue >= count_yellow) and (count_blue >= count_red):
            if count_blue > 500:
                data = 1
                ser.write(b'1')
                response = ser.read(1)
                print(response)
                last_update = time.perf_counter()
        
        elif (count_yellow >= count_blue) and (count_yellow >= count_red):
            if count_yellow > 500:
                data = 2
                ser.write(b'2')
                response = ser.read(1)
                print(response)
                last_update = time.perf_counter()
        
        elif (count_red >= count_blue) and (count_red >= count_yellow):
            if count_red > 500:
                data = 3
                ser.write(b'3')
                response = ser.read(1)
                print(response)
                last_update = time.perf_counter()
    
    cv2.imshow('frame', frame)
    
    # press 'q' to exit the program
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
ser.close()
