from bs4 import BeautifulSoup
import requests

URL = "https://saatchi.com"
headers = {"User-Agent": "Mozilla/5.0"}

r = requests.get(URL, headers=headers, timeout=30)
soup = BeautifulSoup(r.text, "html.parser")

block = soup.find("div", class_="w-100 float-left d-md-none latest-carat-price")
if block:
    span = block.find("span", class_="text-bold")
    if span:
        print("Gold price:", span.text.strip())
    else:
        print("Span not found")
else:
    print("Div not found")
