import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split

from server.utils import data_provider


def preprocess(age, sex, cp, trestbps, restecg, chol, fbs, thalach, exang, oldpeak, slope, ca, thal):

    if sex == "male":
        sex = 1
    else:
        sex = 0
    if cp == "Typical angina":
        cp = 0
    elif cp == "Atypical angina":
        cp = 1
    elif cp == "Non-anginal pain":
        cp = 2
    elif cp == "Asymptomatic":
        cp = 3
    if exang == "Yes":
        exang = 1
    elif exang == "No":
        exang = 0
    if fbs == "Yes":
        fbs = 1
    elif fbs == "No":
        fbs = 0
    if slope == "Upsloping: better heart rate with excercise(uncommon)":
        slope = 0
    elif slope == "Flatsloping: minimal change(typical healthy heart)":
        slope = 1
    elif slope == "Downsloping: signs of unhealthy heart":
        slope = 2
    if thal == "fixed defect: used to be defect but ok now":
        thal = 6
    elif thal == "reversable defect: no proper blood movement when excercising":
        thal = 7
    elif thal == "normal":
        thal = 2.31
    if restecg == "Nothing to note":
        restecg = 0
    elif restecg == "ST-T Wave abnormality":
        restecg = 1
    elif restecg == "Possible or definite left ventricular hypertrophy":
        restecg = 2

    user_input = [age, sex, cp, trestbps, restecg, chol,
                  fbs, thalach, exang, oldpeak, slope, ca, thal]

    scaler = data_provider.GetStandardScalarForHeart()
    clf = data_provider.GetDecisionTreeClassifierForHeart()

    user_input = np.array(user_input).reshape(1, -1)
    user_input = scaler.fit_transform(user_input)
    print(user_input)
    prediction = clf.predict(user_input)
    print(int(prediction))

    return int(prediction)
