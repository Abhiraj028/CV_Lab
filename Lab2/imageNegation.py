import cv2

img = cv2.imread('../Lab3/image.jpg')
cv2.imshow("Normal Image",img)
cv2.waitKey(0)

gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
cv2.imshow("Grayscale",gray)
cv2.waitKey(0)

neg = cv2.bitwise_not(gray)
cv2.imshow("Negative Image",neg)
key = cv2.waitKey(0)
if key is ord("s"):
    cv2.imwrite("Negative_Image",neg)
cv2.destroyAllWindows()