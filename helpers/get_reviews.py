import requests
from bs4 import BeautifulSoup
import lxml
import time


def get_reviews(
    url, base_url, accumulator=None, chunksize=50, callback=None, kwargs=None
):
    def get_from_page(url, base_url, accumulator, chunksize):
        time.sleep(5)
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36"
        }
        page = requests.get(url, headers=headers)
        soup = BeautifulSoup(page.content, "lxml")

        reviews = soup.select(".review")
        try_next = soup.select(".a-last:not(.a-disabled) a")
        next_page = (
            "https://" + base_url + try_next[0]["href"] if len(try_next) > 0 else None
        )

        for review in reviews:
            accumulator.append(
                review.select(".review-text")[0].get_text(separator="\n").strip()
            )

        if len(accumulator) >= chunksize or next_page is None:
            f = open("reviews.txt", "a")
            f.write(str(accumulator))
            f.close()
            accumulator = []

        if next_page is not None:
            get_from_page(next_page, base_url, accumulator, chunksize)

    if accumulator is None:
        accumulator = []

    get_from_page(url, base_url, accumulator, chunksize)

    if callback is not None:
        if kwargs is not None:
            callback(**kwargs)
        else:
            callback()
