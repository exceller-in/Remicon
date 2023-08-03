import numpy as np
import altair as alt
import pandas as pd
import streamlit as st
import os

st.header('동양 레미콘 출하일보')

st.write('2023-08-03 :sunglasses:')

df=pd.read_csv('./df.csv', encoding='EUC-KR')

st.write(df)

st.line_chart(df, x='index')