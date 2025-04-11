import streamlit as st
from data_fetcher import fetch_random_ai_product
from analyzer import analyze_product
from utils import render_report
import os
from dotenv import load_dotenv

load_dotenv()

st.set_page_config(page_title="AI 产品竞品分析器", page_icon="🤖")
st.title("🤖 AI 产品每日竞品分析")
st.markdown("每天自动从 Product Hunt 抽一款 AI 产品并生成分析报告")

if st.button("🎲 抽一款今日AI产品"):
    product = fetch_random_ai_product()
    st.subheader(f"🎯 今日产品：{product['name']}")
    st.write(product['tagline'])
    st.markdown(f"[🔗 官网链接]({product['url']})")

    if st.button("🧠 开始分析"):
        report = analyze_product(product)
        st.markdown(render_report(report), unsafe_allow_html=True)
