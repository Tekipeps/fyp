from calendar import c
import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from server.utils import data_provider


def preprocess(age, sex, cp, trestbps, restecg, chol, fbs, thalach, exang, oldpeak, slope, ca, thal):
    user_input = [age, sex, cp, trestbps, chol, fbs, restecg,
                  thalach, exang, oldpeak, slope, ca, thal]
    user_input = list(map(lambda x: float(x), user_input))
    print(user_input)

    scaler = data_provider.GetStandardScalarForHeart()

    decision_tree_clf = data_provider.GetDecisionTreeClassifierForHeart()
    knn_clf = data_provider.GetKNNClassifierForHeart()
    naive_bayes_clf = data_provider.GetNaiveBayesClassifierForHeart()
    logistic_regression_clf = data_provider.GetLogisticRegressionClassifierForHeart()

    user_input = np.array(user_input).reshape(1, -1)
    user_input = scaler.fit_transform(user_input)
    print(user_input)

    decision_tree_output = decision_tree_clf.predict(user_input)
    knn_output = knn_clf.predict(user_input)
    naive_bayes_output = naive_bayes_clf.predict(user_input)
    logistic_regression_output = logistic_regression_clf.predict(user_input)

    results = [
        {"algorithm": "K-Nearest Neighbors",  "output": knn_output},
        {"algorithm": "Decision Tree",  "output": decision_tree_output},
        {"algorithm": "Naive Bayes",  "output": naive_bayes_output},
        {"algorithm": "Logistic Regression",  "output": logistic_regression_output},
    ]
    return results
