from flask import Flask, render_template
import requests as r


app = Flask(__name__)


@app.route('/')
def home():
    return render_template("index.html")


@app.route('/example')
def example():
    return render_template("day_58-bootstrap_exercises.html")


if __name__ == "__main__":
    app.run(debug=True)
