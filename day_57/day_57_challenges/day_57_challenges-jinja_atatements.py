from datetime import date
from flask import Flask, render_template
import random
import requests as r


app = Flask(__name__)


@app.route("/")
def home():
    random_number = random.randint(1, 10)
    current_year = date.today().year
    return render_template("index.html", num=random_number, current_year=current_year)


@app.route("/guess/<name>")
def guess(name):
    genderize_data = r.get("https://api.genderize.io",
                           params={"name": name}).json()["gender"]
    agify_data = r.get("https://api.agify.io",
                       params={"name": name}).json()["age"]
    return render_template("guess.html", name=name, gender=genderize_data, age=agify_data)


@app.route("/blog")
def blog():
    blog_data = r.get("https://api.npoint.io/c790b4d5cab58020d391").json()
    return render_template("blog.html", blog_data=blog_data)


if __name__ == "__main__":
    app.run(debug=True)
