from os import path, walk
from unicodedata import category
from unittest import result
from flask import Flask
from flask import render_template, redirect, url_for, request, flash, session
from flask import Flask
from flask_assets import Bundle, Environment

import numpy as np
from server.lib import prediction

# import visualization
import matplotlib.pyplot as plt

app = Flask(__name__)
app.config.from_envvar('APPLICATION_SETTINGS')
assets = Environment(app)

css = Bundle("src/main.css", output="dist/main.css")

assets.register("css", css)
css.build()


def create_figure1(data1):
    fig = plt.subplots(figsize=(12, 8))
    barWidth = 0.25
    normal = data1[0]
    user = data1[1]
    br1 = np.arange(len(normal))
    br2 = [x + barWidth for x in br1]
    # br3 = [x + barWidth for x in br2]
    plt.bar(br1, normal, color='g', width=barWidth,
            edgecolor='grey', label='Normal Value')
    plt.bar(br2, user, color='r', width=barWidth,
            edgecolor='grey', label="Yours Value")
    # plt.bar(br3, CSE, color ='b', width = barWidth, edgecolor ='grey', label ='CSE')
    plt.xlabel('Health status defining attributes',
               fontweight='bold', fontsize=15)
    plt.ylabel('respective values', fontweight='bold', fontsize=15)
    plt.xticks([r + barWidth for r in range(len(normal))], ['cp',
               'chol', 'fbs', 'exang', 'oldpeak', 'slope', 'ca', 'thal'])
    plt.legend()
    plt.savefig('static/plotng.png')


def create_figure2(data2):
    fig = plt.subplots(figsize=(12, 8))
    barWidth = 0.25
    normal = data2[0]
    user = data2[1]
    br1 = np.arange(len(normal))
    br2 = [x + barWidth for x in br1]
    plt.bar(br1, normal, color='g', width=barWidth,
            edgecolor='grey', label='Normal Value')
    plt.bar(br2, user, color='r', width=barWidth,
            edgecolor='grey', label="Yours Value")
    plt.xlabel('Health status defining attributes',
               fontweight='bold', fontsize=15)
    plt.ylabel('respective values', fontweight='bold', fontsize=15)
    plt.xticks([r + barWidth for r in range(len(normal))],
               ['trestbps', 'chol', 'thalach'])
    plt.legend()
    plt.savefig('static/plotng2.png')


def pred(age, sex, cp, trestbps, chol, fbs, restegc, thalac, exang, oldpeak, slope, ca, thal):
    print(age, sex, cp, trestbps, chol, fbs, restegc,
          thalac, exang, oldpeak, slope, ca, thal)
    return None


@app.route("/")
def home():
    return render_template('index.html')


@app.route("/notebook")
def notebook():
    return render_template('lg.html')


@app.route("/predict", methods=['POST'])
def predict():
    if request.method == 'POST':
        age = request.form['age']
        sex = request.form['sex']
        cp = request.form['cp']
        trestbps = request.form['trestbps']
        chol = request.form['chol']
        fbs = request.form['fbs']
        restecg = request.form['restecg']
        thalach = request.form['thalach']
        exang = request.form['exang']
        oldpeak = request.form['oldpeak']
        slope = request.form['slope']
        ca = request.form['ca']
        thal = request.form['thal']

        session["user"] = request.form["name"]

        if age == "" or trestbps == "" or chol == "" or thalach == "" or oldpeak == "" or ca == "":
            flash(
                "Age, Trestbps, Chol, Thalach, Oldpeak, and CA are required", category="error")
            return redirect(url_for('home'))

        results = prediction.preprocess(
            age, sex, cp, trestbps, restecg, chol, fbs, thalach, exang, oldpeak, slope, ca, thal)

        # database.crudOperation(age,sex,cp,trestbps,restecg,chol,fbs,thalach,exang,oldpeak,slope,ca,thal,result)
        # data1, data2 = visualization.visualizationpreprocess(
        #     age, sex, cp, trestbps, restecg, chol, fbs, thalach, exang, oldpeak, slope, ca, thal, result)
        # create_figure1(data1)
        # create_figure2(data2)
        # return render_template('result.html', prediction=result, nameofpatient=nameofpatient, model_counter=counter, total_counter=counter2)

        return render_template('index.html', results=results)
        # return res
    else:
        return render_template('index.html')


if __name__ == "__main__":
    app.run()
