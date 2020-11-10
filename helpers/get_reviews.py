import requests
import lxml
import time
import random

from bs4 import BeautifulSoup
from helpers.save_data import save_data
from helpers.get_header import get_header


def get_reviews(url, data, accumulator=None, chunksize=50, callback=None, kwargs=None):
    def get_from_page(url, data, accumulator, chunksize):
        time.sleep(random.randint(2, 12))
        headers = get_header()
        page = requests.get(url, headers=headers)
        soup = BeautifulSoup(page.content, "lxml")

        reviews = soup.select(".review")
        try_next = soup.select(".a-last:not(.a-disabled) a")
        next_page = (
            "https://" + data["base_url"] + try_next[0]["href"]
            if len(try_next) > 0
            else None
        )

        for review in reviews:
            accumulator.append(
                review.select(".review-text")[0].get_text(separator="\n").strip()
            )

        if len(accumulator) >= chunksize or next_page is None:
            save_data(accumulator, data["id"], "a")
            accumulator = []

        if next_page is not None:
            get_from_page(next_page, data, accumulator, chunksize)

    if accumulator is None:
        accumulator = []

    save_data("", data["id"], "w")
    get_from_page(url, data, accumulator, chunksize)

    if callback is not None:
        if kwargs is not None:
            callback(**kwargs)
        else:
            callback()
