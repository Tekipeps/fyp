from flask import Flask
from flask import render_template, redirect, url_for, request, flash, session
from flask import Flask
from flask_assets import Bundle, Environment

from server.lib import prediction

# import visualization
import matplotlib.pyplot as plt

app = Flask(__name__)
app.config.from_envvar('APPLICATION_SETTINGS')
assets = Environment(app)

css = Bundle("src/main.css", output="dist/main.css")

assets.register("css", css)
css.build()

def pred(age, sex, cp, trestbps, chol, fbs, restegc, thalac, exang, oldpeak, slope, ca, thal):
    print(age, sex, cp, trestbps, chol, fbs, restegc,
          thalac, exang, oldpeak, slope, ca, thal)
    return None


@app.route("/")
def home():
    return render_template('index.html')


@app.route("/notebook")
def notebook():
    return render_template('heart_disease.html')


@app.route("/predict", methods=['POST'])
def predict():
    if request.method == 'POST':
        age = request.form['Age']
        sex = request.form['Sex']
        chestpaintype = request.form['ChestPainType']
        restingbp = request.form['RestingBP']
        cholesterol = request.form['Cholesterol']
        fastingbs = request.form['FastingBS']
        restecg = request.form['RestingECG']
        maxhr = request.form['MaxHR']
        exerciseangina = request.form['ExerciseAngina']
        oldpeak = request.form['Oldpeak']
        st_slope = request.form['ST_Slope']

        session["user"] = request.form["name"]

        if age == "" or restingbp == "" or cholesterol == "" or maxhr == "" or oldpeak == "":
            flash(
                "Age, Trestbps, Chol, Thalach, Oldpeak, and CA are required", category="error")
            return redirect(url_for('home'))
        
        user_input =[int(age), sex, chestpaintype, int(restingbp), int(cholesterol), int(fastingbs), restecg, int(maxhr), exerciseangina, float(oldpeak), st_slope]

        results = prediction.process(user_input)
        return render_template('index.html', results=results)
    else:
        return render_template('index.html')


if __name__ == "__main__":
    app.run()
