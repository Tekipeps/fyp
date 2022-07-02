from sklearn.metrics import classification_report, confusion_matrix
from sklearn.metrics import classification_report
from sklearn.metrics import accuracy_score
from sklearn import tree
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
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
    X, Y, random_state=2, test_size=0.1)

# Fitting Decision Tree Classification to the Training set

clf = tree.DecisionTreeClassifier(criterion="entropy", max_depth=3)
clf.fit(X_train, Y_train)

# Saving the model
filename = 'models/decision_tree_model.pkl'
joblib.dump(clf, filename)

# Predicting the Test set results
y_pred = clf.predict(X_test)

# checking the accuracy for predicted results
accuracy_score(Y_test, y_pred)

# Confusion metrics
cm = confusion_matrix(Y_test, y_pred)

# Interpretation:
print(classification_report(Y_test, y_pred))
