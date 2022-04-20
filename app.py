# Setup and import dependencies
from flask import Flask, jsonify, render_template, redirect
from sqlalchemy import create_engine, func
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from bson.json_util import dumps
from bson import json_util
import sqlalchemy
import json
import numpy as np


# Database setup and table references
engine = create_engine("postgresql://postgres:admin@localhost/National_Housing_Database")
Base = automap_base()
Base.prepare(engine, reflect = True)
Base.classes.keys()
Days_On_Market = Base.classes.days_on_market
Housing_Prices = Base.classes.housing_prices

# Flask setup
app = Flask(__name__)

# Flask routes
@app.route("/")
def Homepage():
    """List all API routes."""
    return (
        f"<h1>Welcome to the National Housing Prices API!</h1>"
        f"<h2>Find information about average housing price trends for cities across the United States from March 2018 to March 2020.</h2>"
        f"<strong><u>Available Routes:</u></strong><br/>"
        f"1. <strong>Housing Prices for 1 Bedroom Homes:</strong> /api/v1.0/1bedroom<br/>"
        f"2. <strong>Housing Prices for 2 Bedroom Homes:</strong> /api/v1.0/2bedroom<br/>"
        f"3. <strong>Housing Prices for 3 Bedroom Homes:</strong> /api/v1.0/3bedroom<br/>"
        f"4. <strong>Average Days on Market:</strong> /api/v1.0/days_on_market<br/>"
        f"<br/>"
        f"Note: API references <strong><i>Zillow House Price Data</i></strong> found on Kaggle: <i>https://www.kaggle.com/datasets/paultimothymooney/zillow-house-price-data</i>."
    )

# APP ROUTE 1 - HOUSING PRICES FOR 1 BD
@app.route("/api/v1.0/1bedroom")
def one_bedroom():
    # Create our session from Python to the DB
    session = Session(engine)
    one_bedroom_result = session.query(Housing_Prices.cityname, Housing_Prices.State, Housing_Prices.noofbeds, Housing_Prices.Mar2018, Housing_Prices.Apr2018, Housing_Prices.May2018, Housing_Prices.Jun2018, 
    Housing_Prices.Jul2018, Housing_Prices.Aug2018, Housing_Prices.Sep2018, Housing_Prices.Oct2018, Housing_Prices.Nov2018, Housing_Prices.Dec2018, Housing_Prices.Jan2019, Housing_Prices.Feb2019, 
    Housing_Prices.Mar2019, Housing_Prices.Apr2019, Housing_Prices.May2019, Housing_Prices.Jun2019, Housing_Prices.Jul2019, Housing_Prices.Aug2019, Housing_Prices.Sep2019, Housing_Prices.Oct2019, 
    Housing_Prices.Nov2019, Housing_Prices.Dec2019, Housing_Prices.Jan2020, Housing_Prices.Feb2020, Housing_Prices.Mar2020).\
    filter(Housing_Prices.noofbeds == 1).\
    all()
    session.close()
    # Convert the query results to a dictionary using CityName as the key
    one_bedroom = []
    for cityname, State, noofbeds, Mar2018, Apr2018, May2018, Jun2018, Jul2018, Aug2018, Sep2018, Oct2018, Nov2018, Dec2018, Jan2019, Feb2019, Mar2019, Apr2019, May2019, Jun2019, Jul2019, Aug2019, Sep2019, Oct2019, Nov2019, Dec2019, Jan2020, Feb2020, Mar2020 in one_bedroom_result:
        one_bedroom_dict = {}
        one_bedroom_dict["CityName"] = cityname
        one_bedroom_dict["State"] = State
        one_bedroom_dict["NoOfBeds"] = noofbeds
        one_bedroom_dict["Mar2018"] = Mar2018
        one_bedroom_dict["Apr2018"] = Apr2018
        one_bedroom_dict["May2018"] = May2018
        one_bedroom_dict["Jun2018"] = Jun2018
        one_bedroom_dict["Jul2018"] = Jul2018
        one_bedroom_dict["Aug2018"] = Aug2018
        one_bedroom_dict["Sep2018"] = Sep2018
        one_bedroom_dict["Oct2018"] = Oct2018
        one_bedroom_dict["Nov2018"] = Nov2018
        one_bedroom_dict["Dec2018"] = Dec2018
        one_bedroom_dict["Jan2019"] = Jan2019
        one_bedroom_dict["Feb2019"] = Feb2019
        one_bedroom_dict["Mar2019"] = Mar2019
        one_bedroom_dict["Apr2019"] = Apr2019
        one_bedroom_dict["May2019"] = May2019
        one_bedroom_dict["Jun2019"] = Jun2019
        one_bedroom_dict["Jul2019"] = Jul2019
        one_bedroom_dict["Aug2019"] = Aug2019
        one_bedroom_dict["Sep2019"] = Sep2019
        one_bedroom_dict["Oct2019"] = Oct2019
        one_bedroom_dict["Nov2019"] = Nov2019
        one_bedroom_dict["Dec2019"] = Dec2019
        one_bedroom_dict["Jan2020"] = Jan2020
        one_bedroom_dict["Feb2020"] = Feb2020
        one_bedroom_dict["Mar2020"] = Mar2020
        one_bedroom.append(one_bedroom_dict)
    # Return the JSON representation
    return jsonify(one_bedroom)

# APP ROUTE 2 - HOUSING PRICES FOR 2 BD
@app.route("/api/v1.0/2bedroom")
def two_bedroom():
    # Create our session from Python to the DB
    session = Session(engine)
    two_bedroom_result = session.query(Housing_Prices.cityname, Housing_Prices.State, Housing_Prices.noofbeds, Housing_Prices.Mar2018, Housing_Prices.Apr2018, Housing_Prices.May2018, Housing_Prices.Jun2018, 
    Housing_Prices.Jul2018, Housing_Prices.Aug2018, Housing_Prices.Sep2018, Housing_Prices.Oct2018, Housing_Prices.Nov2018, Housing_Prices.Dec2018, Housing_Prices.Jan2019, Housing_Prices.Feb2019, 
    Housing_Prices.Mar2019, Housing_Prices.Apr2019, Housing_Prices.May2019, Housing_Prices.Jun2019, Housing_Prices.Jul2019, Housing_Prices.Aug2019, Housing_Prices.Sep2019, Housing_Prices.Oct2019, 
    Housing_Prices.Nov2019, Housing_Prices.Dec2019, Housing_Prices.Jan2020, Housing_Prices.Feb2020, Housing_Prices.Mar2020).\
    filter(Housing_Prices.noofbeds == 2).\
    all()
    session.close()
    # Convert the query results to a dictionary using CityName as the key
    two_bedroom = []
    for cityname, State, noofbeds, Mar2018, Apr2018, May2018, Jun2018, Jul2018, Aug2018, Sep2018, Oct2018, Nov2018, Dec2018, Jan2019, Feb2019, Mar2019, Apr2019, May2019, Jun2019, Jul2019, Aug2019, Sep2019, Oct2019, Nov2019, Dec2019, Jan2020, Feb2020, Mar2020 in two_bedroom_result:
        two_bedroom_dict = {}
        two_bedroom_dict["CityName"] = cityname
        two_bedroom_dict["State"] = State
        two_bedroom_dict["NoOfBeds"] = noofbeds
        two_bedroom_dict["Mar2018"] = Mar2018
        two_bedroom_dict["Apr2018"] = Apr2018
        two_bedroom_dict["May2018"] = May2018
        two_bedroom_dict["Jun2018"] = Jun2018
        two_bedroom_dict["Jul2018"] = Jul2018
        two_bedroom_dict["Aug2018"] = Aug2018
        two_bedroom_dict["Sep2018"] = Sep2018
        two_bedroom_dict["Oct2018"] = Oct2018
        two_bedroom_dict["Nov2018"] = Nov2018
        two_bedroom_dict["Dec2018"] = Dec2018
        two_bedroom_dict["Jan2019"] = Jan2019
        two_bedroom_dict["Feb2019"] = Feb2019
        two_bedroom_dict["Mar2019"] = Mar2019
        two_bedroom_dict["Apr2019"] = Apr2019
        two_bedroom_dict["May2019"] = May2019
        two_bedroom_dict["Jun2019"] = Jun2019
        two_bedroom_dict["Jul2019"] = Jul2019
        two_bedroom_dict["Aug2019"] = Aug2019
        two_bedroom_dict["Sep2019"] = Sep2019
        two_bedroom_dict["Oct2019"] = Oct2019
        two_bedroom_dict["Nov2019"] = Nov2019
        two_bedroom_dict["Dec2019"] = Dec2019
        two_bedroom_dict["Jan2020"] = Jan2020
        two_bedroom_dict["Feb2020"] = Feb2020
        two_bedroom_dict["Mar2020"] = Mar2020
        two_bedroom.append(two_bedroom_dict)
    # Return the JSON representation
    return jsonify(two_bedroom)

# APP ROUTE 3 - HOUSING PRICES FOR 3 BD
@app.route("/api/v1.0/3bedroom")
def three_bedroom():
    # Create our session from Python to the DB
    session = Session(engine)
    three_bedroom_result = session.query(Housing_Prices.cityname, Housing_Prices.State, Housing_Prices.noofbeds, Housing_Prices.Mar2018, Housing_Prices.Apr2018, Housing_Prices.May2018, Housing_Prices.Jun2018, 
    Housing_Prices.Jul2018, Housing_Prices.Aug2018, Housing_Prices.Sep2018, Housing_Prices.Oct2018, Housing_Prices.Nov2018, Housing_Prices.Dec2018, Housing_Prices.Jan2019, Housing_Prices.Feb2019, 
    Housing_Prices.Mar2019, Housing_Prices.Apr2019, Housing_Prices.May2019, Housing_Prices.Jun2019, Housing_Prices.Jul2019, Housing_Prices.Aug2019, Housing_Prices.Sep2019, Housing_Prices.Oct2019, 
    Housing_Prices.Nov2019, Housing_Prices.Dec2019, Housing_Prices.Jan2020, Housing_Prices.Feb2020, Housing_Prices.Mar2020).\
    filter(Housing_Prices.noofbeds == 3).\
    all()
    session.close()
    # Convert the query results to a dictionary using CityName as the key
    three_bedroom = []
    for cityname, State, noofbeds, Mar2018, Apr2018, May2018, Jun2018, Jul2018, Aug2018, Sep2018, Oct2018, Nov2018, Dec2018, Jan2019, Feb2019, Mar2019, Apr2019, May2019, Jun2019, Jul2019, Aug2019, Sep2019, Oct2019, Nov2019, Dec2019, Jan2020, Feb2020, Mar2020 in three_bedroom_result:
        three_bedroom_dict = {}
        three_bedroom_dict["CityName"] = cityname
        three_bedroom_dict["State"] = State
        three_bedroom_dict["NoOfBeds"] = noofbeds
        three_bedroom_dict["Mar2018"] = Mar2018
        three_bedroom_dict["Apr2018"] = Apr2018
        three_bedroom_dict["May2018"] = May2018
        three_bedroom_dict["Jun2018"] = Jun2018
        three_bedroom_dict["Jul2018"] = Jul2018
        three_bedroom_dict["Aug2018"] = Aug2018
        three_bedroom_dict["Sep2018"] = Sep2018
        three_bedroom_dict["Oct2018"] = Oct2018
        three_bedroom_dict["Nov2018"] = Nov2018
        three_bedroom_dict["Dec2018"] = Dec2018
        three_bedroom_dict["Jan2019"] = Jan2019
        three_bedroom_dict["Feb2019"] = Feb2019
        three_bedroom_dict["Mar2019"] = Mar2019
        three_bedroom_dict["Apr2019"] = Apr2019
        three_bedroom_dict["May2019"] = May2019
        three_bedroom_dict["Jun2019"] = Jun2019
        three_bedroom_dict["Jul2019"] = Jul2019
        three_bedroom_dict["Aug2019"] = Aug2019
        three_bedroom_dict["Sep2019"] = Sep2019
        three_bedroom_dict["Oct2019"] = Oct2019
        three_bedroom_dict["Nov2019"] = Nov2019
        three_bedroom_dict["Dec2019"] = Dec2019
        three_bedroom_dict["Jan2020"] = Jan2020
        three_bedroom_dict["Feb2020"] = Feb2020
        three_bedroom_dict["Mar2020"] = Mar2020
        three_bedroom.append(three_bedroom_dict)
    # Return the JSON representation
    return jsonify(three_bedroom)

# APP ROUTE 4 - DAYS ON MARKET
@app.route("/api/v1.0/days_on_market")
def days_listed():
    # Create our session from Python to the DB
    session = Session(engine)
    days_listed_result = session.query(Days_On_Market.statename, Days_On_Market.Feb2018, Days_On_Market.Mar2018, Days_On_Market.Apr2018, Days_On_Market.May2018, Days_On_Market.Jun2018, Days_On_Market.Jul2018,
    Days_On_Market.Aug2018, Days_On_Market.Sep2018, Days_On_Market.Oct2018, Days_On_Market.Nov2018, Days_On_Market.Dec2018, Days_On_Market.Jan2019, Days_On_Market.Feb2019, Days_On_Market.Mar2019, 
    Days_On_Market.Apr2019, Days_On_Market.May2019, Days_On_Market.Jun2019, Days_On_Market.Jul2019, Days_On_Market.Aug2019, Days_On_Market.Sep2019, Days_On_Market.Oct2019, Days_On_Market.Nov2019, 
    Days_On_Market.Dec2019, Days_On_Market.Jan2020, Days_On_Market.Feb2020).all()
    session.close()
    # Convert the query results to a dictionary
    days_listed = []
    for statename, Feb2018, Mar2018, Apr2018, May2018, Jun2018, Jul2018, Aug2018, Sep2018, Oct2018, Nov2018, Dec2018, Jan2019, Feb2019, Mar2019, Apr2019, May2019, Jun2019, Jul2019, Aug2019, Sep2019, Oct2019, Nov2019, Dec2019, Jan2020, Feb2020 in days_listed_result:
        days_listed_dict = {}
        days_listed_dict["StateName"] = statename
        days_listed_dict["Feb2018"] = Feb2018
        days_listed_dict["Mar2018"] = Mar2018
        days_listed_dict["Apr2018"] = Apr2018
        days_listed_dict["May2018"] = May2018
        days_listed_dict["Jun2018"] = Jun2018
        days_listed_dict["Jul2018"] = Jul2018
        days_listed_dict["Aug2018"] = Aug2018
        days_listed_dict["Sep2018"] = Sep2018
        days_listed_dict["Oct2018"] = Oct2018
        days_listed_dict["Nov2018"] = Nov2018
        days_listed_dict["Dec2018"] = Dec2018
        days_listed_dict["Jan2019"] = Jan2019
        days_listed_dict["Feb2019"] = Feb2019
        days_listed_dict["Mar2019"] = Mar2019
        days_listed_dict["Apr2019"] = Apr2019
        days_listed_dict["May2019"] = May2019
        days_listed_dict["Jun2019"] = Jun2019
        days_listed_dict["Jul2019"] = Jul2019
        days_listed_dict["Aug2019"] = Aug2019
        days_listed_dict["Sep2019"] = Sep2019
        days_listed_dict["Oct2019"] = Oct2019
        days_listed_dict["Nov2019"] = Nov2019
        days_listed_dict["Dec2019"] = Dec2019
        days_listed_dict["Jan2020"] = Jan2020
        days_listed_dict["Feb2020"] = Feb2020
        days_listed.append(days_listed_dict)
    # Return the JSON representation
    return jsonify(days_listed)

if __name__ == '__main__':
    app.run(debug=True)