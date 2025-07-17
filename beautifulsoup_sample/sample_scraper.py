import requests
from bs4 import BeautifulSoup
import json

url = "https://docs.python.org/ja/3/tutorial/index.html"
headers = {
    "User-Agent": "Mozilla/5.0"
}

response = requests.get(url, headers=headers)
response.encoding = 'utf-8'

soup = BeautifulSoup(response.text, "html.parser")

headings = []
for li in soup.select("li.toctree-l1 > a"):
    text = li.get_text(strip=True)
    if text:
        headings.append(text)

print("検出見出し数：", len(headings))

with open("output.json", "w", encoding="utf-8") as f:
    json.dump(headings, f, ensure_ascii=False, indent=2)

print("抽出完了：output.json に保存しました")

