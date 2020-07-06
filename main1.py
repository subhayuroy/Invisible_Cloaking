import cv2
import time
import numpy as np

fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('output.avi', fourcc, 20.0, (640, 480))

cap = cv2.VideoCapture(0)
time.sleep(5)
count = 0
background = 0

for i in range(60):
    ret, background = cap.read()

background = np.flip(background, axis=1)

while (cap.isOpened()):
    ret, image = cap.read()
    if not ret:
        break
    count += 1