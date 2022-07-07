from sklearn.linear_model import LogisticRegression
from sklearn import tree
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.naive_bayes import GaussianNB
import joblib
# import numpy as np
# import matplotlib.pyplot as plt
import pandas as pd


# read csv using pandas library
df = pd.read_csv("heart_dataset.csv")
cols = ["age", "cp", "trestbps", "fbs", "restecg", "thalach"]


# Feature Scaling
scal = StandardScaler()
feat = ['age', 'sex', 'cp', 'trestbps', 'chol', 'fbs', 'restecg',
        'thalach', 'exang', 'oldpeak', 'slope', 'ca', 'thal']
df[feat] = scal.fit_transform(df[feat])

joblib.dump(scal, "models/standard_scaler.pkl")

# Dataset splitting

X = df.drop("condition", axis=1).values
Y = df.condition.values
X_train, X_test, Y_train, Y_test = train_test_split(
    X, Y, test_size=0.05, stratify=Y)

# Fitting Decision Tree Classification to the Training set

clf = tree.DecisionTreeClassifier(criterion="entropy", max_depth=3)
clf.fit(X_train, Y_train)

# Saving the decision tree model
filename = 'models/decision_tree_model.pkl'
joblib.dump(clf, filename)

# Using 15 neighbours as it got the highest score
clf = KNeighborsClassifier(n_neighbors=15)
clf.fit(X_train, Y_train)

# Saving the knn model
filename = 'models/knn.pkl'
joblib.dump(clf, filename)

# Naive bayes model
gnb = GaussianNB()
gnb.fit(X_train, Y_train)

# Saving the naive bayes model
filename = 'models/naivebayes.pkl'
joblib.dump(clf, filename)

# Logistic Regression model

clf = LogisticRegression()
clf.fit(X_train, Y_train)

# Saving the logistic regression model
filename = 'models/logisticregression.pkl'
joblib.dump(clf, filename)
