# https://www.youtube.com/watch?v=rKcwcARdg9M&list=WL&index=5
# https://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_gui/py_video_display/py_video_display.html
# https://github.com/techwithtim/OpenCV-Tutorials/blob/main/tutorial3.py

import cv2
import numpy as np

# scale factor for smaller_frame
print("WEBCAM chessboard generator")
xx = float(input("How many windows per side of the chessboard do you want n * n ?"))
print("The number of windows per side requested is: ", xx)
scala = ((100/xx) / 100)
print("SCALE is", scala)

# object to acquire the webacam
cap = cv2.VideoCapture(0)
print("To close window press Q ")
while True:
    ret, frame = cap.read()
    # values of width and height of the webcam window
    width = int(cap.get(3))
    height = int(cap.get(4))
    # width and height of smaller_frame
    swidth = int(width * scala)
    sheight = int(height * scala)

    # empty black image (ARRAY fo zeros) with dimensions of smaller_frame * scale factor
    image = np.zeros(((sheight * int(xx)),(swidth * int(xx)),3), np.uint8)

    # smaller_frame made resizing the webcam capture
    smaller_frame = cv2.resize(frame, (0, 0), fx=scala, fy=scala)
    #counter sheight (movement on Y axis)
    sh = 0

    # inserting smalle_frame inside empty black image
    for x in range(int(xx)):
        # counter swidht (movement on X axis)
        sw = 0
        for x in range(int(xx)):
            image[sh : (sheight + sh), sw : (swidth + sw)] = smaller_frame
            # for debugging
            # print( sh, ":", (sheight + sh),",", sw, ":", (swidth + sw), "= smaller_frame")

            # increase counter
            sw = sw + swidth

        # increase counter
        sh = sh + sheight

    # show the image
    cv2.imshow("WEBCAM CHESSBOARD", image)

    # to exit WHILE loop press Q
    if cv2.waitKey(1) == ord("q"):
        break

# release webcam and close all windows
cap.release()
cv2.destroyAllWindows()
