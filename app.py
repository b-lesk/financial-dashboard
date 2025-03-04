import streamlit as st
import yfinance as yf
import pandas as pd
import plotly.graph_objects as go

# Load S&P 500 stock tickers and their company names for dropdown selection
@st.cache_data
def get_sp500_tickers_and_names():
    # Read the S&P 500 data from the Wikipedia page
    table = pd.read_html("https://en.wikipedia.org/wiki/List_of_S%26P_500_companies")
    
    # Inspect the first few rows of the table to see the column names
    print(table[0].head())  # This will print the first few rows of the dataframe to help us see the correct column names
    
    # Extract tickers and names using the correct columns
    tickers = table[0]['Symbol'].tolist()
    company_names = table[0]['Security'].tolist()  # 'Security' is the column name for company names
    return tickers, company_names

# Streamlit UI
st.title("📊 Financial Market Analytics Dashboard")
st.sidebar.header("Filters")

# Get tickers and company names
tickers, company_names = get_sp500_tickers_and_names()

# Create a dictionary of tickers and their company names
ticker_company_dict = dict(zip(tickers, company_names))

# Dropdown menu for stock selection, displaying both ticker and company name
selected_ticker = st.sidebar.selectbox(
    "Select a Stock",
    options=[f"{ticker} - {ticker_company_dict[ticker]}" for ticker in tickers],
    index=tickers.index("AAPL")
)

# Extract the ticker symbol from the selected option
selected_ticker_symbol = selected_ticker.split(" - ")[0]

# Date Range Selection
start_date = st.sidebar.date_input("Start Date", pd.to_datetime("2023-01-01"))
end_date = st.sidebar.date_input("End Date", pd.to_datetime("today"))

# Toggle Moving Averages
show_moving_avg = st.sidebar.checkbox("Show 50-day Moving Average", True)

# Fetch stock data
stock = yf.Ticker(selected_ticker_symbol)
hist = stock.history(start=start_date, end=end_date)

if hist.empty:
    st.warning(f"No data found for {selected_ticker_symbol}")
else:
    # Plot stock price
    st.subheader(f"{selected_ticker_symbol} Stock Price")

    fig = go.Figure()
    fig.add_trace(go.Scatter(x=hist.index, y=hist["Close"], mode="lines", name="Closing Price"))

    if show_moving_avg:
        hist["50_MA"] = hist["Close"].rolling(window=50).mean()
        fig.add_trace(go.Scatter(x=hist.index, y=hist["50_MA"], mode="lines", name="50-Day MA", line=dict(dash="dot")))

    fig.update_layout(title=f"{selected_ticker_symbol} Stock Price Over Time", xaxis_title="Date", yaxis_title="Price (USD)")
    st.plotly_chart(fig)

    # Show Key Financial Metrics
    st.subheader("📈 Key Financial Metrics")
    stock_info = stock.info
    metrics = {
        "Market Cap": stock_info.get("marketCap"),
        "P/E Ratio": stock_info.get("trailingPE"),
        "Dividend Yield": stock_info.get("dividendYield"),
        "Beta": stock_info.get("beta"),
        "52-Week High": stock_info.get("fiftyTwoWeekHigh"),
        "52-Week Low": stock_info.get("fiftyTwoWeekLow"),
    }

    # Display metrics in a table format
    metrics_df = pd.DataFrame.from_dict(metrics, orient="index", columns=["Value"])
    st.table(metrics_df)

st.markdown("Developed by Benjamin Lesko | Data sourced from Yahoo Finance")
