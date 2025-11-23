from flask import Flask, request, render_template, redirect, url_for
from pymongo import MongoClient
import os

from utils import validate, generate_short_url, get_timestamp, get_short_url

app = Flask(__name__)
client = MongoClient(os.getenv('MONGODB_URI', 'mongodb://localhost:27017/'))
db = client["URL_SHORTENER"]
urls = db["urls"]

@app.route('/', methods=['GET'])
def home() -> str:
    return render_template('index.html')

@app.route('/shorten', methods=['POST'])
def shorten():
    org_url = request.form.get('url', '')
    print(f"Original URL: {org_url}")
    if validate(org_url):
        short_url = generate_short_url()
        _ts = get_timestamp()
        urls.insert_one({'short_url': short_url, 'original_url': org_url, 'timestamp': str(_ts)})
        print(f"Shortened URL: {short_url} at {_ts}")
        return render_template('index.html', short_url=short_url)

    return redirect(url_for('home'))


@app.route('/<path>', methods=['GET'])
def redirect_url(path: str):
    if validate(path):
        short_url = get_short_url(path)
        record = urls.find_one({'short_url': short_url})
        if record:
            return redirect(record['original_url'])
    return render_template('index.html', message=["Invalid URL or URL not found!"])