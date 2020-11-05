import requests
from bs4 import BeautifulSoup
import lxml

# def scrape(base_url, search_string):


def get_list(base_url, search_string):
    URL = f"https://{base_url}/s?k={search_string}"
    print(URL)
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36"
    }
    page = requests.get(URL, headers=headers)
    soup = BeautifulSoup(page.content, "lxml")

    items = soup.select(".s-result-item:not(.s-widget)")

    response = []

    for item in items:
        data = item.select("h2 .a-link-normal.a-text-normal")[0]
        imglink = item.select(".aok-relative img")[0]
        response.append(
            {
                "product": data.find("span").get_text(),
                "img": imglink["src"],
                "url": data["href"],
            }
        )
    return {"list": response, "next": "go"}
