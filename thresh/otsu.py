#Otsu Binarization-, it automatically calculates a threshold value from image histogram for a bimodal image
#algorithm finds the optimal threshold value and returns you as the second output, retVal
import cv2 as cv
i=cv.imread("coins.jpg")
img=cv.cvtColor(i,cv.COLOR_BGR2GRAY)
ret,th1=cv.threshold(img,0,255,cv.THRESH_BINARY+cv.THRESH_OTSU)
cv.imshow("OTSU",th1)
print("[INFO] otsu's thresholding value: {}".format(ret))
cv.imwrite("thresh_otsu.jpg", th1)
cv.waitKey(0)
#APPLICATION:The algorithm calculates the optimum threshold value,and it improves noise filtering.