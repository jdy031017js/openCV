import cv2

# 이미지 읽기
image = cv2.imread('city.jpg')

# 이미지 크기 축소 (가로, 세로 크기의 50%로 축소)
small_image = cv2.resize(image, (0, 0), fx=0.5, fy=0.5)

# Gaussian Blur 적용
blurred_image = cv2.GaussianBlur(small_image, (5, 5), 0)

# 원본 이미지와 블러 처리된 이미지 동시에 표시
cv2.imshow('Original Image (Small)', small_image)
cv2.imshow('Gaussian Blurred Image (Small)', blurred_image)

# 키 입력 대기
cv2.waitKey(0)
cv2.destroyAllWindows()
