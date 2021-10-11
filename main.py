import cv2

# 카메라 열기
capture = cv2.VideoCapture(0)
capture.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
capture.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

if not capture.isOpened():
    print("Could not open camera")
    exit()

# 프레임 반복
while capture.isOpened():
    
    # 프레임 읽기
    status, frame = capture.read()
    cv2.imshow("VideoFrame", frame)

# release resources
capture.release()
cv2.destroyAllWindows()