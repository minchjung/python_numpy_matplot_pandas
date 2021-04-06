## TrackBar 
import numpy as np 
import cv2 
# 변환용 콜백함수 
def change_color(x):
    r = cv2.getTrackbarPos("R", "IMAGE") 
    g = cv2.getTrackbarPos("G", "IMAGE")
    b = cv2.getTrackbarPos("B", "IMAGE")
    image[:]=[b,g,r] # 전체 행렬에 모두 적용
    cv2.imshow("IMAGE",image)
# 600x400x rgb값d에, int8 타입으로 모든 요소에 0값으로 넘파이객체 생성
image = np.zeros((600,400,3), np.uint8)
# openCV 윈도우창 이름 설정해 만들고 
cv2.namedWindow("IMAGE")
# openCV 트랙바를 각각 생성한 윈도우창에 만들어준다 
# bar이름,'윈도우창이름',0부터,255까지,콜백함수
cv2.createTrackbar("R", "IMAGE",0,255,change_color) 
cv2.createTrackbar("G", "IMAGE",0,255,change_color) 
cv2.createTrackbar("B", "IMAGE",0,255,change_color) 
cv2.imshow('IMAGE',image)
cv2.waitKey(0)