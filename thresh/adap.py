#Adaptive Thresholding: In this, the algorithm calculate the threshold for a small regions of the image. So we get different thresholds
#  for different regions of the same image and it gives us better results for images with varying illumination
import cv2 as cv
i=cv.imread("plate.jpg")
img=cv.cvtColor(i,cv.COLOR_BGR2GRAY)
gaussian_blur=cv.GaussianBlur(img,(11,11),20)
adap=cv.adaptiveThreshold(gaussian_blur,255,cv.ADAPTIVE_THRESH_MEAN_C,cv.THRESH_BINARY_INV,25,30)
cv.imshow("Adaptive Thresholding",adap)
cv.imwrite ("thresholded_plate.jpg", adap)
cv.waitKey(0)
#APPLICATIONS:In the Simple Thresholding, we used a global value as threshold value. But it may not be good in all the conditions where
#image has different lighting conditions in different areas. In that case, we go for adaptive thresholding