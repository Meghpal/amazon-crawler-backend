import requests
from bs4 import BeautifulSoup
import lxml
import time


def get_reviews(json_dict, type="all_reviews"):
    info = json_dict["url"]
    data = ()
    if len(info.split(r"url=%2F")) > 1:
        splt = info.split(r"%2F")
        base_url = splt[0].split(r"/")[2]
        data = {"base_url": base_url, "name": splt[1], "id": splt[3]}
    else:
        splt = info.split(r"/")
        data = {"base_url": splt[2], "name": splt[3], "id": splt[5]}
    url = f"""https://{data["base_url"]}/{data["name"]}/product-reviews/{data["id"]}/ref=cm_cr_dp_d_show_all_btm?ie=UTF8&pageNumber=1&reviewerType={type}"""
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36"
    }
    page = requests.get(url, headers=headers)
    soup = BeautifulSoup(page.content, "lxml")

    reviews = soup.select(".review")
    # next_page = data["base_url"] + soup.select(".a-last a")[0]["href"]

    response = []

    for review in reviews:
        response.append(review.select(".review-text")[0].get_text())

    return {"list": response}
