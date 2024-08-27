import os
from flask import Flask, jsonify, request
from flask_cors import CORS
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from sqlalchemy import select
from models.models import Item
from langchain_core.prompts import ChatPromptTemplate
from langchain_ollama.llms import OllamaLLM

load_dotenv()

# Create a Flask app
app = Flask(__name__)
CORS(app)

# Get environment variables
TURSO_DATABASE_URL = os.environ.get("TURSO_DATABASE_URL")
TURSO_AUTH_TOKEN = os.environ.get("TURSO_AUTH_TOKEN")

# construct special SQLAlchemy URL
dbUrl = f"sqlite+{TURSO_DATABASE_URL}/?authToken={TURSO_AUTH_TOKEN}&secure=true"

engine = create_engine(dbUrl, connect_args={'check_same_thread': False}, echo=True)



@app.route('/api/home', methods=['GET', 'POST'])
def home():
    template = """Question: {question}

    Answer: You are a comedian, scan the url given in the question and make fun of the contents inside in less than 200 words."""

    prompt = ChatPromptTemplate.from_template(template)

    model = OllamaLLM(model="llava-llama3:8b")

    chain = prompt | model

    data = request.json
    param1 = data.get('param1')
    # session = Session(engine)

    # get & print items
    # stmt = select(Item)
    # json_items = list(map(lambda item: item.to_json(), session.scalars(stmt)))

    print("Ollama is thinking give us a couple minutes")
    answer = chain.invoke({"question": param1})
    
    return jsonify(answer)


@app.route('/about')
def about():
    return 'About'

if __name__ == '__main__':
    app.run(debug=True)