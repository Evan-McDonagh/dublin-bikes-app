from flask import render_template, url_for
from dublinbikes.getdata import get_locations
from dublinbikes import app

@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', locationdata=get_locations())


@app.route('/about')
def about():
    return render_template('about.html', title='About')
