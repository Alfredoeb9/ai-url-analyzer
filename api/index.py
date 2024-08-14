import os
from flask import Flask, jsonify
# from flask_cors import CORS
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from sqlalchemy import select
# from models.models import Item

# load_dotenv()

# Create a Flask app
app = Flask(__name__)
# CORS(app)

# Get environment variables
# TURSO_DATABASE_URL = os.environ.get("TURSO_DATABASE_URL")
# TURSO_AUTH_TOKEN = os.environ.get("TURSO_AUTH_TOKEN")

# construct special SQLAlchemy URL
# dbUrl = f"sqlite+{TURSO_DATABASE_URL}/?authToken={TURSO_AUTH_TOKEN}&secure=true"

# engine = create_engine(dbUrl, connect_args={'check_same_thread': False}, echo=True)

# app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///db.sqlite"

@app.route('/', methods=['GET'])
def home():
    # session = Session(engine)

    # get & print items
    # stmt = select(Item)

    # json_items = list(map(lambda item: item.to_json(), session.scalars(stmt)))
    return jsonify("hello")

    # for item in session.scalars(stmt):
    #     print(item)
    #     return jsonify(item)

@app.route('/about')
def about():
    return 'About'

if __name__ == '__main__':
    app.run(debug=True)