from flask import render_template
from . import bp as app
from app.blueprints.main.models import Car
  
@app.route("/")
def home():

    cars = Car.query.all()

    cars.sort(key=lambda car: car.date_created, reverse=True)

    print(cars)

    context = {
        "cars": cars,
        "user": "Christopher"
    }

    return render_template('index.html', **context)

@app.route("/about")
def about():
    return render_template('about.html')

@app.route("/contact")
def contact():
    return render_template('contact.html')

@app.route("/blog")
def blog():
    return render_template('blog.html')