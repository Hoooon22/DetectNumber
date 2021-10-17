import sys

import cv2

# 카메라 열기
capture = cv2.VideoCapture(0)
capture.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
capture.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

if not capture.isOpened():
    print("Could not open camera")
    exit()

# 영역 설정
x, y, w, h = 320, 240, 100, 100
rc = (x, y, w, h)

ret, frame = capture.read()

if not ret:
    print("Frame read failed")
    sys.exit()

roi = frame[y:y+h, x:x+w]
roi_hsv = cv2.cvtColor(roi, cv2.COLOR_BGR2HSV)

# calculate HS histogram
channels = [0, 1]
ranges = [0, 180, 0, 256]
hist = cv2.calcHist([roi_hsv], channels, None, [90, 128], ranges)

# CamShift algorithm exit stat
term_crit = (cv2.TERM_CRITERIA_EPS | cv2.TERM_CRITERIA_COUNT, 10, 1)

# Camera frame
while True:
    ret, frame = capture.read()

    if not ret:
        break

    # back projection of HS histogram
    frame_hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    backproj = cv2.calcBackProject([frame_hsv], channels, hist, ranges, 1)

    # CamShift
    ret, rc = cv2.CamShift(backproj, rc, term_crit)

    # print trace result
    cv2.rectangle(frame, rc, (0, 0, 255), 2)
    # drawing circle
    cv2.ellipse(frame, ret, (0, 255, 0), 2)
    cv2.imshow('frame', frame)

    if cv2.waitKey(60) == 27:
        break

# release resources
capture.release()
cv2.destroyAllWindows()