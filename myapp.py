# Import the yfinance library to fetch stock data from Yahoo Finance
import yfinance as yf

# Import streamlit library for creating web applications, aliased as 'st'
import streamlit as st

# Import pandas library for data manipulation and analysis, aliased as 'pd'
import pandas as pd

# Use streamlit's write function to display markdown text on the web page
st.write("""
# Simple Stock Price App

Shown are the stock closing price and volume of Google!

""")

# Comment referencing a tutorial article about getting stock data with Python
# https://towardsdatascience.com/how-to-get-stock-data-using-python-c0de1df17e75

# Comment explaining the next step
#define the ticker symbol

# Create a string variable containing Google's stock ticker symbol
tickerSymbol = 'GOOGL'

# Comment explaining the next step
#get data on this ticker

# Create a yfinance Ticker object using the ticker symbol to access stock data
tickerData = yf.Ticker(tickerSymbol)

# Comment explaining the next step
#get the historical prices for this ticker

# Fetch historical stock data for the specified time period
# start='2010-5-31' sets the beginning date for data collection
# end='2020-5-31' sets the ending date for data collection
tickerDf = tickerData.history(start='2010-5-31', end='2020-5-31')

# Display the raw data with proper column labels
st.write("""
## Historical Stock Data
""")

# Display the dataframe with all columns and proper formatting
st.dataframe(tickerDf)

# Display basic information about the dataset
st.write(f"""
### Dataset Information
- **Total Records**: {len(tickerDf)} days
- **Date Range**: {tickerDf.index.min().date()} to {tickerDf.index.max().date()}
- **Available Columns**: {', '.join(tickerDf.columns.tolist())}
""")

# Comment listing the columns available in the returned DataFrame
# Columns: Open, High, Low, Close, Volume, Dividends, Stock Splits

# Add section header for closing price chart
st.write("""
## Closing Price Over Time
""")

# Create a line chart displaying the closing prices over time
# tickerDf.Close accesses the 'Close' column from the DataFrame
st.line_chart(tickerDf['Close'])

# Add section header for volume chart
st.write("""
## Trading Volume Over Time
""")

# Create a line chart displaying the trading volume over time
# tickerDf.Volume accesses the 'Volume' column from the DataFrame
st.line_chart(tickerDf['Volume'])

# Display additional statistics
st.write("""
## Summary Statistics
""")

# Create two columns for better layout
col1, col2 = st.columns(2)

with col1:
    st.write("""
    ### Closing Price Statistics
    """)
    # Display closing price statistics
    price_stats = tickerDf['Close'].describe()
    st.dataframe(price_stats)

with col2:
    st.write("""
    ### Volume Statistics
    """)
    # Display volume statistics
    volume_stats = tickerDf['Volume'].describe()
    st.dataframe(volume_stats)

# Display correlation between different price metrics
st.write("""
## Price Correlation Matrix
""")
# Select only numeric price columns for correlation
price_columns = ['Open', 'High', 'Low', 'Close', 'Volume']
correlation_matrix = tickerDf[price_columns].corr()
st.dataframe(correlation_matrix)

# Add a section showing recent data
st.write("""
## Most Recent 10 Days
""")
# Display the last 10 rows of data with all columns visible
st.dataframe(tickerDf.tail(10))

# Add information about each column
st.write("""
## Column Definitions
- **Open**: Opening price at market open
- **High**: Highest price during the trading day
- **Low**: Lowest price during the trading day  
- **Close**: Closing price at market close
- **Volume**: Number of shares traded
""")