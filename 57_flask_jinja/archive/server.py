from flask import Flask, render_template
import random
import datetime
import requests
import json

app = Flask(__name__)

@app.route("/")
def home():
    random_number = random.randint(1,10)
    year_current = datetime.datetime.now().year
    return render_template("index.html", random_number = random_number, year_current = year_current)

@app.route("/guess/<name_entered>")
def name_analysis(name_entered):
    #get gender
    response_gender = requests.get(url=f"https://api.genderize.io?name={name_entered}")
    response_gender.raise_for_status()
    data_gender = response_gender.json()
    analyzed_gender = data_gender["gender"]
    #get age
    response_age = requests.get(url=f"https://api.agify.io?name={name_entered}")
    response_age.raise_for_status()
    data_age = response_age.json()
    analyzed_age = data_age["age"]
    return render_template("name_analysis.html", name_entered = name_entered, analyzed_gender = analyzed_gender, analyzed_age = analyzed_age)

@app.route("/blogs")
def get_blogs():
    #api npoint somehow blocked, using a local file
    with open("57_flask_jinja\\blog-data.json", "r") as file:
        data_blogs = json.load(file)
    return render_template("blogs.html", data_blogs = data_blogs)
    
if __name__ == "__main__":
    app.run(debug=True)