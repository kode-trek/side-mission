import shutil
import datetime
import imghdr
import cv2 as cv
import numpy as np
import numpy
from os import walk
import os

filenames = next(walk("."), (None, None, []))[2]

v = []
for i in filenames:
	if imghdr.what(i) in ['png', 'jpg', 'jpeg', 'tiff', 'bmp', 'gif']:
		v.append(i)

src = []
for i in v:	src.append(cv.imread(i))

hsv = []
for i in src:	hsv.append(cv.cvtColor(i, cv.COLOR_BGR2HSV))

h_bins = 50
s_bins = 60
histSize = [h_bins, s_bins]

# hue varies from 0 to 179, saturation from 0 to 255
h_ranges = [0, 180]
s_ranges = [0, 256]
ranges = h_ranges + s_ranges # concat lists

# Use the 0-th and 1-st channels
channels = [0, 1]

hist = []
for i in hsv:
	hist.append(cv.calcHist(i, channels, None, histSize, ranges, accumulate=False))
for i in hist:
	cv.normalize(i, i, alpha=0, beta=1, norm_type=cv.NORM_MINMAX)

x = datetime.datetime.now()
dt = x.strftime("%d") + x.strftime("%m") + x.strftime("%y") + x.strftime("%H") + x.strftime("%M") + x.strftime("%S")

tmpd = "result_" + str(dt)
#os.mkdir(tmpd)

#f = open(tmpd + "/" + v[0] + ".txt", "a")
#f.write(v[1])
#f.close()

comp = []
c = 0
while (c < len(hist) - 1):
	for i in range(len(hist) - 1):
		a1 = (int(cv.compareHist(hist[c], hist[i+1], 0)*100) >= 95)
		a2 = (int(cv.compareHist(hist[c], hist[i+1], 3)*100) >= 95)
#		print(int(cv.compareHist(hist[c], hist[i+1], 0)*100))
#		print(int(cv.compareHist(hist[c], hist[i+1], 3)*100))
#		print ()
		if a1:
#		if (cv.compareHist(hist[c], hist[i+1], 0)*100 >= 85):
			comp.append((v[c], v[i+1]))
#			f = open(tmpd + "/" + v[c] + ".txt", "a")
#			f.write(v[i+1] + "\n")
#			f.close()

	c += 1

comp2 = []
for i in comp:
	if i[0] != i[1]:	comp2.append(i)

for i in comp2:	print (i[0], i[1])

for i in comp2:
	try:
		os.mkdir(i[0] + "_d")
	except:	pass
	shutil.copy2(i[1], i[0] + "_d")
