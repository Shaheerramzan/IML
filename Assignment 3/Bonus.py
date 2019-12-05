import pandas as pd
from sklearn import metrics
from sklearn.naive_bayes import GaussianNB
from sklearn.model_selection import train_test_split
from itertools import combinations


def work(current_data):
    for col, col_data in current_data.items():
        if col_data.dtype == object:
            unique_list = col_data.unique()
            for ind in range(0, len(unique_list)):
                current_data[col] = current_data[col].replace(unique_list[ind], ind)

    # for col in dataHead:
    #    data[col] = pd.Categorical(data[col])

    x_train, x_test, y_train, y_test = train_test_split(current_data, y, test_size=0.85, random_state=1)

    gnb = GaussianNB()
    gnb.fit(x_train, y_train)
    y_pred_naive = gnb.predict(x_test)
    acc_naive_bayes = metrics.accuracy_score(y_test, y_pred_naive) * 100
    print("Gaussian Naive Bayes model accuracy(in %):", acc_naive_bayes)


data = pd.read_csv('student-data.csv')
y = data['passed']
data = data.drop(columns='passed')
dataHead = data.columns
new_data = pd.DataFrame()

for n in range(1, 30):
    print(n)
    comb = combinations(dataHead, n)
    for cmb in comb:
        for item in cmb:
            new_data[item] = data[item]
        work(new_data)
        del new_data
        new_data = pd.DataFrame()
    del comb

