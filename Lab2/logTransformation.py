import cv2
import numpy as np

img = cv2.imread("log.jpg")
gamma = 1.5
C = 255

gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
log_img = C * np.log1p(gray_img.astype(np.float32))

log_img = np.uint8(log_img)
result = cv2.hconcat([gray_img, log_img])

cv2.imshow("Log Transformation", img)
cv2.imshow("Log Transformation", log_img)
cv2.imwrite("output.jpg", result)
cv2.waitKey(0)
cv2.destroyAllWindows()


#import cv2 import numpy as np

img = cv2.imread("img.jpg")
C = 1.5
gray_img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
log_img = np.log1p(gray_img.astype(np.float32))