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

    # Maximize Contrast
    structuringElement = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3))

    imgTopHat = cv2.morphologyEx(gray, cv2.MORPH_TOPHAT, structuringElement)
    imgBlackHat = cv2.morphologyEx(gray, cv2.MORPH_BLACKHAT, structuringElement)

    imgGrayscalePlusTopHat = cv2.add(gray, imgTopHat)
    gray = cv2.subtract(imgGrayscalePlusTopHat, imgBlackHat)

    # Adaptive Thresholding
    img_blurred = cv2.GaussianBlur(gray, ksize=(5, 5), sigmaX=0)

    img_thresh = cv2.adaptiveThreshold(
        img_blurred,
        maxValue=255.0,
        adaptiveMethod=cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
        thresholdType=cv2.THRESH_BINARY_INV,
        blockSize=19,
        C=9
    )


    # show Video
    cv2.imshow("VideoFrame", img_thresh)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

capture.release()
cv2.destroyAllWindows()