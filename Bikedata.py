from pygwalker.api.streamlit import StreamlitRenderer
import pandas as pd
import streamlit as st
import pygwalker as pyg

# Adjust the width of the Streamlit page
st.set_page_config(
    page_title="Use Pygwalker In Streamlit for Bike Data",
    layout="wide"
)

# Import your data
#df = pd.read_csv("https://kanaries-app.s3.ap-northeast-1.amazonaws.com/public-datasets/bike_sharing_dc.csv")
df_bike = pd.read_csv('E:\\2025\\KSR_datavizion_JAN-JUNE\\March\\dax\\Bike_Data.csv')

pyg_html = pyg.to_html(df_bike)
st.components.v1.html(pyg_html, height=1200, scrolling=True)



pyg_app = StreamlitRenderer(df_bike)
 
pyg_app.explorer()
    