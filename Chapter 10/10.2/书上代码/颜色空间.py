import cv2
img_data = cv2.imread('empire.jpg')
cv2.cvtColor(img_data, cv2.COLOR_BGR2GRAY)
