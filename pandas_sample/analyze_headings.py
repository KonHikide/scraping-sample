import pandas as pd
from collections import Counter
import re

# --- 入力ファイル（selenium_sample から読み込み） ---
input_path = "../selenium_sample/wikipedia_headings_final.csv"
df = pd.read_csv(input_path)

# --- 1. 用途に関する見出しだけを抽出 ---
usage_keywords = ["用途", "利用", "使用", "活用"]
usage_related = df[df["見出しテキスト"].str.contains("|".join(usage_keywords), na=False)]

# --- 2. 単語頻度分析（日本語分かち書きせず単純分割） ---
words = []
for heading in df["見出しテキスト"].dropna():
    # 漢字・ひらがな・カタカナ・英語を分離（簡易版）
    tokens = re.findall(r'[一-龥ぁ-んァ-ンーa-zA-Z0-9]+', heading)
    words.extend(tokens)

# 頻度カウント（上位20個）
counter = Counter(words)
top_words = counter.most_common(20)
top_df = pd.DataFrame(top_words, columns=["単語", "出現数"])

# --- 3. 保存処理 ---
usage_related.to_csv("wikipedia_headings_usage.csv", index=False, encoding="utf-8-sig")
top_df.to_csv("heading_words.csv", index=False, encoding="utf-8-sig")

# --- 4. 結果出力 ---
print("=== 用途に関する見出し ===")
print(usage_related)

print("\n=== 見出しで頻出した単語 TOP 20 ===")
print(top_df)
print("\n出力ファイル:")
print("- wikipedia_headings_usage.csv")
print("- heading_words.csv")

