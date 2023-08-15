# app.pyという名前のファイルを作成してください。
import streamlit as st

st.title('Simple Streamlit App')
st.write('Welcome to my app!')

# テキストボックスを追加
user_input = st.text_input("あなたの名前を入力してください:", "")

# テキストボックスの内容を表示
if user_input:
    st.write(f"こんにちは、{user_input}さん！")
