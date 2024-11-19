import cv2
import numpy as np

# 컬러 이미지 읽기
image = cv2.imread('tree.jpg')

# 커널 생성
kernel = np.ones((5, 5), np.uint8)

# 각 채널 분리 (BGR 채널)
b, g, r = cv2.split(image)

# 각 채널에 열기 연산 적용
b_open = cv2.morphologyEx(b, cv2.MORPH_OPEN, kernel)
g_open = cv2.morphologyEx(g, cv2.MORPH_OPEN, kernel)
r_open = cv2.morphologyEx(r, cv2.MORPH_OPEN, kernel)

# 채널 병합
opened_image = cv2.merge((b_open, g_open, r_open))

# 결과 출력
cv2.imshow('Original Color Image', image)
cv2.imshow('Opened Color Image', opened_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
