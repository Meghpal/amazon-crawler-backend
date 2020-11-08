import requests
import lxml

from bs4 import BeautifulSoup
from helpers.get_header import get_header


def get_list(url):
    base_url = url.split(r"/")[2]
    headers = get_header()
    page = requests.get(url, headers=headers)
    soup = BeautifulSoup(page.content, "lxml")

    items = soup.select(".s-result-item:not(.s-widget)")
    try_next = soup.select(".a-last a")
    next_page = (
        "https://" + base_url + try_next[0]["href"] if len(try_next) > 0 else None
    )

    response = []

    for item in items:
        data = item.select("h2 .a-link-normal.a-text-normal")[0]
        img_link = item.select(".aok-relative img")[0]
        prices = item.select(".a-price .a-offscreen")
        response.append(
            {
                "name": data.find("span").get_text(),
                "img": img_link["src"],
                "price": [
                    prices[0].get_text() if len(prices) > 0 else None,
                    prices[1].get_text() if len(prices) > 1 else None,
                ],
                "url": "https://" + base_url + data["href"],
            }
        )
    return {"list": response, "next": next_page}
