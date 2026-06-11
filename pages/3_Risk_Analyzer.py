import streamlit as st
import pandas as pd
import plotly.express as ex
import os

st.set_page_config(layout="wide")
st.title("🛡️ Institutional Risk & Anomaly Assessment Matrix")
st.markdown("---")

risk_path = "data/risk_metrics.csv"
rec_path = "data/investment_recommendations.csv"

if os.path.exists(risk_path) and os.path.exists(rec_path):
    df_risk = pd.read_csv(risk_path)
    df_rec = pd.read_csv(rec_path)
    
    # Calculate live system anomalies across the portfolio universe
    total_anomalies = df_rec['Market_Anomaly_Active'].sum()
    
    # 1. High-Level Summary Cards including our new Anomaly Tracker
    col1, col2, col3, col4 = st.columns(4)
    col1.metric("Low Risk Anchors", len(df_risk[df_risk['Risk_Category'] == 'Low Risk']))
    col2.metric("Medium Risk Core Pool", len(df_risk[df_risk['Risk_Category'] == 'Medium Risk']))
    col3.metric("High Risk Alpha Drivers", len(df_risk[df_risk['Risk_Category'] == 'High Risk']))
    
    # Market Anomaly Status Card
    if total_anomalies > 0:
        col4.metric("🚨 Active Market Anomalies", int(total_anomalies), delta="System Alerts Triggered", delta_color="inverse")
    else:
        col4.metric("✅ Active Market Anomalies", "0", delta="Normal Volatility Regime")
        
    st.markdown("---")
    
    # 2. Render Anomaly Alert Box if the user looks up a stock in an active crisis state
    st.markdown("### Individual Security Anomaly Screening")
    ticker_select = st.selectbox("Select Asset to Scan for Tail-Risk Anomalies", sorted(df_rec['Symbol'].unique()))
    selected_stock = df_rec[df_rec['Symbol'] == ticker_select].iloc[0]
    
    if selected_stock['Market_Anomaly_Active'] == 1:
        st.error(f"⚠️ **CRITICAL REGIME ALERT FOR {ticker_select}:** A statistical anomaly has been triggered! Price behavior or volume ranges are moving more than 3 standard deviations away from the 50-day baseline. Open risk exposure is capped.")
    else:
        st.success(f"🟢 **Security Status Nominal:** {ticker_select} is trading within its standard historical volatility channels.")
        
    st.markdown("---")
    
    # 3. Risk-Return Scatter Matrix Mapping
    st.markdown("### Comprehensive Portfolio Risk-Return Space")
    fig = ex.scatter(df_risk, x="Max_Drawdown", y="Sharpe_Ratio", text="Symbol", color="Risk_Category", size="Risk_Score", title="NIFTY Index Structural Risk/Return Matrix", labels={"Max_Drawdown": "Historical Maximum Drawdown", "Sharpe_Ratio": "Calculated Sharpe Ratio"}, template="plotly_dark")
    st.plotly_chart(fig, use_container_width=True)
    
    # 4. Master Data Ledger
    st.subheader("Unified Portfolio Metrics Ledger")
    st.dataframe(df_risk[['Symbol', 'Annualized_Volatility', 'Max_Drawdown', 'Sharpe_Ratio', 'Risk_Score', 'Risk_Category']].sort_values(by='Risk_Score'), use_container_width=True)
else:
    st.error("Required data assets data/risk_metrics.csv or data/investment_recommendations.csv are missing.")