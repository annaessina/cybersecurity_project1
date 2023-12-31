from flask import render_template, request, redirect, flash, session, abort
from sqlalchemy.sql import text
from app import app
from db import db
from spas import search_spas, delete_spa, get_all_spas, add_spa
from reviews import get_reviews, add_review
import users

'''
FLAW 5. How to fix.

from logging import getLogger, ERROR

logger = getLogger('login_activity')
logger.setLevel(ERROR)

def log_access_control_failure(username):
    logger.error(f'Access control failure for user: {username}')

'''

@app.route("/")
def index():
    return render_template("home.html")

@app.route("/new")
def new():
    spas = get_all_spas()
    return render_template("new.html", spas=spas)

@app.route("/spas")
def spas():
    username = session['username']
    spas = get_all_spas()
    is_admin = users.admins(username)
    return render_template("spas.html", count=len(spas), spas=spas, is_admin = is_admin)
 

@app.route("/review")
def reviews():
    spas_all = get_reviews()
    return render_template("reviews.html", count=len(spas_all), spas=spas_all)

@app.route("/add_review", methods=["POST"])
def reviews_to_db():
    spa_id = request.form.get('spa_id')
    stars = request.form.get('stars')
    comment = request.form.get('comment')

    if session["csrf_token"] != request.form["csrf_token"]:
        abort(403)

    if not stars:
        return redirect(request.referrer)
    add_review(spa_id, stars, comment)
    return redirect('/review')

@app.route("/send", methods=["POST"])
def send():
    name = request.form["name"]
    city = request.form["city"]
    categories = request.form.get('categories')
    address = request.form["address"]

    '''FLAW 6'''
    if len(address) == 0:
        return render_template("error.html", message="Anna kylpylän osoite")
    '''FLAW 6. How to fix.
    address = request.form["address"].strip()
    if not address or len(address) > 255:
        return render_template("error.html", message="Empty or too long address")'''



    if session["csrf_token"] != request.form["csrf_token"]:
        abort(403)

    if add_spa(name, address, city, categories):
        return redirect("/spas")
    else:
        message = "spa with name {} already exists".format(name)
        return render_template("new.html", message=message)

@app.route("/login",methods=["POST"])
def login():
    username = request.form["username"]
    password = request.form["password"]

    if users.login(username,password) == False:
        flash('Invalid username or password')
        return redirect('/')
    else:
        return redirect("/spas")
    '''
    FLAW 5. How to fix.

    logger.error('Login attempt initiated')

    username = request.form["username"]
    password = request.form["password"]

    if users.login(username,password) == False:
        # Logging failed login attempt
        logger.error(f'Failed login attempt for user: {username}')
        log_access_control_failure(username)

        flash('Invalid username or password')
        return redirect('/')
    else:
        # Logging successful login
        logger.error(f'User {username} successfully logged in')

        return redirect("/spas")'''

@app.route("/logout")
def logout():
    users.logout()
    return redirect("/")

@app.route("/create_account", methods=["POST"])
def create_account():
    username = request.form["username"]
    password = request.form["password"]

    if not username or not password:
        flash('Väärä käyttäjä tai salasana')
        return redirect('/')

    if len(username) < 4:
        flash('Käyttäjänimen täytyy olla vähintään 4 merkkiä')
        return redirect('/')
    if len(password) < 6:
        flash('Salasanan täytyy olla vähintään 6 merkkiä')
        return redirect('/')
    users.create_account(username,password)

    return redirect('/spas')

@app.route("/search", methods=["POST"])
def search():
    substring = request.form.get('name')
    filtered_spas = search_spas(substring)

    html_response = f"<html><body>Count: {len(filtered_spas)}<br>spas: {filtered_spas}</body></html>"
    return html_response

    '''
    FLAW 4. How to fix.
    return render_template('filtered.html', count=len(filtered_spas), spas=filtered_spas)
    '''

@app.route("/delete", methods=["POST"])
def delete():

    '''
    #FLAW 2. How to fix.

    if session["csrf_token"] != request.form["csrf_token"]:
        abort(403)
    '''

    '''
    #FLAW 1. How to fix.

    username = session.get('username')
    if not users.admins(username):
        abort(401)  

    '''
    spa_id = request.form.get('spa_id')
    delete_spa(spa_id)
    return redirect("/spas")
