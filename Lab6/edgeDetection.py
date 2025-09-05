import cv2

img = cv2.imread("q.jpg")
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
blur = cv2.GaussianBlur(gray,(13,13),0)  # Increased blur from (5,5) to (9,9)

sobelx = cv2.Sobel(blur,cv2.CV_64F,1,0,ksize=3)
sobely = cv2.Sobel(blur,cv2.CV_64F,0,1,ksize=3)

abs_sobelx = cv2.convertScaleAbs(sobelx)
abs_sobely = cv2.convertScaleAbs(sobely)

edges = cv2.bitwise_or(abs_sobelx,abs_sobely)
edges = cv2.Canny(edges,150,250)  # Increased thresholds from 100,200 to 150,250

cv2.imshow("Original Image",img)
cv2.imshow("Edge Detected Image",edges)
cv2.imwrite("output.jpg",edges)
cv2.waitKey(0)
cv2.destroyAllWindows()


#import cv2

img = cv2.imread("q.jpg")
gray = cv2.cvtColor(gray,cv2.COLOR_BGR2GRAY)

blur = cv2.GaussianBlur(gray,(5,5),0)

sobel_x = cv2.Sobel(blur,cv2.CV_64F,1,0,ksize = 3)
sobel_y = cv2.Sobel(blur,cv2.CV_64F,0,1,ksize = 3)

sobel_x = cv2.convertScaleAbs(sobelx)
sobel_y = cv2.convertScaleAbs(sobely)

edges = cv2.bitwise_or(sobel_y,sobel_x)

edges = cv2.Canny(edges,500,250)

cv2.imshow("idk",edges)