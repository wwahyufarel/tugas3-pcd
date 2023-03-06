import cv2
import numpy as np

# image path
path = r'foto alam.jpg'

# using imread()
img = cv2.imread(path)

im1 = cv2.blur(img, (5, 5))
im2 = cv2.boxFilter(img, -1, (2, 2), normalize=True)

cv2.imshow('image', np.hstack((im1, im2)))
cv2.waitKey(0);
cv2.destroyAllWindows();
cv2.waitKey(1)