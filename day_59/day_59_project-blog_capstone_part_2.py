from flask import Flask, render_template, request
import requests as r
from smtplib import SMTP
import os
from pathlib import Path
import dotenv


data = r.get("https://api.npoint.io/c790b4d5cab58020d391").json()


dotenv_path = Path("path_to_dotenv")
dotenv.load_dotenv(dotenv_path=dotenv_path)


smtp_yahoo = os.environ["SMTP_YAHOO"]
user_yahoo = os.environ["USER_YAHOO"]
password_yahoo = os.environ["PASSWORD_YAHOO"]
gmail_account = os.environ["GMAIL_ACCOUNT"]


app = Flask(__name__)


def send_email(msg, email=gmail_account):
    with SMTP(smtp_yahoo, port=587) as connection:
        connection.starttls()
        connection.login(user=user_yahoo, password=password_yahoo)
        connection.sendmail(from_addr=user_yahoo, to_addrs=email, msg=msg)


@app.route('/')
def home():
    return render_template("index.html", posts=data)


@app.route('/<page>')
def render_page(page):
    return render_template(page)


@app.route("/posts/<int:id>")
def show_post(id):
    post = next(_ for _ in data if _["id"] == id)
    print(post["id"])
    return render_template("post.html", post=post)

@app.route("/form-entry", methods=["POST"])
def receive_data():
    if request.method == "POST":
        data = request.form.to_dict()
        print(data)
        msg = f"Subject: New msg\n\nName: {data['name']}\nEmail: {data['email']}\nPhone: {data['phone']}\nMessage: {data['message']}"
        send_email(msg)
        return render_template("contact.html", msg_status=True)


if __name__ == "__main__":
    app.run(debug=True)
