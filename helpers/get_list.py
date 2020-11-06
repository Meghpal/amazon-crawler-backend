import requests
from bs4 import BeautifulSoup
import lxml


def get_list(url):
    base_url = url.split(r"/")[2]
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36"
    }
    page = requests.get(url, headers=headers)
    soup = BeautifulSoup(page.content, "lxml")

    items = soup.select(".s-result-item:not(.s-widget)")
    next_page = soup.select(".a-last a")[0]["href"]

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
    return {"list": response, "next": "https://" + base_url + next_page}
