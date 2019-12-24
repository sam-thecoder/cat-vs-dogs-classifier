import cv2
import numpy as np

images = ['data/train/dog.5642.jpg']

img = images[0]

img = cv2.imread(img)

edges = cv2.Canny(img, 250, 250)

cv2.imshow('edges', edges)

cv2.waitKey(0)
cv2.destroyAllWindows()
