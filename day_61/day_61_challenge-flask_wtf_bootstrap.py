from flask import Flask, render_template, request
from wtforms import EmailField, PasswordField, SubmitField, validators
from flask_wtf import FlaskForm
from flask_bootstrap import Bootstrap

adm_email = "email"
adm_psw = "password"


class LoginForm(FlaskForm):
    email = EmailField("Email", [validators.DataRequired(), validators.Email()])
    password = PasswordField("Password", [validators.DataRequired(), validators.Length(min=8)])
    submit = SubmitField("Log In")


app = Flask(__name__)
app.secret_key = "secret key"


Bootstrap(app)


@app.route("/")
def home():
    # return render_template("index.html")
    return render_template("index_bootstrap.html")


@app.route("/login", methods=["GET","POST"])
def login():
    login_form = LoginForm()
    if request.method == "POST" and login_form.validate():
        data = request.form.to_dict()
        print(data)
        if login_form.email.data == adm_email and login_form.password.data == adm_psw:
            return render_template("success.html", login_form=login_form)
        else:
            return render_template("denied.html", login_form=login_form)
    return render_template("login.html", login_form=login_form)


if __name__== "__main__":
    app.run(debug=True)

