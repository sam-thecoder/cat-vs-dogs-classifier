import cv2
import numpy as np

images = ['data/test/1818.jpg']

img = images[0]

img = cv2.imread(img)

edges = cv2.Canny(img, 250, 250)
image_data = cv2.resize(edges, (64, 64))

cv2.imshow('edges', edges)
cv2.imshow('img', img)
cv2.imshow('small icon', image_data)
#cv2.imwrite('img.png', image_data)

cv2.waitKey(0)
cv2.destroyAllWindows()
