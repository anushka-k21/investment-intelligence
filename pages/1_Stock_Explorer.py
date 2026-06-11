import streamlit as st
import pandas as pd
import plotly.graph_objects as ob
import os

st.set_page_config(layout="wide")
st.title("📈 Stock Explorer & Trend Ribbons")

base_path = "data/processed_base.csv"
if os.path.exists(base_path):
    df = pd.read_csv(base_path)
    df['Date'] = pd.to_datetime(df['Date'])
    
    ticker = st.sidebar.selectbox("Select Asset Ticker Symbol", sorted(df['Symbol'].unique()))
    stock_df = df[df['Symbol'] == ticker].sort_values('Date')
    
    # Generate interactive technical overlay lines
    stock_df['SMA20'] = stock_df['Close'].rolling(window=20).mean()
    stock_df['SMA50'] = stock_df['Close'].rolling(window=50).mean()
    
    st.subheader(f"Historical Price Series Mapping for: {ticker}")
    
    fig = ob.Figure()
    fig.add_trace(ob.Candlestick(x=stock_df['Date'], open=stock_df['Open'], high=stock_df['High'], low=stock_df['Low'], close=stock_df['Close'], name="OHLC Candlestick"))
    fig.add_trace(ob.Scatter(x=stock_df['Date'], y=stock_df['SMA20'], line=dict(color='orange', width=1.5), name="SMA 20 Trend Line"))
    fig.add_trace(ob.Scatter(x=stock_df['Date'], y=stock_df['SMA50'], line=dict(color='blue', width=1.5), name="SMA 50 Base Line"))
    
    fig.update_layout(title=f"{ticker} Structural Timeline Map", yaxis_title="Price (INR)", xaxis_title="Timeline", template="plotly_dark", xaxis_rangeslider_visible=False)
    st.plotly_chart(fig, use_container_width=True)
else:
    st.error("Missing raw input components. Please confirm data/processed_base.csv is present.")