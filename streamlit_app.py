import streamlit as st
import pandas as pd
from numpy.random import default_rng as rng

st.title("Hello World")

# 创建边栏
with st.sidebar:
    st.header("About this app")
    st.write("This is my first app!")

# 创建一个带分隔栏的抬头
st.header("This is a header with a divider", divider="rainbow")

st.markdown("This is markdown.")

# 创建两个分栏
st.subheader("st.columns")
col1, col2 = st.columns(2)
with col1:
    x = st.slider("Choose an x value", 1, 10)
with col2:
    st.write("The value of :red[x] is", x)

# 创建一个数据框并绘制面积图
st.subheader("st.area_chart")
df = pd.DataFrame(rng(0).standard_normal((20, 3)), columns=["a", "b", "c"])

st.area_chart(df)
