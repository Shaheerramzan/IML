# load dogs vs cats dataset, reshape and save to a new file
from os import listdir
import gc
from sys import getsizeof
from numpy import asarray
from numpy import save
from keras.preprocessing.image import load_img
from keras.preprocessing.image import img_to_array


# define location of dataset
folder = '../Datasets/cats&dogs/train/'
file_list = listdir(folder)
number_files = len(file_list)
batch = int(number_files / 5)
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
    if i % batch == 0 and i != 0:
        # convert to a numpy arrays
        photos = asarray(photos)
        labels = asarray(labels)
        print(photos.shape, labels.shape, i / batch)
        # save the reshaped photos
        save('Dataset/dogs_vs_cats_photos' + str(int(i/batch)) + '.npy', photos)
        save('Dataset/dogs_vs_cats_labels' + str(int(i/batch)) + '.npy', labels)
        del photos
        del labels
        photos, labels = [list()] * batch, [int] * batch
photos = asarray(photos)
labels = asarray(labels)
print(photos.shape, labels.shape)
# save the reshaped photos
save('Dataset/dogs_vs_cats_photos' + str(int(batch)) + '.npy', photos)
save('Dataset/dogs_vs_cats_labels' + str(int(batch)) + '.npy', labels)
del photos
del labels
