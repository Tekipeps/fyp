import os
import pickle
import joblib

config = {
    'heart': {
        'LogisticRegression': 'models/logisticregression.pkl',
        'NaiveBayes': 'models/naivebayes.pkl',
        'KNN': 'models/knn.pkl',
        'DecisionTree': 'models/decision_tree_model.pkl',
        'scalar_file': 'models/standard_scaler.pkl',
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


def GetStandardScalarForHeart():
    return GetJobLibFile(config['heart']['scalar_file'])


def GetAllClassifiersForHeart():
    return (GetLogisticRegressionClassifierForHeart(), GetNaiveBayesClassifierForHeart(), GetDecisionTreeClassifierForHeart(), GetKNNClassifierForHeart())


def GetLogisticRegressionClassifierForHeart():
    return GetJobLibFile(config['heart']['LogisticRegression'])


def GetNaiveBayesClassifierForHeart():
    return GetJobLibFile(config['heart']['NaiveBayes'])


def GetDecisionTreeClassifierForHeart():
    return GetJobLibFile(config['heart']['DecisionTree'])


def GetKNNClassifierForHeart():
    return GetJobLibFile(config['heart']['KNN'])
