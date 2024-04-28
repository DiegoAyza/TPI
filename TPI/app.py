from flask import Flask, render_template, request, jsonify
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
import os

from chatbot import generate_response


app = Flask(__name__)

# Directorio de las plantillas
template_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), 'templates'))
app.template_folder = template_dir


@app.route('/')
def index():
    return render_template('index2.html')



@app.route('/ask', methods=['POST'])
def ask():
    question = request.json['question']
    response = generate_response(question)
    return jsonify({'response': response})


if __name__ == '__main__':
    app.run(debug=True)