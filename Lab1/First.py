import cv2

image = cv2.imread("img.jpeg")
cv2.imshow("Original Image:",image)
cv2.waitKey(0)

gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
output = cv2.cvtColor(gray,cv2.COLOR_GRAY2BGR)

cv2.line(output,(400,200),(500,350),(255,255,0),3)
cv2.line(output,(300,350),(400,200),(255,255,0),3)
cv2.line(output,(300,350),(500,350),(255,255,0),3)
cv2.line(output,(400,200),(700,200),(255,255,0),3)
cv2.line(output,(700,200),(700,500),(255,255,0),3)

cv2.rectangle(output,(300,350),(700,500),(255,255,0),4)
cv2.rectangle(output,(350,400),(400,500),(255,255,0),4)
cv2.circle(output,(400,300),20,(255,255,0),3)
cv2.putText(output,"HALLO ME RAJNIKENT",(400,600),cv2.FONT_ITALIC,1,(255,255,0),2)
cv2.imshow("Image",output)
cv2.waitKey(0)
cv2.destroyAllWindows()