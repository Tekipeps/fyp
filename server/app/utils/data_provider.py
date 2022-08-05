import os
import pickle
import joblib

config = {
    'heart': {
        'LogisticRegression': 'models/logistic_regression.pkl',
        'NaiveBayes': 'models/naivebayes.pkl',
        'KNN': 'models/knn.pkl',
        'DecisionTree': 'models/decision_tree.pkl',
        'scalar_non_tree': 'models/minmax_scaler_non_tree.pkl',
        'label_encoder_tree': 'models/label_encoder.pkl',
        'one_hot_encoder_nontree': 'models/ohe_transformer.pkl'
    }}

dir = os.path.dirname(__file__)


def GetJobLibFile(filepath):
    if os.path.isfile(os.path.join(dir, filepath)):
        return joblib.load(os.path.join(dir, filepath))
    return None


def GetPickleFile(filepath):
    if os.path.isfile(os.path.join(dir, filepath)):
        return pickle.load(open(os.path.join(dir, filepath), "rb"))
    return None


def GetMinMaxScalerNonTree():
    return GetJobLibFile(config['heart']['scalar_non_tree'])

def GetLabelEncoderTree():
    return GetJobLibFile(config['heart']['label_encoder_tree'])

def GetOneHotEncoderNonTree():
    return GetJobLibFile(config['heart']['one_hot_encoder_nontree'])
    
def GetAllClassifiers():
    return (GetLogisticRegressionClassifier(), GetNaiveBayesClassifier(), GetDecisionTreeClassifier(), GetKNNClassifier())


def GetLogisticRegressionClassifier():
    return GetJobLibFile(config['heart']['LogisticRegression'])


def GetNaiveBayesClassifier():
    return GetJobLibFile(config['heart']['NaiveBayes'])


def GetDecisionTreeClassifier():
    return GetJobLibFile(config['heart']['DecisionTree'])


def GetKNNClassifier():
    return GetJobLibFile(config['heart']['KNN'])
