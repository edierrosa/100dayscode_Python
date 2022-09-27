from flask import Flask, render_template, request
from smtplib import SMTP
import os
from pathlib import Path
import dotenv


dotenv_path = Path("/Users/Agilulfo/python/py310/.virtualenvs/100daysCode/day_60.txt")
dotenv.load_dotenv(dotenv_path=dotenv_path)


smtp_yahoo = os.environ["SMTP_YAHOO"]
user_yahoo = os.environ["USER_YAHOO"]
password_yahoo = os.environ["PASSWORD_YAHOO"]
gmail_account = os.environ["GMAIL_ACCOUNT"]


app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")

@app.route("/login", methods=["POST"])
def login():
    credentials = request.form.to_dict()
    print(credentials)
    return f"<p>{credentials['name'], credentials['password']}<p>"

if __name__ == "__main__":
    app.run(debug=True)