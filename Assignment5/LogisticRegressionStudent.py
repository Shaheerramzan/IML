import pandas as pd
from sklearn import metrics
import matplotlib.pyplot as plt
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression


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
X_train, X_test, y_train, y_test = train_test_split(data, y, test_size=0.25, random_state=1)

logistic_regression = LogisticRegression()
logistic_regression.fit(X_train, y_train)
y_predict = logistic_regression.predict(X_test[0:])
acc_logistic_regression = logistic_regression.score(X_test, y_test)
print("Logistic Regression accuracy:", acc_logistic_regression)
cm = metrics.confusion_matrix(y_test, y_predict)
print(cm)
