# Setup and import dependencies
from flask import Flask, jsonify
from sqlalchemy import create_engine, func
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from bson.json_util import dumps
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

# Flask Routes
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
    one_bedroom_result = session.query(Housing_Prices.CityName, Housing_Prices.State, Housing_Prices.NoOfBeds, Housing_Prices.Mar2018, Housing_Prices.Apr2018, Housing_Prices.May2018, Housing_Prices.Jun2018, Housing_Prices.Jul2018, Housing_Prices.Aug2018, Housing_Prices.Sep2018, Housing_Prices.Oct2018, Housing_Prices.Nov2018, Housing_Prices.Dec2018, Housing_Prices.Jan2019, Housing_Prices.Feb2019, Housing_Prices.Mar2019, Housing_Prices.Apr2019, Housing_Prices.May2019, Housing_Prices.Jun2019, Housing_Prices.Jul2019, Housing_Prices.Aug2019, Housing_Prices.Sep2019, Housing_Prices.Oct2019, Housing_Prices.Nov2019, Housing_Prices.Dec2019, Housing_Prices.Jan2020, Housing_Prices.Feb2020, Housing_Prices.Mar2020).filter(Housing_Prices.NoOfBeds == 1).all()
    session.close()
    # Convert the query results to a dictionary using Index as the key
    one_bedroom = []
    for CityName, State, NoOfBeds, Mar2018 in one_bedroom_result:
        one_bedroom_dict = {}
        one_bedroom_dict["CityName"] = CityName
        one_bedroom_dict["State"] = State
        one_bedroom_dict["NoOfBeds"] = NoOfBeds
        one_bedroom_dict["Mar2018"] = Mar2018
        one_bedroom.append(one_bedroom_dict)
    # Return the JSON representation
    return jsonify(one_bedroom)

if __name__ == '__main__':
    app.run(debug=True)