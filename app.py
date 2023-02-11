import json
import os

import requests
from flask import Flask, render_template, request

import utils

app = Flask(__name__)

access_token = os.environ['FB_API_TOKEN']
base_url = 'https://graph.facebook.com/v15.0/ads_archive'


@app.route('/search')
def facebook_ads():
    search_terms = request.args.get('search_terms')
    ad_reached_countries = ','.join(request.args.getlist('ad_reached_countries'))

    search_url = f'{base_url}?search_terms={search_terms}' \
                 f'&access_token={access_token}' \
                 f'&ad_reached_countries={ad_reached_countries}'
    response = requests.get(search_url)
    response_json = json.loads(response.text)
    ads = response_json['data']
    sorted_ads = sorted(ads, key=lambda x: x['impressions'], reverse=True)

    return render_template('templates/search.html', ads=sorted_ads)


@app.route('/')
def search():
    return render_template('index.html', countries=utils.get_countries())


if __name__ == '__main__':
    app.run(debug=True)
