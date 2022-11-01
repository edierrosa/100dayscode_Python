from flask import Flask, jsonify, render_template, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql.expression import func


app = Flask(__name__)


API_KEY = "TopSecretAPIKey"

##Connect to Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///full path to db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


##Cafe TABLE Configuration
class Cafe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), unique=True, nullable=False)
    map_url = db.Column(db.String(500), nullable=False)
    img_url = db.Column(db.String(500), nullable=False)
    location = db.Column(db.String(250), nullable=False)
    seats = db.Column(db.String(250), nullable=False)
    has_toilet = db.Column(db.Boolean, nullable=False)
    has_wifi = db.Column(db.Boolean, nullable=False)
    has_sockets = db.Column(db.Boolean, nullable=False)
    can_take_calls = db.Column(db.Boolean, nullable=False)
    coffee_price = db.Column(db.String(250), nullable=True)

    def to_dict(self):
        return {column.name: getattr(self, column.name) for column in self.__table__.columns}


@app.route("/")
def home():
    return render_template("index.html")
    

## HTTP GET - Read Record
@app.route("/random")
def get_random_cafe():
    random_cafe = db.session.query(Cafe).order_by(func.random()).first()
    return jsonify(random_cafe.to_dict())


@app.route("/all")
def get_all_cafes():
    all_cafes = [cafe.to_dict() for cafe in db.session.query(Cafe).all()]
    # all_cafes = [{k:v for k, v in cafe.__dict__.items() if k != "_sa_instance_state"} for cafe in db.session.query(Cafe).all()]
    return jsonify(all_cafes)


@app.route("/search")
def get_cafes_by_location():
    location = request.args.get("loc")
    cafes_by_location = [cafe.to_dict() for cafe in db.session.query(Cafe).filter_by(location=location).all()]
    return jsonify(cafes_by_location) if cafes_by_location else jsonify(error={"Not Found": f"No cafes at {location}"})


## HTTP POST - Create Record
@app.route("/add", methods=["POST"])
def add_cafe():
    new_cafe = Cafe(
    name = request.form.get("name"),
    map_url = request.form.get("map_url"),
    img_url = request.form.get("img_url"),
    location = request.form.get("location"),
    seats = request.form.get("seats"),
    has_toilet = bool(request.form.get("has_toilet")),
    has_wifi = bool(request.form.get("has_wifi")),
    has_sockets = bool(request.form.get("has_sockets")),
    can_take_calls = bool(request.form.get("can_take_calls")),
    coffee_price = request.form.get("coffee_price")
    )
    db.session.add(new_cafe)
    db.session.commit()
    return jsonify(response={"success": "Successfully added the new cafe."})


## HTTP PUT/PATCH - Update Record
@app.route("/update_price/<int:cafe_id>", methods=["PATCH"])
def update_price(cafe_id):
    cafe = db.session.query(Cafe).get(cafe_id)
    new_price = request.args.get("new_price")
    if cafe:
        cafe.coffee_price = new_price
        db.session.commit()
        return jsonify(response={"success": "Successfully updated the price."})
    else:
        return jsonify(error={"Not Found": "Cafe id not found."}), 404


## HTTP DELETE - Delete Record
@app.route("/report-close/<int:cafe_id>", methods=["DELETE"])
def delete_cafe(cafe_id):
    api_key = request.args.get("api-key")
    if api_key == API_KEY:
        cafe = db.session.query(Cafe).get(cafe_id)
        if cafe:
            db.session.delete(cafe)
            db.session.commit()
            return jsonify(response={"success": "Successfully deleted the cafe."}), 200
        else:
            return jsonify(error={"Not Found": "Cafe id not found."}), 404
    else:
        return jsonify(error={"Forbidden": "Not allowed. Make sure you have a valid api-key."}), 403


if __name__ == '__main__':
    app.run(debug=True)
