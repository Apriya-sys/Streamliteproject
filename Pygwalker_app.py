import pygwalker as pyg
from pygwalker.api.streamlit import StreamlitRenderer  # Import the StreamlitRenderer
import streamlit.components.v1 as components
import pandas as pd
import streamlit as st

# Adjust the width of the Streamlit page
st.set_page_config(
    page_title="Use Pygwalker In Streamlit",
    layout="wide"
)

# Add Title
st.image("https://th.bing.com/th/id/OIP.pyK8cnRkuXuKNx0RaqSqBgHaHa?rs=1&pid=ImgDetMain", width=100)
st.title("Bike Data DashBoard using pygwalker in streamlit app",)
st.subheader("Created by RApriya")
st.markdown("### 📊 _Data Overview_")



# Add subtitle
SUB_TITLE = """
<div>
    <span>Don't know how to use PyGWalker? Check out the </span>
    <a target="_blank" href="https://docs.kanaries.net/graphic-walker/create-data-viz">document</a>
    <span> for more details!</span>
</div>
<br/>
<div>
    <span>Reference: </span>
    <a target="_blank" href="https://docs.kanaries.net/pygwalker/use-pygwalker-with-streamlit.en">Exploring Data and Sharing Findings with Pygwalker and Streamlit</a>
</div>
"""
components.html(SUB_TITLE, height=80)

# Import your data
#df = pd.read_csv("https://kanaries-app.s3.ap-northeast-1.amazonaws.com/public-datasets/bike_sharing_dc.csv")
df_bike = pd.read_csv('E:\\2025\\KSR_datavizion_JAN-JUNE\\March\\dax\\Bike_Data.csv')


# Embed the HTML into the Streamlit app
pyg_html = pyg.to_html(df_bike)
st.components.v1.html(pyg_html, height=1200, scrolling=True)

pyg_app = StreamlitRenderer(df_bike)
 
pyg_app.explorer()
    