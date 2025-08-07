# -*- coding: utf-8 -*-
"""
Created on Sun Apr 28 12:25:10 2024

@author: hardik polamarasetti
"""
from flask import Flask, request, render_template, redirect, url_for, flash
from werkzeug.utils import secure_filename
from bs4 import BeautifulSoup
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import os

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'user_uploads/'  
app.config['ALLOWED_EXTENSIONS'] = {'html', 'htm'}
app.secret_key = 'your_secret_key'  

# check the upload directory exists
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in app.config['ALLOWED_EXTENSIONS']

def preprocess_and_vectorize(filepaths):
    documents = []
    for filepath in filepaths:
        with open(filepath, 'r', encoding='utf-8') as file:
            soup = BeautifulSoup(file.read(), 'html.parser')
            text = soup.get_text()
            documents.append(text)
    vectorizer = TfidfVectorizer(stop_words='english')
    tfidf_matrix = vectorizer.fit_transform(documents)
    return vectorizer, tfidf_matrix

def search_files(vectorizer, tfidf_matrix, query):
    query_vec = vectorizer.transform([query])
    scores = cosine_similarity(query_vec, tfidf_matrix).flatten()
    return scores

@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        files = request.files.getlist('file')
        for file in files:
            if file and allowed_file(file.filename):
                filename = secure_filename(file.filename)
                file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        flash('Files uploaded successfully!')
        return redirect(url_for('upload_file'))
    return render_template('upload.html')

@app.route('/search', methods=['GET', 'POST'])
def search():
    if request.method == 'POST':
        keyword = request.form['keyword']
        filepaths = [os.path.join(app.config['UPLOAD_FOLDER'], filename) for filename in os.listdir(app.config['UPLOAD_FOLDER'])]
        vectorizer, tfidf_matrix = preprocess_and_vectorize(filepaths)
        scores = search_files(vectorizer, tfidf_matrix, keyword)
        results = sorted(zip(filepaths, scores), key=lambda x: x[1], reverse=True)
        return render_template('results.html', results=results, keyword=keyword)
    return render_template('search.html')

if __name__ == '__main__':
    app.run(debug=True)