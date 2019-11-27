# -*- coding: utf-8 -*-
"""
Created on Tue Nov  5 00:31:00 2019

@author: Shaheer
"""

import numpy as np
import skimage.io as skio
import matplotlib.pyplot as plt
# read an image file in variable from current directory
img = skio.imread('Italy30.png')
# display an image on screen
skio.imshow(img)
# save an array as an image file in current directory
skio.imsave(arr, 'filename.png')
# get the dimensions of the 3-d array
rows, cols, chans = np.shape(img)
# create a new array of unsigned 8 bit integers of size 10 x 15 x 5
arr = np.array(shape = (10, 15, 5), dtype = np.uint8)
# create a new array filled with zeros of unsigned 8 bit integers of size 10 x 15 x 5
arr = np.zeros(shape = (10, 15, 5), dtype = np.uint8)
# create a new array filled with 100 of unsigned 8 bit integers of size 10 x 15 x 5
arr = 100 * np.ones(shape = (10, 15, 5), dtype = np.uint8)
# create a new array of booleans filled with false of size 10 x 15 x 5
arr = 100 * np.zeros(shape = (10, 15, 5), dtype = bool)