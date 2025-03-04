# Financial Market Analytics Dashboard

## 📊 Overview
This project provides an **interactive dashboard** for analyzing stock market data. Built using **Streamlit**, **yfinance**, and **Plotly**, it allows users to visualize the performance of stocks (S&P 500 and custom tickers) over different time ranges, calculate key financial metrics, and plot stock prices and moving averages.

## 🚀 Features
- **Interactive stock selection**: Choose a stock from the **S&P 500** or enter a custom ticker.
- **Date range selection**: Choose any date range to display stock data.
- **Moving average toggle**: Optionally show the **50-day moving average**.
- **Key financial metrics**: Display critical stock metrics like **Market Cap**, **P/E Ratio**, **Dividend Yield**, and more.
- **Interactive Plotly charts**: View interactive charts that display stock prices and moving averages.

## 🛠 Installation

To get started, you'll need **Python** installed. Then, set up a **virtual environment** and install the necessary dependencies.

### 1. Clone this repository
```bash
git clone https://github.com/YOUR_USERNAME/financial-market-analytics-dashboard.git
cd financial-market-analytics-dashboard
```

### 2. Set up a virtual environment
```bash
python -m venv venv
```
### 3. Activate the virtual environment
- On Windows:
```bash
.\venv\Scripts\activate
```
- On macOS/Linux:
```bash
source venv/bin/activate
```
### 4. Install required dependencies
```bash
pip install yfinance streamlit plotly pandas
```
Alternatively, if you have a `requirements.txt` file, you can install all dependencies at once by running:

```bash
pip install -r requirements.txt
```

## ⚙️ Requirements
- yfinance: To fetch stock market data from Yahoo Finance.
- Streamlit: For building the web-based dashboard.
- Plotly: To create interactive stock charts.
- Pandas: To handle data and manipulate time-series.


## 🧑‍💻 Usage
Run the app with Streamlit:
```bash
streamlit run app.py
```
This will open the dashboard in your default web browser where you can select stocks, view financial metrics, and interact with charts.

## 🎯 Project Structure
```bash
financial-market-analytics-dashboard/
│
├── app.py              # Main Streamlit app file
├── requirements.txt    # List of dependencies
├── README.md           # Project documentation
└── assets/             # Store any static assets (like images)
```

## 📚 Key Financial Metrics
The dashboard displays the following metrics for each stock:

- Market Cap: The total value of a company's outstanding shares.
- P/E Ratio: Price-to-earnings ratio, a measure of stock valuation.
- Dividend Yield: The annual dividend income as a percentage of stock price.
- Beta: A measure of the stock's volatility compared to the market.
- 52-Week High/Low: The highest and lowest stock prices over the past year.

## 👨‍💻 Contributions
Feel free to fork this repository, submit issues, or create pull requests if you'd like to contribute. I welcome any suggestions or improvements!

## 📑 License
This project is licensed under the [MIT License](https://opensource.org/osd)

## 📜 Acknowledgments
Yahoo Finance for the stock data.
Streamlit for building the interactive dashboard.
Plotly for creating interactive charts.
