import numpy as np
import pandas as pd
from server.utils import data_provider



def pred_logistic_regression(inp, cols):
    ohe = data_provider.GetOneHotEncoderNonTree()
    scal = data_provider.GetMinMaxScalerNonTree()

    inp= pd.DataFrame(np.array(inp).reshape(1, -1), columns=cols)
    inp = ohe.transform(inp)
    inp = scal.transform(inp)
    clf = data_provider.GetLogisticRegressionClassifier()
    return clf.predict(inp)

def pred_naive_bayes(inp, cols):
    ohe = data_provider.GetOneHotEncoderNonTree()
    scal = data_provider.GetMinMaxScalerNonTree()

    inp= pd.DataFrame(np.array(inp).reshape(1, -1), columns=cols)
    inp = ohe.transform(inp)
    inp = scal.transform(inp)
    clf = data_provider.GetNaiveBayesClassifier()
    return clf.predict(inp)


def pred_knn(inp, cols):
    ohe = data_provider.GetOneHotEncoderNonTree()
    scal = data_provider.GetMinMaxScalerNonTree()

    inp= pd.DataFrame(np.array(inp).reshape(1, -1), columns=cols)
    inp = ohe.transform(inp)
    inp = scal.transform(inp)
    clf = data_provider.GetKNNClassifier()
    return clf.predict(inp)

def pred_decision_tree(inp, cols, string_cols):

    # le = data_provider.GetLabelEncoderTree()
    # inp = pd.DataFrame(np.array(inp).reshape(1, -1), columns=cols)

    # print(inp.dtypes)
    # transformed_cols = inp[string_cols].astype(str).apply(le.transform)

    # inp= pd.concat([inp.drop(string_cols, axis=1), transformed_cols], axis=1)
    # clf = data_provider.GetDecisionTreeClassifier()
    # return clf.predict(inp)
    return 0 # something wrong

# order Age,Sex,ChestPainType,RestingBP,Cholesterol,FastingBS,RestingECG,MaxHR,ExerciseAngina,Oldpeak,ST_Slope
# sample 37,M,ASY,140,207,0,Normal,130,Y,1.5,Flat
def process(user_input):
    print(user_input)
    string_cols = ['Sex', 'ChestPainType', 'RestingECG', 'ExerciseAngina', 'ST_Slope']
    colums = ['Age','Sex','ChestPainType','RestingBP','Cholesterol','FastingBS','RestingECG','MaxHR','ExerciseAngina','Oldpeak','ST_Slope']

    logistic_regression_output = pred_logistic_regression(user_input, colums)
    naive_bayes_output = pred_naive_bayes(user_input, colums)
    knn_output = pred_knn(user_input, colums)
    decision_tree_output = pred_decision_tree(user_input, colums, string_cols) # hax
    # print(logistic_regression_output, naive_bayes_output, knn_output, decision_tree_output)

    results = [
        {"algorithm": "K-Nearest Neighbors",  "output": knn_output},
        {"algorithm": "Decision Tree",  "output": knn_output},
        {"algorithm": "Naive Bayes",  "output": naive_bayes_output},
        {"algorithm": "Logistic Regression",  "output": logistic_regression_output},
    ]
    return results
