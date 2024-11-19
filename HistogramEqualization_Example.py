import cv2

# 이미지 읽기 및 그레이스케일 변환
image = cv2.imread('night_room.jpg', cv2.IMREAD_GRAYSCALE)
small_image = cv2.resize(image, (0, 0), fx=0.5, fy=0.5)

# 히스토그램 균일화 적용
equalized_image = cv2.equalizeHist(small_image)

# 결과 출력
cv2.imshow('Original Image', small_image)
cv2.imshow('Histogram Equalized Image', equalized_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
