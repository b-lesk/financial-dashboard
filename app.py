import streamlit as st
import yfinance as yf
import pandas as pd
import plotly.graph_objects as go

# Load S&P 500 stock tickers for dropdown selection
@st.cache_data
def get_sp500_tickers():
    table = pd.read_html("https://en.wikipedia.org/wiki/List_of_S%26P_500_companies")
    return sorted(table[0]['Symbol'].tolist())

# Streamlit UI
st.title("📊 Financial Market Analytics Dashboard")
st.sidebar.header("Filters")

# Dropdown menu for stock selection
tickers = get_sp500_tickers()
selected_ticker = st.sidebar.selectbox("Select a Stock", tickers, index=tickers.index("AAPL"))

# Date Range Selection
start_date = st.sidebar.date_input("Start Date", pd.to_datetime("2023-01-01"))
end_date = st.sidebar.date_input("End Date", pd.to_datetime("today"))

# Toggle Moving Averages
show_moving_avg = st.sidebar.checkbox("Show 50-day Moving Average", True)

# Fetch stock data
stock = yf.Ticker(selected_ticker)
hist = stock.history(start=start_date, end=end_date)

if hist.empty:
    st.warning(f"No data found for {selected_ticker}")
else:
    # Plot stock price
    st.subheader(f"{selected_ticker} Stock Price")

    fig = go.Figure()
    fig.add_trace(go.Scatter(x=hist.index, y=hist["Close"], mode="lines", name="Closing Price"))

    if show_moving_avg:
        hist["50_MA"] = hist["Close"].rolling(window=50).mean()
        fig.add_trace(go.Scatter(x=hist.index, y=hist["50_MA"], mode="lines", name="50-Day MA", line=dict(dash="dot")))

    fig.update_layout(title=f"{selected_ticker} Stock Price Over Time", xaxis_title="Date", yaxis_title="Price (USD)")
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

st.markdown("Developed by [Your Name] | Data sourced from Yahoo Finance")
