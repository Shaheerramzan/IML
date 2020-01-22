import tensorflow as tf
from keras import Sequential
from keras.layers import Dense
import pandas as pd
from sklearn.metrics import confusion_matrix, accuracy_score
from sklearn import metrics
import matplotlib.pyplot as plt
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler


data = pd.read_csv('student-data.csv')

for col, col_data in data.iteritems():
    if col_data.dtype == object:
        unique_list = col_data.unique()
        for ind in range(0, len(unique_list)):
            data[col] = data[col].replace(unique_list[ind], ind)

dataHead = data.columns
for col in dataHead:
    data[col] = pd.to_numeric(data[col])

y = data['passed']
data = data.drop(columns='passed')
X_train, X_test, y_train, y_test = train_test_split(data, y, test_size=0.30, random_state=0, stratify=y)

scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

model = Sequential()
model.add(Dense(data.shape[1], activation='relu', input_dim=data.shape[1]))
model.add(Dense(118, activation='relu'))
model.add(Dense(131, activation='tanh'))
model.add(Dense(121, activation='relu'))
model.add(Dense(1, activation='sigmoid'))
model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

model.fit(X_train, y_train.to_numpy(), batch_size=10, epochs=10, verbose=1)
y_pred = model.predict_classes(X_test)
model.evaluate(X_test, y_test.to_numpy())
print(confusion_matrix(y_test, y_pred))
print(accuracy_score(y_test, y_pred))
