#Write a program that applies gamma correction to an image. Allow the user to test different gamma values such as 0.4, 1.0 and 2.5. Observe the brightness change.

import cv2
import numpy as np

img = cv2.imread("gammaSet_question.jpg")
gamma = 0


corrected = np.power(img/255 , 1/gamma) * 255
corrected = corrected.astype(np.uint8)

cv2.imshow(f"Gamma {gamma}", corrected)
cv2.waitKey(0)
cv2.destroyAllWindows()

#import cv2

img = cv2.imread("image.jpg")
gamma = 0

correctedImg = np.power(img/255,1/gamma) * 255
correctedImg = correctedImg.astype(np.uint8)

cv2.imshow(correctedImg)
cv2.waitKey(0)
cv2.destroyAllWindows()