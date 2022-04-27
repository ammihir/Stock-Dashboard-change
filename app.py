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
    
    st.markdown(""" <style> .font {
    font-size:35px ; font-family: 'Cooper Black'; color: #FF9633;} 
    </style> """, unsafe_allow_html=True)
    st.markdown('<p class="font">Financial Dashboard</p>', unsafe_allow_html=True)

    #st.subheader('Equity Data')
    st.markdown('The data will be pulled from Yahoo finances')


    st.title('Fundamental Analysis')

    #st.header('This is the header below')

    tickers = ('idfc.ns','HDFCBANK.NS' ,'HDB','^NSEI','ABB')

    dropdown = st.selectbox('Pick your stock', tickers)



    start  =st.date_input('Start',value = pd.to_datetime('2021-01-01'))
    end = st.date_input('End',value = pd.to_datetime('today'))

    ticker = yf.Ticker(dropdown).info


    import datetime
    end_52 = pd.to_datetime('today').date()
    start_52 = end_52 - datetime.timedelta(365)

    df_52 = yf.download(dropdown, start_52, end_52)


    st.write('52-high',round(df_52['Adj Close'].min(),1))
    st.write('Current Price', ticker['currentPrice'])
    st.write('52-low',round(df_52['Adj Close'].max(),1))
    st.write('PEG ratio', ticker['pegRatio'])

    st.write('Market Cap', ticker['marketCap'])




    #st.text(hdb['sector'])

    def relativeret(df):
        rel = df.pct_change()
        cumret = (1+rel).cumprod()-1
        cumret = cumret.fillna(0)
        return cumret

    if len(dropdown)  > 0:
        #df = yf.download(dropdown, start, end)['Adj Close']

        df = relativeret(yf.download(dropdown, start, end)['Adj Close'])
        st.write("**BELOW IS RETURNS**")   
        st.line_chart(df)

    st.write("**BELOW IS CLOSING PRICE**")    

    st.line_chart(yf.download(dropdown, start, end)['Adj Close'])




    
