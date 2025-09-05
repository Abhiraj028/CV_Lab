# Program to rotate the image
import cv2

# Read the input image
img = cv2.imread('change.jpeg')

# Define the rotation angle
angle = 45

# Get the image dimensions
h, w = img.shape[:2]

# Calculate the rotation matrix M
M = cv2.getRotationMatrix2D((w/2, h/2), angle, 1)

# Apply the rotation to the image
rotated_img = cv2.warpAffine(img, M, (w, h))

# Display the original and rotated images
cv2.imshow('Original Image', img)
cv2.imshow('Rotated Image', rotated_img)

# Wait for a key event
cv2.waitKey(0)

# Release the memory and destroy all windows
cv2.destroyAllWindows()


# Program to scale an image
import numpy as np
import cv2 as cv

img = cv.imread('change.jpeg', 0)
rows, cols = img.shape

# Shrink the image
img_shrinked = cv.resize(img, (250, 200), interpolation=cv.INTER_AREA)
cv.imshow('img', img_shrinked)

# Enlarge the image
img_enlarged = cv.resize(img_shrinked, None, fx=1.5, fy=1.5, interpolation=cv.INTER_CUBIC)
cv.imshow('img', img_enlarged)

cv.waitKey(0)
cv.destroyAllWindows()


# Program to translate an image
import numpy as np
import cv2 as cv

img = cv.imread('change.jpeg', 0)
rows, cols = img.shape

# Define translation matrix
M = np.float32([[1, 0, 100], [0, 1, 50]])

# Apply translation
dst = cv.warpAffine(img, M, (cols, rows))
cv.imshow('img', dst)

cv.waitKey(0)
cv.destroyAllWindows()


# Program to shear an image
import numpy as np
import cv2 as cv

img = cv.imread('change.jpeg', 0)
rows, cols = img.shape

# Define shear matrix
M = np.float32([[1, 0.5, 0], [0, 1, 0], [0, 0, 1]])

# Apply shear
sheared_img = cv.warpPerspective(img, M, (int(cols*1.5), int(rows*1.5)))
cv.imshow('img', sheared_img)
cv.waitKey(0)
cv.destroyAllWindows()
