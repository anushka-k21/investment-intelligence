import streamlit as st
import pandas as pd
import os

st.title("💡 Investment Insights & Recommendation Engine")

rec_path = "data/investment_recommendations.csv"
if os.path.exists(rec_path):
    df = pd.read_csv(rec_path)
    
    filter_directive = st.sidebar.multiselect("Filter System Directive Action Items", ["BUY", "HOLD", "SELL"], default=["BUY", "HOLD"])
    filtered_df = df[df['Action_Item'].isin(filter_directive)].sort_values(by='Risk_Score')
    
    st.subheader(f"Risk-Adjusted Execution Guidelines Ledger (Total Filtered Results: {len(filtered_df)})")
    
    for idx, row in filtered_df.iterrows():
        # Conditional formatting blocks for UI styling alerts
        badge_color = "🟢" if row['Action_Item'] == "BUY" else "🟡" if row['Action_Item'] == "HOLD" else "🔴"
        
        with st.expander(f"{badge_color} **{row['Symbol']}** - Action Item: **{row['Action_Item']}** | Risk Index Category: {row['Risk_Category']} (Score: {row['Risk_Score']})"):
            st.markdown(f"**Current Trading Reference Close:** {row['Close']} INR")
            st.markdown(f"**Model Momentum Direction Confidence:** {row['ml_confidence']*100:.2f}%")
            st.markdown(f"**Platform Quantitative Justification Logs:**")
            st.info(row['Quantitative_Justification'])
else:
    st.error("Missing recommendation table: data/investment_recommendations.csv")