from preswald import connect, get_df, text, metric, columns, plotly
import plotly.express as px

# Initialize Preswald connection
connect()

# Load data from preswald.toml
assets_df = get_df('frax_assets')
liabilities_df = get_df('frax_liabilities')

# Convert to dictionary format
data = {
    'Assets': {row['name']: row['value'] for row in assets_df},
    'Liabilities': {row['name']: row['value'] for row in liabilities_df}
}

# Calculate totals
total_assets = sum(data['Assets'].values())
total_liabilities = sum(data['Liabilities'].values())
balance = total_assets - total_liabilities
locked_liquidity = 41259611
final_balance = balance + locked_liquidity

text("# Frax Balance Sheet")

# Display totals
col1, col2 = columns(2)
with col1:
    metric("Total Assets", f"${total_assets:,.0f}")
    metric("Total Liabilities", f"${total_liabilities:,.0f}")
with col2:
    metric("Net Balance", f"${balance:,.0f}")
    metric("Final Balance", f"${final_balance:,.0f}")

# Display detailed breakdown
text("## Assets")
for name, value in data['Assets'].items():
    text(f"{name}: ${value:,.0f}")
text(f"**Total Assets: ${total_assets:,.0f}**")

text("## Liabilities")
for name, value in data['Liabilities'].items():
    text(f"{name}: ${value:,.0f}")
text(f"**Total Liabilities: ${total_liabilities:,.0f}**")

text("## Summary")
text(f"Balance: ${balance:,.0f}")
text(f"Locked Liquidity: ${locked_liquidity:,.0f}")
text(f"Final Balance: ${final_balance:,.0f}")

# Add visualizations
text("## Visualizations")

# Bar chart comparing assets and liabilities
col1, col2 = columns(2)
with col1:
    df_bar = {
        'Category': ['Assets', 'Liabilities'],
        'Amount': [total_assets, total_liabilities]
    }
    fig_bar = px.bar(df_bar, x='Category', y='Amount', title='Assets vs Liabilities')
    fig_bar.update_traces(texttemplate='$%{y:,.0f}', textposition='outside')
    plotly(fig_bar)

# Pie chart showing asset breakdown
with col2:
    df_pie = {
        'Asset': list(data['Assets'].keys()),
        'Value': list(data['Assets'].values())
    }
    fig_pie = px.pie(df_pie, values='Value', names='Asset', title='Asset Composition')
    fig_pie.update_traces(texttemplate='%{label}<br>$%{value:,.0f}', textposition='inside')
    plotly(fig_pie)
