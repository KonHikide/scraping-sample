from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from bs4 import BeautifulSoup
import pandas as pd
import time

# --- ブラウザ設定 ---
options = webdriver.ChromeOptions()
options.add_argument("--headless")
options.add_argument("--no-sandbox")

# --- ドライバ起動 ---
service = Service()
driver = webdriver.Chrome(service=service, options=options)

# --- Wikipediaページにアクセス ---
url = "https://ja.wikipedia.org/wiki/Python"
driver.get(url)
time.sleep(3)

# --- HTML取得＆BeautifulSoupでパース ---
soup = BeautifulSoup(driver.page_source, "html.parser")

# --- コンテンツ内のすべての見出しを抽出 ---
headings = soup.select("#mw-content-text h2, #mw-content-text h3, #mw-content-text h4")

results = []
for tag in headings:
    text = tag.get_text(strip=True)
    # [編集] などの補助テキスト除去
    text = text.replace("[編集]", "")
    if text:
        results.append(text)

# --- CSV出力 ---
df = pd.DataFrame(results, columns=["見出しテキスト"])
df.to_csv("wikipedia_headings_selenium.csv", index=False, encoding="utf-8-sig")

print(f"抽出見出し数: {len(results)} 件")
print("出力ファイル：wikipedia_headings_final.csv")

driver.quit()

