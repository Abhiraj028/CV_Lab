import cv2
import matplotlib.pyplot as plt

img = cv2.imread("img.jpg")
img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

plt.figure(figsize=(20, 20))

plt.subplot(221)
plt.title('Original')
plt.imshow(img_rgb)

img_hist = cv2.calcHist([img_gray], [0], None, [256], [0, 256])
plt.subplot(222)
plt.title('Histogram 1')
plt.plot(img_hist)

plt.subplot(223)
equalized_img = cv2.equalizeHist(img_gray)
plt.title('Equalized Image')
plt.imshow(equalized_img, cmap='gray')

eq_image = cv2.calcHist([equalized_img],[0],None,[256],[0,256])

plt.subplot(224)
plt.plot(eq_image)
plt.title("Equalised Historgram")

plt.savefig("Hist.jpg")

#import cv2 import matplotlib import matplotlib.pyplot as plt

img = cv2.imread("img.jpg")
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
rgb = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
plt.figure(figsize=(20,20))

plt.subplot(221)
plt.imshow(rgb)
plt.title("ORiginal Image")
gray_hist = cv2.calcHist([gray],[0],None,[256],[0,256])

plt.subplot(222)
plt.plot(gray_hist)
plt.title("Hist")

plt.subplot(223)
plt.hist(gray.ravel(),[256],[0,256])
plt.title("Ravel Hist")

plt.subplot(224)
eq = cv2.equalizeHist(gray_hist)