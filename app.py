#!/usr/bin/env python
# coding: utf-8

from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
import mars_scraping

# Create an instance of Flask
app = Flask(__name__)

#Use flask_pymongo to set up mongo connection
app.config["MONGO_URI"] = "mongodb://localhost:27017/mars_app"
mongo = PyMongo(app)

@app.route("/")
def index():
   mars = mongo.db.mars.find_one()
   return render_template("index.html", mars=mars)

@app.route("/scrape")
def scrape():
   mars = mongo.db.mars
   mars_data = mars_scraping.scrape_all()
   mars.replace_one({}, mars_data, upsert=True)
   return "Scraping Successful"

if __name__ == "__main__":
    app.run(debug=True)