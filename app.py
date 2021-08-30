from flask import Flask, render_template, redirect, url_for
from flask_pymongo import PyMongo
import scraping

app = Flask(__name__)

# Use flask_pymongo to set up mongo connection
app.config["MONGO_URI"] = "mongodb://localhost:27017/mars_app"
mongo = PyMongo(app)
# Create a new variable to hold the database collection reference
mars_collection = mongo.db.mars

@app.route("/")
def index():
   mars = mars_collection.find_one()
   return render_template("index.html", mars=mars)

@app.route("/scrape")
def scrape():
   mars_data = scraping.scrape_all()
   mars_collection.update({}, mars_data, upsert=True)
   return redirect('/', code=302)

if __name__ == "__main__":
   app.run()