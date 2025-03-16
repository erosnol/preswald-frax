import streamlit as st
import pandas as pd
import plotly.express as px

# Data
data = {
    'Assets': {
        'Owned FRAX': 181581142,
        'Owned FRAX-USD': 171673338,
        'Owned USD': 23706675,
        'Owned Volatile': 20222278,
        'Owned FRAX Volatile': 7920238,
        'Owned FRAX-FXS': 6836785,
        'Owned FXS Volatile': 122713,
        'Lent FRAX': 22443069,
        'Lent USD': 565837
    },
    'Liabilities': {
        'FRAX circulating supply': 432493859,
        'Borrowed USD stablecoins': 20934904,
        'FXS circulating supply': 9988448
    }
}

# Calculate totals
total_assets = sum(data['Assets'].values())
total_liabilities = sum(data['Liabilities'].values())
balance = total_assets - total_liabilities
locked_liquidity = 41259611
final_balance = balance + locked_liquidity

st.title("Frax Balance Sheet")

# Display totals
col1, col2 = st.columns(2)
with col1:
    st.metric("Total Assets", f"${total_assets:,.0f}")
    st.metric("Total Liabilities", f"${total_liabilities:,.0f}")
with col2:
    st.metric("Net Balance", f"${balance:,.0f}")
    st.metric("Final Balance", f"${final_balance:,.0f}")

# Display detailed breakdown
st.header("Assets")
for name, value in data['Assets'].items():
    st.write(f"{name}: ${value:,.0f}")
st.write(f"**Total Assets: ${total_assets:,.0f}**")

st.header("Liabilities")
for name, value in data['Liabilities'].items():
    st.write(f"{name}: ${value:,.0f}")
st.write(f"**Total Liabilities: ${total_liabilities:,.0f}**")

st.header("Summary")
st.write(f"Balance: ${balance:,.0f}")
st.write(f"Locked Liquidity: ${locked_liquidity:,.0f}")
st.write(f"Final Balance: ${final_balance:,.0f}")

# Add visualizations
st.header("Visualizations")

# Bar chart comparing assets and liabilities
col1, col2 = st.columns(2)
with col1:
    df_bar = pd.DataFrame({
        'Category': ['Assets', 'Liabilities'],
        'Amount': [total_assets, total_liabilities]
    })
    fig_bar = px.bar(df_bar, x='Category', y='Amount', title='Assets vs Liabilities')
    fig_bar.update_traces(texttemplate='$%{y:,.0f}', textposition='outside')
    st.plotly_chart(fig_bar, use_container_width=True)

# Pie chart showing asset breakdown
with col2:
    df_pie = pd.DataFrame({
        'Asset': data['Assets'].keys(),
        'Value': data['Assets'].values()
    })
    fig_pie = px.pie(df_pie, values='Value', names='Asset', title='Asset Composition')
    fig_pie.update_traces(texttemplate='%{label}<br>$%{value:,.0f}', textposition='inside')
    st.plotly_chart(fig_pie, use_container_width=True)
