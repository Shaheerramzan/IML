# load dogs vs cats dataset, reshape and save to a new file
import numpy as np  # linear algebra
import pandas as pd  # data processing, CSV file I/O (e.g. pd.read_csv)
import cv2
import matplotlib.pyplot as plt
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Flatten, Dropout, Activation, Conv2D, MaxPooling2D

# define location of dataset
folder = '../Datasets/cats&dogs/train/'
file_list = listdir(folder)
number_files = len(file_list)
partition = 5
batch = int(number_files / partition)
photos, labels = [list()] * batch, [int] * batch
# enumerate files in the directory
for i in range(number_files):
    # determine class
    output = 0.0
    if file_list[i].startswith('cat'):
        output = 1.0
    # load image
    photo = load_img(folder + file_list[i], target_size=(200, 200))
    temp_photo = photo
    # convert to numpy array
    photo = img_to_array(photo)
    # store
    photos[i % batch] = photo
    labels[i % batch] = output
    del temp_photo
    del photo
    del output
    if i % batch == 0 and i != 0 or i == number_files - 1:
        # convert to a numpy arrays
        photos = asarray(photos)
        labels = asarray(labels)
        print(photos.shape, labels.shape, i / batch)
        # save the reshaped photos
        if i == number_files - 1:
            st = str(partition)
        else:
            st = str(int(i / batch))
        save('Dataset/dogs_vs_cats_photos' + st + '.npy', photos)
        save('Dataset/dogs_vs_cats_labels' + st + '.npy', labels)
        del photos
        del labels
        photos, labels = [list()] * batch, [int] * batch
