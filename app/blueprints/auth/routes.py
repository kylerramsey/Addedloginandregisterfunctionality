from flask import render_template, request, redirect, url_for, flash
from . import bp as app
from app.blueprints.main.models import User
from app import db
from flask_login import login_user, logout_user

@app.route("/login")
def login():
    if request.method == "POST":
        user = User.query.filter_by(email=request.form['inputEmail']).first()

        if user is None:
            flash(f'User with email {request.form["inputEmail"]} does not exist.')
        elif not user.check_my_password(request.form['inputPassword']):
            flash('Incorrect password!')
        else:
            login_user(user)
            flash('User logged in successfully')
            return redirect(url_for('main.home'))

        return render_template('login.html')

    else:
        return render_template('login.html')

@app.route("/register")
def register():
    if request.method == "POST":
        check_user = User.query.filter_by(
            email=request.form['inputEmail']).first()
        if check_user is not None:
            flash('User already exists')
        else:
            if request.form['inputPassword'] == request.form['inputPasswordConfirm']:
                new_user = User(
                    email=request.form['inputEmail'],
                    password='',
                    username=request.form['inputUsername'],
                    first_name=request.form['inputFirstName'],
                    last_name=request.form['inputLastName'],
                )
                new_user.hash_my_password(request.form['inputPassword'])
                db.session.add(new_user)
                db.session.commit()

                flash('User created successfully')
                return redirect(url_for('main.home'))
            else:
                flash('Passwords do not match')
        return render_template('register.html')
    else:
        return render_template('register.html')

@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('auth.login'))