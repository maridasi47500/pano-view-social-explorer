from flask import Flask
from . import db


app = Flask(__name__)
db.init_app(app)

@app.route("/")
def hello_world():
    return "<p>Circle: Represents a panoramic view (e.g., sea, city, nature).square: Represents a social media post linked to that pano view.</p>"

