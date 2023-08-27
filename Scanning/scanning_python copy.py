import cv2
import serial
import time
import numpy as np

ser = serial.Serial('COM1', 9600)  # replace COM3 with the port where your Arduino is connected
time.sleep(2)

cap = cv2.VideoCapture(1)  # replace 1 with the index of your external webcam

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
    
    print (np.count_nonzero(mask_blue))
    print (np.count_nonzero(mask_yellow))
    print (np.count_nonzero(mask_red))
    
    # find contours in the thresholded images
    contours_blue, _ = cv2.findContours(mask_blue, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    contours_yellow, _ = cv2.findContours(mask_yellow, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    contours_red, _ = cv2.findContours(mask_red, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    
    # check if blue color is dominant and there is a large blue contour
    if len(contours_blue) > len(contours_yellow) and len(contours_red):
        for cnt in contours_blue:
            area = cv2.contourArea(cnt)
            if area > 1000:  # adjust the area threshold to detect larger or smaller objects
                data = 1
                ser.write(b'1')
                response = ser.read(1)
                print(response)
                time.sleep(2)
                break  # exit the loop after sending the data to the Arduino
    
    # check if yellow color is dominant and there is a large yellow contour
    elif len(contours_yellow) > len(contours_blue) and len(contours_red):
        for cnt in contours_yellow:
            area = cv2.contourArea(cnt)
            if area > 1000:
                data = 2
                ser.write(b'2')
                response = ser.read(1)
                print(response)
                time.sleep(2)
                break
    
    # check if red color is dominant and there is a large red contour
    elif len(contours_red) > len(contours_blue) and len(contours_yellow):
        for cnt in contours_red:
            area = cv2.contourArea(cnt)
            if area > 1000:
                data = 3
                ser.write(b'3')
                response = ser.read(1)
                print(response)
                time.sleep(2)
                break
    
    cv2.imshow('frame', frame)
    
    # press 'q' to exit the program
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
ser.close()
