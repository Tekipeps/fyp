from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.preprocessing import MinMaxScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.naive_bayes import GaussianNB
import joblib
import pandas as pd
import numpy as np


print("Training all models...")

# read csv using pandas library
df = pd.read_csv("heart.csv")

# select numerical features and encoding it
from sklearn.preprocessing import LabelEncoder

string_col = df.select_dtypes(include="object").columns

## Creating one hot encoded features for working with non tree based algorithms
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import make_column_transformer

target_col="HeartDisease"


df_nontree = df.drop(target_col,axis=1)

ohe = OneHotEncoder(handle_unknown='ignore')

transformer = make_column_transformer(
    (OneHotEncoder(), string_col),
    remainder='passthrough',
    verbose_feature_names_out=False
)

transformed = transformer.fit_transform(df_nontree)
df_nontree = pd.DataFrame(
    transformed, 
    columns=transformer.get_feature_names_out()
)

joblib.dump(transformer, "models/ohe_transformer.pkl")

# Getting the target column at the end
df_nontree=pd.concat([df_nontree,df[target_col]],axis=1)

feature_col_nontree=df_nontree.columns.to_list()
feature_col_nontree.remove("HeartDisease")

# Feature Scaling
scal = MinMaxScaler()
X_train = scal.fit_transform(df_nontree[feature_col_nontree].values)
Y_train = df_nontree[target_col]

joblib.dump(scal, "models/minmax_scaler_non_tree.pkl")

# LOGISTIC REGRESSION
clf=LogisticRegression()
clf.fit(X_train,Y_train)

joblib.dump(clf, "models/logistic_regression.pkl")


# NAIVE BAYES
gnb = GaussianNB()
gnb.fit(X_train, Y_train)

joblib.dump(clf, 'models/naivebayes.pkl')

# KNN
clf = KNeighborsClassifier(n_neighbors=15)
clf.fit(X_train, Y_train)

joblib.dump(clf, 'models/knn.pkl')


# Label Ecoding 
# which will be used with Tree Based Algorithms

df_tree = df.drop(np.insert(string_col, -1, target_col),axis=1)


le = LabelEncoder()
df_cat = df[string_col].apply(le.fit_transform)

# Add back categorical features
df_tree = pd.concat([df_tree, df_cat],axis=1)
joblib.dump(le, "models/label_encoder.pkl")

# Add back the target column
df_tree=pd.concat([df_tree,df[target_col]],axis=1)

feature_col_tree=df_tree.columns.to_list()
feature_col_tree.remove(target_col)

X_train = df_tree[feature_col_tree]
Y_train = df_tree[target_col]

clf=DecisionTreeClassifier(criterion="entropy")
clf.fit(X_train,Y_train)

# Saving the decision tree model
filename = 'models/decision_tree.pkl'
joblib.dump(clf, filename)

print("Done!")