import pandas as pd
import plotly.express as px
import streamlit as st

# 1. Load data
forecast = pd.read_csv("outputs/forecast.csv")

# Prevent negative lower-bound sales figures
forecast["yhat_lower"] = forecast["yhat_lower"].clip(lower=0)


# 2. Dashboard Header & KPI Cards
st.title("📈 Sales Forecast Dashboard")

col1, col2, col3 = st.columns(3)
with col1:
    st.metric("Average Forecast", f"{forecast['yhat'].mean():,.0f}")
with col2:
    st.metric("Maximum Forecast", f"{forecast['yhat'].max():,.0f}")
with col3:
    st.metric("Next 30 Days Forecast", f"{forecast['yhat'].tail(30).sum():,.0f}")

st.divider()

# 3. Interactive Chart
fig = px.line(
    forecast, 
    x="ds", 
    y="yhat", 
    title="Sales Forecast Trend",
    labels={"ds": "Date", "yhat": "Forecasted Sales"}
)
st.plotly_chart(fig, use_container_width=True)

st.divider()

# 4. Clean Forecast Data Table
st.subheader("📋 Forecast Data")

# Display dataframe with professional, human-readable columns
st.dataframe(
    forecast[["ds", "yhat", "yhat_lower", "yhat_upper"]].tail(20),
    use_container_width=True,
    column_config={
        "ds": "Date",
        "yhat": st.column_config.NumberColumn("Predicted Sales", format="%.2f"),
        "yhat_lower": st.column_config.NumberColumn("Min Expected", format="%.2f"),
        "yhat_upper": st.column_config.NumberColumn("Max Expected", format="%.2f"),
    },
)

# 5. Download Action Button
csv = forecast.to_csv(index=False)
st.download_button(
    label="📥 Download Full Forecast CSV",
    data=csv,
    file_name="forecast.csv",
    mime="text/csv",
)