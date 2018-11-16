import numpy as np
import cv2

# Load the 600x600 image and convert to grayscale
img_palm = cv2.imread("palm.jpg")
 
#converting into gray scale
gray = cv2.cvtColor(img_palm, cv2.COLOR_BGR2GRAY) 

#reducing some noise by opencv function 
noiseReduced = cv2.fastNlMeansDenoising(gray)

# equalize hist
kernel = np.ones((7,7),np.uint8)
img_palm = cv2.morphologyEx(noiseReduced, cv2.MORPH_OPEN, kernel)
img_palm_yuv = cv2.cvtColor(img_palm, cv2.COLOR_BGR2YUV)
img_palm_yuv[:,:,0] = cv2.equalizeHist(img_palm_yuv[:,:,0])
img_palm_output = cv2.cvtColor(img_palm_yuv, cv2.COLOR_YUV2BGR)

#skeletonize using repeated erosion
img_palm = gray.copy()
skel = img_palm.copy()
skel[:,:] = 0
kernel = cv2.getStructuringElement(cv2.MORPH_CROSS, (5,5))
while cv2.countNonZero(img_palm) > 0:
    eroded = cv2.morphologyEx(img_palm, cv2.MORPH_ERODE, kernel)
    temp = cv2.morphologyEx(eroded, cv2.MORPH_DILATE, kernel)
    temp  = cv2.subtract(img_palm, temp)
    skel = cv2.bitwise_or(skel, temp)
    img_palm[:,:] = eroded[:,:]
# applying a threshold so make veins more visible 
ret, thr = cv2.threshold(skel, 5,255, cv2.THRESH_BINARY);
cv2.imwrite("thr.jpg", thr)