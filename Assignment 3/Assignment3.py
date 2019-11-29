import pandas as pd
from sklearn import metrics
from sklearn.naive_bayes import GaussianNB
from sklearn.model_selection import train_test_split

data = pd.read_csv('student-data.csv')
for name, colData in data.iteritems():
    data[name] = pd.Categorical(data[name])

y = data['passed']
data = data.drop(columns='passed')
X_train, X_test, y_train, y_test = train_test_split(data, y, test_size=0.4, random_state=1)

gnb = GaussianNB()
gnb.fit(X_train, y_train)

# making predictions on the testing set
y_pred = gnb.predict(X_test)

# comparing actual response values (y_test) with predicted response values (y_pred)

print("Gaussian Naive Bayes model accuracy(in %):", metrics.accuracy_score(y_test, y_pred)*100)

