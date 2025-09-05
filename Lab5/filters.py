import cv2
import numpy as np
img = cv2.imread("img.jpg",cv2.IMREAD_GRAYSCALE)

kernel = np.ones((5,5),np.float32) /25

mean_filtered = cv2.filter2D(img,-1,kernel)
median_filtered = cv2.medianBlur(img,5)
sharpened_image2 = cv2.Laplacian(img,cv2.CV_64F)

cv2.imshow("Original Image",img)
cv2.imshow("Mean Filtered Image",mean_filtered)
cv2.imshow("Median Filtered Image",median_filtered)
cv2.imshow("Sharpened Image",sharpened_image2)

cv2.waitKey(0)
cv2.destroyAllWindows()