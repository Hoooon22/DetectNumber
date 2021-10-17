import cv2
import numpy as np
import matplotlib.pyplot as plt
import pytesseract

capture = cv2.VideoCapture(0)

# 비디오 매 프레임 처리
while True:
    ret, frame = capture.read()

    if not ret:
        break

    # GrayScale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # show Video
    cv2.imshow("VideoFrame", gray)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

capture.release()
cv2.destroyAllWindows()