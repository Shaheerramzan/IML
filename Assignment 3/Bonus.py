import pandas as pd
from sklearn import metrics
from sklearn.naive_bayes import GaussianNB
from sklearn.model_selection import train_test_split
from itertools import combinations
import copy as cpy
import threading as th
import cython


def main_work(current_data, acc, c):
    for col, col_data in current_data.items():
        if col_data.dtype == object:
            unique_list = col_data.unique()
            for ind in range(0, len(unique_list)):
                current_data[col] = current_data[col].replace(unique_list[ind], ind)

    x_train, x_test, y_train, y_test = train_test_split(current_data, y, test_size=0.85, random_state=1)

    gnb = GaussianNB()
    gnb.fit(x_train, y_train)
    y_pred_naive = gnb.predict(x_test)
    acc_naive_bayes = metrics.accuracy_score(y_test, y_pred_naive) * 100
    if acc[1] < acc_naive_bayes:
        acc[1] = cpy.deepcopy(acc_naive_bayes)
        temp = acc[0]
        del temp
        acc[0] = list()
        acc[0] = cpy.deepcopy(c)


data = pd.read_csv('student-data.csv')
y = data['passed']
data = data.drop(columns='passed')
dataHead = data.columns
the_accurate = [list(), 0.0]

new_data = pd.DataFrame()

for n in range(1, 30):
    comb = combinations(dataHead, n)
    for cmb in comb:
        for item in cmb:
            new_data[item] = data[item]
        main_work(new_data, the_accurate, cmb)
        del new_data
        new_data = pd.DataFrame()
        del cmb
    print(f'combination with choose {n} the minimum till now is: {the_accurate[0]} and accuracy is: {the_accurate[1]}')
    del comb

