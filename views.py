from flask import request
from helpers.get_list import get_list
from helpers.get_reviews import get_reviews


def index():
    json = request.json
    url = f"""https://{json["base_url"]}/s?k={json["search_string"]}"""
    return get_list(url)


def fetch_reviews():
    return get_reviews(request.json)