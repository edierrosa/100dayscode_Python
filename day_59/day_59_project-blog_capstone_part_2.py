from flask import Flask, render_template
import requests as r


data = r.get("https://api.npoint.io/c790b4d5cab58020d391").json()


app = Flask(__name__)


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


if __name__ == "__main__":
    app.run(debug=True)
