from flask import request
from helpers.get_list import get_list
from helpers.get_reviews import get_reviews
from threading import Thread


def search():
    json = request.json
    url = f"""https://{json["base_url"]}/s?k={json["search_string"]}"""
    return get_list(url)


def search_next():
    return get_list(request.json["next"])


def fetch_reviews():
    info = request.json["url"]
    data = {}

    if len(info.split(r"url=%2F")) > 1:
        splt = info.split(r"%2F")
        base_url = splt[0].split(r"/")[2]
        data = {"base_url": base_url, "name": splt[1], "id": splt[3]}
    else:
        splt = info.split(r"/")
        data = {"base_url": splt[2], "name": splt[3], "id": splt[5]}

    url = f"""https://{data["base_url"]}/{data["name"]}/product-reviews/{data["id"]}/ref=cm_cr_dp_d_show_all_btm?ie=UTF8&pageNumber=1&reviewerType={type}"""
    thread = Thread(
        target=get_reviews,
        kwargs={"url": url, "base_url": data["base_url"]},
    )
    thread.start()
    return "Initiated"