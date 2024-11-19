import cv2

# 이미지 읽기 및 그레이스케일 변환
image = cv2.imread('Plate.jpg', cv2.IMREAD_GRAYSCALE)

# 이미지 크기 축소 (가로, 세로 크기의 50%로 축소)
small_image = cv2.resize(image, (0, 0), fx=0.5, fy=0.5)
# Otsu의 이진화 적용
_, binary_image = cv2.threshold(small_image, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

# 결과 출력
cv2.imshow('Original Image', small_image)
cv2.imshow('Binary Thresholded Image', binary_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
