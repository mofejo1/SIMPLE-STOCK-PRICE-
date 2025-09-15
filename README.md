# Simple Stock Price App

A simple web application built with **Streamlit** and **yfinance** that displays Google's historical stock data including closing prices and trading volume.

## 📊 Features

- **Real-time Stock Data**: Fetches historical stock data from Yahoo Finance
- **Interactive Charts**: Displays closing prices and trading volume as line charts
- **Web Interface**: Clean, user-friendly Streamlit web interface
- **Historical Analysis**: Shows data from 2010 to 2020 for trend analysis

## 🚀 Demo

The app displays two main visualizations:

1. **Stock Closing Prices**: Line chart showing Google's stock price over time
2. **Trading Volume**: Line chart showing daily trading volume

## 🛠️ Installation

### Prerequisites

- Python 3.7 or higher
- pip package manager

### Required Libraries

```bash
pip install streamlit yfinance pandas
```

### Optional (for better performance)

```bash
# For macOS users
xcode-select --install
pip install watchdog
```

## 📁 Project Structure

```
Simple Stock Price/
├── myapp.py          # Main application file
└── README.md         # This file
```

## 🏃‍♂️ How to Run

1. **Clone or download** the project files
2. **Navigate** to the project directory:
   ```bash
   cd "Simple Stock Price"
   ```
3. **Run the application**:
   ```bash
   streamlit run myapp.py
   ```
4. **Open your browser** and go to:
   - Local URL: `http://localhost:8501`
   - Network URL: `http://192.168.1.96:8501` (or your network IP)

## 💻 Code Overview

### Key Components

- **yfinance**: Fetches stock data from Yahoo Finance API
- **streamlit**: Creates the web application interface
- **pandas**: Handles data manipulation and analysis

### Main Functions

```python
# Fetch Google stock data
tickerData = yf.Ticker('GOOGL')
tickerDf = tickerData.history(start='2010-5-31', end='2020-5-31')

# Display charts
st.line_chart(tickerDf.Close)    # Closing prices
st.line_chart(tickerDf.Volume)   # Trading volume
```

## 🔧 Customization

### Change Stock Symbol

Modify the `tickerSymbol` variable in `myapp.py`:

```python
tickerSymbol = 'AAPL'  # For Apple
tickerSymbol = 'TSLA'  # For Tesla
tickerSymbol = 'MSFT'  # For Microsoft
```

### Change Date Range

Modify the start and end dates:

```python
tickerDf = tickerData.history(start='2015-1-1', end='2025-1-1')
```

### Add More Charts

You can add additional visualizations:

```python
st.line_chart(tickerDf.High)     # High prices
st.line_chart(tickerDf.Low)      # Low prices
st.line_chart(tickerDf.Open)     # Opening prices
```

## 📈 Data Fields Available

The yfinance library provides these data columns:

- **Open**: Opening price
- **High**: Highest price of the day
- **Low**: Lowest price of the day
- **Close**: Closing price
- **Volume**: Number of shares traded
- **Dividends**: Dividend payments
- **Stock Splits**: Stock split information

## ⚠️ Troubleshooting

### Common Issues

1. **ValueError: Setting period, start and end is nonsense**

   - **Solution**: Don't use `period` parameter when specifying both `start` and `end` dates

2. **Module not found errors**

   - **Solution**: Install required packages using pip

3. **Connection errors**
   - **Solution**: Check internet connection for Yahoo Finance API access

## 🤝 Contributing

Feel free to fork this project and submit pull requests for improvements:

- Add more stock symbols and comparison features
- Implement additional chart types (candlestick, moving averages)
- Add data export functionality (CSV, Excel)
- Improve UI/UX design with custom styling
- Add technical indicators (RSI, MACD, Bollinger Bands)
- Implement real-time data updates

## 📚 Learning Resources

- [Streamlit Documentation](https://docs.streamlit.io/)
- [yfinance Documentation](https://pypi.org/project/yfinance/)

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

---

**Happy Trading! 📊🚀**
