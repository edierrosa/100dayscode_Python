from turtle import title
from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
import requests
from sqlalchemy_utils.functions import database_exists
import os, dotenv
from pathlib import Path


# Environment Variables
dotenv_path = Path("/Users/Agilulfo/python/py310/.virtualenvs/100daysCode/day_63.txt")
dotenv.load_dotenv(dotenv_path=dotenv_path)
tmdb_apikey = os.environ["API_KEY"]
tmdb_token = os.environ["API_READ_TOKEN"]


# Flask app
app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///movie-list.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


# Bootstrap
Bootstrap(app)


# SQLAlchemy database
db = SQLAlchemy(app)


# Update form
class RateMovieForm(FlaskForm):
    rating = StringField('Your Rating')
    review = StringField('Your Review')
    submit = SubmitField('Submit')


# Add form
class AddMovieForm(FlaskForm):
    title = StringField('Movie Title', validators=[DataRequired()])
    submit = SubmitField('Add Movie')


class Movie(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50), unique=True, nullable=False)
    year = db.Column(db.Integer, nullable=False)
    description = db.Column(db.String(150), nullable=False)
    rating = db.Column(db.Float, nullable=True)
    ranking = db.Column(db.Integer, nullable=True)
    review = db.Column(db.String(300), nullable=True)
    img_url = db.Column(db.String(150), nullable=False)

if not database_exists("sqlite:///movie-list.db"):
    with app.app_context():
        db.create_all()


@app.route("/")
def home():
    movie_list = Movie.query.order_by(Movie.rating).all()
    for i in range(len(movie_list)):
        movie_list[i].ranking = len(movie_list) - i
    db.session.commit()
    return render_template("index.html", movie_list=movie_list)


@app.route("/update", methods=["GET", "POST"])
def update():
    update_form = RateMovieForm()
    movie_id = request.args.get("movie_id")
    movie = Movie.query.get(movie_id)
    if update_form.validate_on_submit():
        movie.rating = float(update_form.rating.data)
        movie.review = update_form.review.data
        db.session.commit()
        return redirect(url_for("home"))
    return render_template("edit.html", movie=movie, form=update_form)


@app.route("/delete")
def delete():
    movie_id = request.args.get("movie_id")
    db.session.delete(Movie.query.get(movie_id))
    db.session.commit()
    return redirect(url_for("home"))


@app.route("/find", methods=["GET", "POST"])
def find():
    add_form = AddMovieForm()
    if add_form.validate_on_submit():
        movie = add_form.title.data
        movies_data = requests.get(url="https://api.themoviedb.org/3/search/movie", params={
            "api_key": tmdb_apikey,
            "query": movie}).json()
        print(movies_data)
        return render_template("select.html", movies_data=movies_data)
    return render_template("add.html", form=add_form)


@app.route("/add")
def add():
    movie_id = request.args.get("movie_id")
    if movie_id:
        movie_data = requests.get(url=f"https://api.themoviedb.org/3/movie/{movie_id}", params={
            "api_key": tmdb_apikey}).json()
        print(movie_data)
        movie = Movie(
            id = movie_data["id"],
            title = movie_data["original_title"],
            year = movie_data["release_date"].split("-")[0],
            img_url = f"http://image.tmdb.org/t/p/w300{movie_data['poster_path']}",
            description = movie_data["overview"]
        )
        print(movie.img_url)
        db.session.add(movie)
        db.session.commit()
        return redirect(url_for("update", movie_id=movie_id))


if __name__ == '__main__':
    app.run(debug=True)

