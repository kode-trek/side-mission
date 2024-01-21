from sys import argv
from os import walk
from os import mkdir
from os import system

# returns reversed list. (ex. [b,a] for [a,b])
def rev(arg1):
 v1 = arg1
 v2 = []
 for i in reversed(v1): v2.append(i)
 return v2

# v1: directory-name
v1 = argv[1]
# v2: file-name(s) in [v1]
v2 = next(walk(v1), (None, None, []))[2]
# v3: paire(s)
v3 = []
for i in v2:
 for j in v2:
  v3.append([i,j])
v3 = [i for i in v3 if i[0] != i[1]]
# v4: eliminates duplicated-pairs (ex. [a,b] & [b,a]) in [v3]
v4 = []
for i in v3:
 if rev(i) not in v4: v4.append(i)

import cv2 as cv
from skimage.metrics import structural_similarity as ssim

k=[]
for i in v4:
 p1 = v1 + "/" + i[0]
 p2 = v1 + "/" + i[1]

 img1 = cv.imread(p1)
 img2 = cv.imread(p2)

 img1 = cv.resize(img1, (64, 64))
 img2 = cv.resize(img2, (64, 64))

 img1_grayed = cv.cvtColor(img1, cv.COLOR_BGR2GRAY)
 img2_grayed = cv.cvtColor(img2, cv.COLOR_BGR2GRAY)

 (score, diff) = ssim(img1_grayed, img2_grayed, full=True)
 diff = (diff * 255).astype("uint8")

 print(i, "SSIM: " + str(score))
 
 score = abs(int(score*100))
 try:
  try: mkdir(str(score))
  except: pass
  l1 = str(score) + "/" + i[0]
  l2 = str(score) + "/" + i[1]
  system("ln -s ../\"" + p1 + "\" \"" + l1 + "\"")
  system("ln -s ../\"" + p2 + "\" \"" + l2 + "\"")
 except: pass
