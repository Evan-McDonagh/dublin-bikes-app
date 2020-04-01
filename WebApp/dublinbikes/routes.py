from flask import render_template, url_for, request
from dublinbikes import app
from dublinbikes.getdata import get_locations, get_current_station_data, get_all_station_data, get_model_predictions
import json

print(app)
@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', locationdata=get_locations(), modeldata=get_model_predictions())


@app.route('/about')
def about():
    return render_template('about.html', title='About')

@app.route('/query')
def query():
    # get the argument from the get request
    id = request.args.get('id')
    if id =="all":
        station_info = json.dumps(get_all_station_data())
    else:
        # invoke function to run sql query and store results
        station_info = json.dumps(get_current_station_data(id))
    return station_info
