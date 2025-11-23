from flask import Flask, request, render_template, redirect, url_for
from pymongo import MongoClient
import os

from utils import validate, generate_short_url, get_timestamp

app = Flask(__name__)
client = MongoClient(os.getenv('MONGO_URI', 'mongodb://localhost:27017/urlshortener'))
BASE_URL = os.getenv('BASE_URL', 'http://localhost:5000/')
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
        slug = generate_short_url()
        short_url = BASE_URL + slug
        _ts = get_timestamp()
        urls.insert_one({'slug': slug, 'original_url': org_url, 'timestamp': str(_ts)})
        return render_template('index.html', short_url=short_url)

    return redirect(url_for('home'))


@app.route('/<slug>', methods=['GET'])
def redirect_url(slug: str):
    if len(slug) == 8:
        record = urls.find_one({'short_url': slug})
        if record:
            return redirect(record['original_url'])
    return render_template('index.html', message=["Invalid URL or URL not found!"])


if __name__=="__main__":
    app.run(debug=False, host='0.0.0.0', port=5000)