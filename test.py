import requests

URL = "https://saatchi.com"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
}

try:
    r = requests.get(URL, headers=headers, timeout=30)
    print("Status code:", r.status_code)
    print("First 200 chars of page:\n", r.text[:200])
except Exception as e:
    print("Error:", e)
