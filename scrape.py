import requests
import csv
from datetime import datetime
from bs4 import BeautifulSoup

URL = "https://www.saatchi.com/gold"   # آدرس دقیق صفحه نرخ طلا را باید جایگزین کنیم

def fetch_price():
    r = requests.get(URL, timeout=10)
    soup = BeautifulSoup(r.text, "html.parser")

    # این قسمت نیاز به دقت دارد چون ساختار ساعتچی ثابت نیست
    price_tag = soup.select_one(".price")  # باید بهت کمک کنم عنصر دقیق را پیدا کنیم
    price = price_tag.text.strip()

    return price

price = fetch_price()

with open("prices.csv", "a", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow([datetime.now(), price])
