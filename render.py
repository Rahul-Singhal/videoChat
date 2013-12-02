from cv import *
# from highgui import *
import sys
import os.path
import time

i = 0
while (os.path.exists("pic"+`i`+".jpg")):
	filename = "pic"+`i`+".jpg"
	im = LoadImage(filename, CV_LOAD_IMAGE_COLOR)
	ShowImage("sample1", im);
	WaitKey(62)
	i = i+1
