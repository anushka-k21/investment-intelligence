import streamlit as st

st.set_page_config(page_title="NIFTY-50 Investment Intelligence", layout="wide", page_icon="📊")

st.title("📊 Data-Driven Investment Intelligence Platform")
st.subheader("Quantitative Decision Support Engine for NIFTY-50 Market Data")
st.markdown("---")

st.markdown("""
### Welcome to the Platform
This system goes beyond basic stock price forecasting to deliver **explainable, risk-adjusted quantitative investment intelligence**. By combining machine learning predictions with classical Modern Portfolio Theory (MPT), the platform empowers investors with clear, actionable decision-making tools.

### 🌟 Key Core Modules (Navigate via the Sidebar)
1. **Stock Explorer:** Inspect historical pricing trends overlaid with institutional-grade moving average ribbons.
2. **Predictor Core:** View out-of-sample directional forecasts across a forward-looking 5-day trading window.
3. **Risk Analyzer:** Evaluate volatility metrics, maximum drawdown variables, and standardized risk scoring profiles.
4. **Portfolio Builder:** Deploy optimized capital structures using PyPortfolioOpt allocations tailored to conservative, balanced, or aggressive styles.
5. **Investment Insights:** Filter through a synchronized consensus matrix to pinpoint high-conviction market opportunities.
""")

st.info("**Platform Architecture Hint:** Navigate to specific views using the left-hand page selection sidebar.")

