import cv2
import numpy as np
cap = cv2.VideoCapture(0)
fourcc = cv2.VideoWriter_fourcc(*'DIVX')
out = cv2.VideoWriter('Video.avi', fourcc,20,(640,480))

while True:
    ret, frame = cap.read()
    flip = cv2. flip(frame, 0)
    cv2.imshow('Camera feed', frame)
    cv2.imshow('Flipped feed',flip)
    out.write(flip)
    if cv2.waitKey(1) == 27:
        break
cap.release()
out.release()
cv2.destroyAllWindows()
