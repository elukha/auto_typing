import cv2

im = cv2.imread('C:\\Users\\User\\Desktop\\typing\\image.png')

th, im_th = cv2.threshold(im, 128, 255, cv2.THRESH_BINARY)

print(th)
# 128.0

cv2.imwrite('./opencv_th.jpg', im_th)