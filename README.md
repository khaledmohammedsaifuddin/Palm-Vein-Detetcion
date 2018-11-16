# Palm-Vein-Detetcion
Palm Vein Detection Technique using OpenCV
To detect the vein of a human beings palm we have to first take a picture of palm. As we know hemoglobin in our blood absorbs infrared light so we can use some infrared LEDs below one's hand and then take picture of palm by using RasberryPi NOIR camera. 
# Procedures
## step 1(Import OpenCv):
-import cv2 #as we are working on OpenCv
## step 2 (Read Image):
Now we have to read an image of palm. Below instruction will read image from the current directory. </br> 
-img_palm = cv2.imread("palm.jpg")</br>
## step 3 (Convert into gray scale):
Then we have to convert it into gray scale by using this command </br>
gray = cv2.cvtColor(img_palm, cv2.COLOR_BGR2GRAY) </br>
## step 4 (Reduce Noise):
Reducing some noise by opencv function </br>
-noiseReduced = cv2.fastNlMeansDenoising(gray)</br>
## step 5 (Apply Histogram Equalization):
To make the vein more smooth we may apply histogram equalization. It will improve contrast of the image. </br>
-kernel = np.ones((7,7),np.uint8)</br>
-img_palm = cv2.morphologyEx(noiseReduced, cv2.MORPH_OPEN, kernel)</br>
-img_palm_yuv = cv2.cvtColor(img_palm, cv2.COLOR_BGR2YUV)</br>
-img_palm_yuv[:,:,0] = cv2.equalizeHist(img_palm_yuv[:,:,0])</br>
-img_palm_output = cv2.cvtColor(img_palm_yuv, cv2.COLOR_YUV2BGR)</br>
## step 6 (Erosion Technique):
Now, we may apply erosion technique it can strip away outer layers of data from a image. It will make the vein portion more sharp.</br>

-img_palm = gray.copy()</br>
-skel = img_palm.copy()</br>
-skel[:,:] = 0</br>
-kernel = cv2.getStructuringElement(cv2.MORPH_CROSS, (5,5))</br>
-while cv2.countNonZero(img_palm) > 0:</br>
    -eroded = cv2.morphologyEx(img_palm, cv2.MORPH_ERODE, kernel)</br>
    -temp = cv2.morphologyEx(eroded, cv2.MORPH_DILATE, kernel)</br>
    -temp  = cv2.subtract(img_palm, temp)</br>
    -skel = cv2.bitwise_or(skel, temp)</br>
    -img_palm[:,:] = eroded[:,:]</br>
## step 7 (Apply Threshold):
At last, we may apply a threshold as our wish to make the vein portion more visible  </br>
-ret, thr = cv2.threshold(skel, 5,255, cv2.THRESH_BINARY);</br>
-cv2.imwrite("thr.jpg", thr)


