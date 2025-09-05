import cv2
import numpy as np

img = cv2.imread("image.jpg")
gamma = 0.01 #0.2 for overexposed #3.5 for underexposed


corrected = np.power(img/255 , 1/gamma) * 255
corrected = corrected.astype(np.uint8)

cv2.imshow(f"Gamma {gamma}", corrected)
cv2.waitKey(0)
cv2.destroyAllWindows()



# import cv2
img = cv2.imread("image.jpg")
gamma = 50

changedImage = np.power(img/255,1/gamma) * 255
changedImage = changedImage.astype(np.uint8)

cv2.imshow("changedImage",changedImage)
cv2.waitKey(0)
cv2.destroyAllWindows()