#Simple Thresholding:If pixel value is greater than a threshold value, it is assigned one value (white), 
# else it is assigned another value ( black).
import cv2
import imutils


i = cv2.imread('coins.jpg')
img=cv2.cvtColor(i,cv2.COLOR_BGR2GRAY)
gaussian_blur=cv2.GaussianBlur(img,(11,11),20)
ret, thresh1 = cv2.threshold(gaussian_blur,245,255,cv2.THRESH_BINARY)
#ret, thresh2 = cv2.threshold(img,127,255,cv2.THRESH_BINARY_INV)


cv2.imshow("Thresholded image",thresh1)
cv2.imwrite("thresh_coins.jpg", thresh1)
cv2.waitKey()
#APPLICATIONS: we change the pixels of an image to make the image easier to analyze

cnts = cv2.findContours(thresh1.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
cnts = imutils.grab_contours(cnts)
output = i.copy()
# loop over the contours
#for c in cnts:
	# draw each contour on the output image with a 3px thick purple
	# outline, then display the output contours one at a time
cv2.drawContours(output, cnts, -1, (0, 0, 255), 5)
cv2.imshow("Contours", output)
cv2.waitKey(0)