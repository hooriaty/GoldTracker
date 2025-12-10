import requests
from bs4 import BeautifulSoup

URL = "https://saatchi.com"

def fetch_price():
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
                      "(KHTML, like Gecko) Chrome/114.0 Safari/537.36"
    }

    r = requests.get(URL, headers=headers, timeout=25)  # زمان را بیشتر کن
    r.raise_for_status()

    soup = BeautifulSoup(r.text, "html.parser")

    block = soup.find("div", class_="latest-carat-price")
    if not block:
        raise ValueError("DIV for price not found")

    span = block.find("span", class_="text-bold")
    if not span:
        raise ValueError("SPAN for price not found")

    price_text = span.get_text(strip=True)
    return price_text
