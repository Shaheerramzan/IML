import pandas as pd
from sklearn import metrics
from sklearn.naive_bayes import GaussianNB
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier as Dt


data = pd.read_csv('student-data.csv')

for col, col_data in data.iteritems():
    if col_data.dtype == object:
        unique_list = col_data.unique()
        for ind in range(0, len(unique_list)):
            data[col] = data[col].replace(unique_list[ind], ind)

dataHead = data.columns
for col in dataHead:
    data[col] = pd.Categorical(data[col])

y = data['passed']
data = data.drop(columns='passed')
X_train, X_test, y_train, y_test = train_test_split(data, y, test_size=0.85, random_state=1)

gnb = GaussianNB()
gnb.fit(X_train, y_train)
y_pred_naive = gnb.predict(X_test)
acc_naive_bayes = metrics.accuracy_score(y_test, y_pred_naive)*100
print("Gaussian Naive Bayes model accuracy(in %):", acc_naive_bayes)

dts = Dt()
dts.fit(X_train, y_train)
y_pred_d_tree = dts.predict(X_test)
acc_d_tree = metrics.accuracy_score(y_test, y_pred_d_tree)*100
print("Decision tree model accuracy(in %):", acc_d_tree)
if acc_d_tree < acc_naive_bayes:
    print('Naive Bayes has more accuracy than Decision Trees')
else:
    print('Decision Trees has more accuracy than Naive Bayes')
