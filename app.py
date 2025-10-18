import streamlit as st

# ページ設定
st.set_page_config(page_title="STYLE SYNC AI", page_icon="🧠")

# タイトル
st.title("🧠 STYLE SYNC AI（コーデ診断テスト）")

# 説明文
st.write("こんにちは！これはあなたのファッションタイプを診断するAIアプリです。")

# 入力フォーム
name = st.text_input("あなたの名前を入力してください：")
style = st.selectbox("好きなスタイルを選んでください：", ["カジュアル", "ストリート", "モード", "ヴィンテージ", "アウトドア"])

# 診断ボタン
if st.button("診断スタート！"):
    st.success(f"{name} さんは「{style}」スタイルが似合うタイプです！✨")

# デバッグ用
st.write("✅ アプリが正常に起動しています。")

import openai
import os

openai.api_key = os.getenv("OPENAI_API_KEY")

if st.button("AIコーデ診断スタート！"):
    if name and style:
        with st.spinner("AIがあなたに合うコーデを考えています...👕"):
            prompt = f"{name}さんは{style}スタイルが好きです。この人におすすめのファッションコーデを3つ提案してください。"
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[{"role": "user", "content": prompt}]
            )
            st.write("👗 **AIの提案:**")
            st.write(response.choices[0].message["content"])
    else:
        st.warning("名前とスタイルを入力してください！")
