import streamlit as st
from streamlit_option_menu import option_menu
import streamlit.components.v1 as html
from  PIL import Image
import numpy as np
#import cv2
import pandas as pd
#from st_aggrid import AgGrid
import plotly.express as px
import io 

#Below is MC##
import streamlit as st
import pandas as pd
import yfinance as yf
import numpy as np
import pandas as pd
import os
from datetime import datetime, timedelta
import matplotlib.pyplot as plt
#import alpaca_trade_api as tradeapi
####
    
    
with st.sidebar:
    choose = option_menu("Qauntics", ["Home", "Analysis", "Portfolio Engineering", "Forecasting", "Contact"],
                         icons=['house', 'kanban', 'gear', 'activity','person lines fill'],
                         menu_icon="quora", default_index=1,
                         styles={
        "container": {"padding": "5!important", "background-color": "#fafafa"},
        "icon": {"color": "orange", "font-size": "25px"}, 
        "nav-link": {"font-size": "16px", "text-align": "left", "margin":"0px", "--hover-color": "#eee"},
        "nav-link-selected": {"background-color": "#02ab21"},
    }
    )
    
    
logo = Image.open(r'test.jpg')
profile = Image.open(r'test.jpg')
if choose == "Home":
    col1, col2 = st.columns( [0.8, 0.2])
    with col1:               # To display the header text using css style
        st.markdown(""" <style> .font {
        font-size:35px ; font-family: 'Cooper Black'; color: #FF9633;} 
        </style> """, unsafe_allow_html=True)
        st.markdown('<p class="font">About the Creator</p>', unsafe_allow_html=True)    
    with col2:               # To display brand log
        st.image(logo, width=130 )
    
    st.write("Our objective to create a world class application to help beginners understand the naunces of investing in equity markets")    
    st.image(profile, width=700 )
    
    
elif choose == "Forecasting":
    st.write("fORECASTING")

    
    
elif choose == "Portfolio Engineering":
    st.write("mCARLO")
    
elif choose == "Analysis":
    st.write("analysis")
    
    
