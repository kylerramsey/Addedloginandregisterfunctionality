from flask import jsonify, request, redirect
from . import bp as app
from app.blueprints.main.models import Car
from app import db

@app.route("/car_post", methods=["POST"])
def car_post():
    make_input = request.form['makeInput']
    model_input = request.form['modelInput']
    year_input = request.form['yearInput']
    color_input = request.form['colorInput']
    price_input = request.form['priceInput']
    user = 1

    # instantiate new post
    new_car = Car(make=make_input, model=model_input, year=year_input, color=color_input, price=price_input, user_id=user)

    # adding new post to database
    db.session.add(new_car)
    db.session.commit()

    return redirect("http://127.0.0.1:5000/")