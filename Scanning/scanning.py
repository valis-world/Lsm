import cv2
import serial 
import time
import numpy as np

ser = serial.Serial('/dev/ttyACM0', 9600)  # replace COM3 with the port where your Arduino is connected

time.sleep(2)

cap = cv2.VideoCapture(0)  # replace 1 with the index of your external webcam

last_update = 0

def wait_for_confirmation(expected_response):
    response = ser.read(1)
    if response == expected_response.encode():
        print(f"Received confirmation: {response}")
    else:
        print("Confirmation not received")

while True:
    ret, frame = cap.read()
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    
    # define range of blue color in HSV
    lower_blue = np.array([105, 195, 80])
    upper_blue = np.array([120, 225, 150])
    
    # define range of yellow color in HSV 
    lower_yellow = np.array([18, 180, 135])
    upper_yellow = np.array([25, 225, 225])
    
    # define range of red color in HSV 
    lower_red = np.array([0, 185, 125])
    upper_red = np.array([5, 250, 200])

    # define range of green color in HSV
    lower_green = np.array([60, 160, 60])
    upper_green = np.array([75, 210, 80])

    # define range of light_gray color in HSV
    lower_light_gray = np.array([0, 10 , 90])
    upper_light_gray = np.array([180, 30, 125])

    # threshold the HSV image to get only blue colors
    mask_blue = cv2.inRange(hsv, lower_blue, upper_blue)
    
    # threshold the HSV image to get only yellow colors
    mask_yellow = cv2.inRange(hsv, lower_yellow, upper_yellow)
    
    # threshold the HSV image to get only red colorsqq
    mask_red = cv2.inRange(hsv, lower_red, upper_red)

    # threshold the HSV image to get obly green colors
    mask_green = cv2.inRange(hsv, lower_green, upper_green)

    # threshold the HSV image to get obly ligh_gray colors tuning required
    mask_light_gray = cv2.inRange(hsv, lower_light_gray, upper_light_gray)
    
    cv2.imshow("Blue Mask", mask_blue)
    cv2.imshow("Yellow Mask", mask_yellow)
    cv2.imshow("Red Mask", mask_red)
    cv2.imshow("Green Mask", mask_green)
    cv2.imshow("Light Gray Mask", mask_light_gray)
    
    count_blue = np.count_nonzero(mask_blue)
    count_yellow = np.count_nonzero(mask_yellow)
    count_red = np.count_nonzero(mask_red)
    count_green = np.count_nonzero(mask_green)
    count_light_gray = np.count_nonzero(mask_light_gray)
    
    if time.perf_counter() - last_update > 2:
        if (count_blue >= count_yellow) and (count_blue >= count_red) and (count_blue >= count_green):
            if count_blue > 500:
                data = 1
                ser.write(b'1')
                wait_for_confirmation('A')
                print("Blue detected")
                last_update = time.perf_counter()
        
        elif (count_yellow >= count_blue) and (count_yellow >= count_red) and (count_yellow >= count_green) and (count_blue >= count_blue):
            if count_yellow > 500:
                data = 2
                ser.write(b'2')
                wait_for_confirmation('A')
                print("Yellow detected")
                last_update = time.perf_counter()
        
        elif (count_red >= count_blue) and (count_red >= count_yellow) and (count_red >= count_green) and (count_red >= count_light_gray):
            if count_red > 500:
                data = 3
                ser.write(b'3')
                wait_for_confirmation('A')
                print("Red detected")
                last_update = time.perf_counter()

        elif (count_green >= count_blue) and (count_green >= count_yellow) and (count_green >= count_red) and (count_green >= count_light_gray):
            if count_green > 500:
                data = 4
                ser.write(b'4')
                wait_for_confirmation('A')
                print("Green detected")
                last_update = time.perf_counter()

        elif (count_light_gray >= count_blue) and (count_light_gray >= count_yellow) and (count_light_gray >= count_red) and (count_light_gray >= count_green):
            if count_green > 500:
                data = 5
                ser.write(b'5')
                wait_for_confirmation('A')
                print("Green detected")
                last_update = time.perf_counter()
    
    cv2.imshow('frame', frame)
    
    # press 'q' to exit the program
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
ser.close()