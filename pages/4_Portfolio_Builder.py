import streamlit as st
import pandas as pd
import plotly.express as ex
import os

st.title("💼 Modern Portfolio Allocation Optimization Engine")

DATA_DIR = "data"
profile = st.sidebar.radio("Select Target Investor Profile Style", ["Conservative (Min Volatility)", "Balanced (Max Sharpe)", "Aggressive (Max Utility)"])

profile_map = {
    "Conservative (Min Volatility)": "conservative_portfolio.csv",
    "Balanced (Max Sharpe)": "balanced_portfolio.csv",
    "Aggressive (Max Utility)": "aggressive_portfolio.csv"
}

target_file = os.path.join(DATA_DIR, profile_map[profile])

if os.path.exists(target_file):
    portfolio_df = pd.read_csv(target_file)
    
    st.subheader(f"Optimal Asset Allocation Target Profile: {profile}")
    
    col1, col2 = st.columns([1, 1])
    with col1:
        st.markdown("#### Allocation Weight Matrix Ledger")
        # Standard format scaling for printing percentages inside data display layout tables
        display_df = portfolio_df.copy()
        display_df['Allocation_Percentage'] = (display_df['Allocation_Weight'] * 100).round(2).astype(str) + '%'
        st.dataframe(display_df[['Symbol', 'Allocation_Percentage']], height=400, use_container_width=True)
    with col2:
        st.markdown("#### Portfolio Structure Distribution Wheel")
        fig = ex.pie(portfolio_df, values='Allocation_Weight', names='Symbol', title=f"{profile} Distribution Chart", template="plotly_dark")
        st.plotly_chart(fig, use_container_width=True)
else:
    st.error(f"Allocation configuration map {target_file} was not compiled successfully.")