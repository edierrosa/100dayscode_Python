from flask import Flask, render_template


app = Flask(__name__, template_folder="../day_42")


@app.route("/")
def home():
    return render_template("day_42_project-personal_web_improved.html")


if __name__ == "__main__":
    app.run(debug=True)
