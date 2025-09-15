import yfinance as yf
import streamlit as st
import pandas as pd

# Create a string variable containing Google's stock ticker symbol
tickerSymbol = 'GOOGL'


#get data on this ticker

# Create a yfinance Ticker object using the ticker symbol to access stock data
tickerData = yf.Ticker(tickerSymbol)

 
#get the historical prices for this ticker

# Fetch historical stock data for the specified time period
# period='1d' means daily data intervals
tickerDf = tickerData.history(start='2010-5-31', end='2020-5-31')

# Open   High   Low Close   Volume   Dividends   Stock Splits

# Create a line chart displaying the closing prices over time
# tickerDf.Close accesses the 'Close' column from the DataFrame
st.line_chart(tickerDf.Close)

# Create a line chart displaying the trading volume over time
# tickerDf.Volume accesses the 'Volume' column from the DataFrame
st.line_chart(tickerDf.Volume)