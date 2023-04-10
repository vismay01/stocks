import yfinance as yf
import streamlit as st 

st.write("""
# Stock Price App

Shown are teh stock **closing price** and ***volume*** of Adani Enterprises Limites!

""")

tickerSymbol = 'ADANIENT.NS'
tickerData = yf.Ticker(tickerSymbol)
tickerDf = tickerData.history(period='1d', start='2022-4-6', end='2023-4-6')

st.write("""
## Closing Price    
""")

st.line_chart(tickerDf.Close)

st.write("""
## Volume
""")
st.line_chart(tickerDf.Volume)