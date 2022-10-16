from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy_utils.functions import database_exists


# Flask app
app = Flask(__name__)


# Flask app config
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///bookshelf-collection.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


# SQLAlchemy database
db = SQLAlchemy(app)


class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    author = db.Column(db.String(250), nullable=False)
    rating = db.Column(db.Float, nullable=False)

    def __repr__(self):
            return f'<Book {self.title} {self.author} {self.rating}>'



# Home
@app.route('/')
def home():
    if not database_exists("sqlite:///bookshelf-collection.db"):
            db.create_all()
    all_books = db.session.query(Book).all()
    return render_template("index.html", all_books=all_books)


# Add 
@app.route("/add", methods=["GET", "POST"])
def add():
    if request.method == "POST":
        db.session.add(Book(**request.form))
        db.session.commit()
        return redirect(url_for("home"))
    return render_template("add.html")

# Edit
@app.route("/edit", methods=["GET", "POST"])
def edit():
    if request.method == "POST":
        book_id = request.form["id"]
        book = Book.query.get(book_id)
        book.rating = request.form["rating"]
        db.session.commit()
        return redirect(url_for("home"))
    book_id = request.args.get("book_id")
    book = Book.query.get(book_id)
    return render_template("edit.html", book=book )

# Delete
@app.route("/delete")
def delete():
    book_id = request.args.get("book_id")
    book = Book.query.get(book_id)
    db.session.delete(book)
    db.session.commit()
    return redirect(url_for("home"))


if __name__ == "__main__":
    app.run(debug=True)

