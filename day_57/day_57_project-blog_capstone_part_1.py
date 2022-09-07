from flask import Flask, render_template
import requests as r
from post import Post


post_data = r.get("https://api.npoint.io/c790b4d5cab58020d391").json()
posts = [Post(**item) for item in post_data]


app = Flask(__name__)


@app.route('/')
def home():
    return render_template("index.html", posts=posts)


@app.route("/posts/<int:id>")
def show_post(id):
    post_show = next(filter(lambda x: x.id == id, posts))
    print(post_show.id)
    return render_template("post.html", post=post_show)


if __name__ == "__main__":
    app.run(debug=True)
