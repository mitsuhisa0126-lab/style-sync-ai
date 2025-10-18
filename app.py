import streamlit as st
from openai import OpenAI
import os

# ページ設定
st.set_page_config(page_title="STYLE SYNC AI", page_icon="🧠")

st.title("🧠 STYLE SYNC AI（コーデ診断テスト）")
st.write("こんにちは！これはあなたのファッションタイプをAIが診断するアプリです。")

# 入力欄
name = st.text_input("あなたの名前を入力してください：")
style = st.selectbox("好きなスタイルを選んでください：", ["カジュアル", "モード", "ストリート", "古着", "きれいめ", "アメカジ", "スポーティ"])

# アプリ状態
st.write("✅ アプリが正常に起動しています。")

# OpenAI 初期化
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# AI診断ボタン
if st.button("AIコーデ診断スタート！"):
    if name and style:
        with st.spinner("AIがあなたに似合うコーデを考えています...👕"):
            prompt = f"""
{name}さんは{style}系のファッションが好きです。
この人におすすめのコーディネートを3つ提案してください。

それぞれ以下のフォーマットで出力してください：
1️⃣ コーデ名（例：「カジュアル・アーバン」など）
2️⃣ 解説（似合う理由・ポイントなど）
3️⃣ おすすめブランドまたはタグ（例：#Patagonia #L.L.Bean #古着 #ユニクロ）

出力は日本語で、優しいトーンでお願いします。
"""
            # OpenAI Chat API呼び出し（新仕様対応）
            response = client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": "あなたは日本のファッションに詳しい一流のスタイリストです。"},
                    {"role": "user", "content": prompt}
                ]
            )

            # 応答表示
            answer = response.choices[0].message.content
            st.subheader("👗 あなたにおすすめのコーデ")
            st.markdown(answer)
    else:
        st.warning("名前とスタイルを入力してください！")
