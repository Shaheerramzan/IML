from keras.datasets import mnist
from keras.models import Sequential
from keras.layers import Dense
from keras.optimizers import RMSprop
from keras import utils
import matplotlib.pyplot as plt

(x_train, y_train), (x_test, y_test) = mnist.load_data()

rec = x_train[1]
plt.imshow(rec, cmap='gray')
