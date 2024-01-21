# Usage:
# python3 script.py original.png modified.png
# Based on: https://github.com/mostafaGwely/Structural-Similarity-Index-SSIM-

import sys
import imutils
import cv2 as cv
from skimage.metrics import structural_similarity as ssim
#(score, diff) = ssim(img1, img2, Full=True)

img1 = cv.imread(sys.argv[1])
img2 = cv.imread(sys.argv[2])

img1 = cv.resize(img1, (64, 64))
img2 = cv.resize(img2, (64, 64))

img1_grayed = cv.cvtColor(img1, cv.COLOR_BGR2GRAY)
img2_grayed = cv.cvtColor(img2, cv.COLOR_BGR2GRAY)

#(score, diff) = compare_ssim(grayA, grayB, full=True)
(score, diff) = ssim(img1_grayed, img2_grayed, full=True)
diff = (diff * 255).astype("uint8")

print("SSIM: " + str(score))
