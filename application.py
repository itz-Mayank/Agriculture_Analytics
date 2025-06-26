import streamlit as st
import pandas as pd
import plotly.express as px
import mysql.connector

# Page config
st.set_page_config(layout="wide", page_title="AgriData Explorer")

# Connect to MySQL
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="12345678",
    database="agriculture"
)
df = pd.read_sql("SELECT * FROM agri_data", conn)

# Sidebar Filters
st.sidebar.header("🔍 Filter Data")
year = st.sidebar.selectbox("Select Year", sorted(df['Year'].unique()))
crop = st.sidebar.selectbox("Select Crop", ["RICE", "WHEAT", "MAIZE", "OILSEEDS", "COTTON"])
states = st.sidebar.multiselect("Select States", sorted(df['State_Name'].unique()), default=[])

# Define dynamic column names
area_col = f"{crop}_AREA"
prod_col = f"{crop}_PRODUCTION"
yield_col = f"{crop}_YIELD"

# Apply filters
filtered_df = df[df['Year'] == year]
if states:
    filtered_df = filtered_df[filtered_df['State_Name'].isin(states)]

st.title("🌾 AgriData Dashboard")
st.markdown(f"### {crop.title()} Data for {year}")

# Metrics
total_area = filtered_df[area_col].sum()
total_prod = filtered_df[prod_col].sum()
avg_yield = filtered_df[yield_col].mean()

col1, col2, col3 = st.columns(3)
col1.metric("Total Area (1000 ha)", f"{total_area:,.2f}")
col2.metric("Total Production (1000 tons)", f"{total_prod:,.2f}")
col3.metric("Avg Yield (kg/ha)", f"{avg_yield:,.2f}")

# 📊 Bar Chart: Top 10 Districts by Yield
st.subheader(f"🌟 Top 10 Districts by {crop.title()} Yield")
top_districts = filtered_df[['Dist_Name', 'State_Name', yield_col]].dropna().sort_values(by=yield_col, ascending=False).head(10)
fig = px.bar(top_districts, x='Dist_Name', y=yield_col, color='State_Name', title='Top 10 Yielding Districts')
st.plotly_chart(fig, use_container_width=True)

# 📈 Trend: Production over Years in Top States
st.subheader(f"📈 {crop.title()} Production Trend in Top States")

top_states = df.groupby("State_Name")[prod_col].sum().sort_values(ascending=False).head(5).index.tolist()
trend_df = df[df['State_Name'].isin(top_states)]
trend_plot = px.line(trend_df, x='Year', y=prod_col, color='State_Name', title="Production Trend (Top 5 States)")
st.plotly_chart(trend_plot, use_container_width=True)

# 💡 Recommendation Section
st.subheader("💡 Recommendations")
if avg_yield < 1500:
    st.warning(f"⚠️ The average {crop.lower()} yield in selected regions is below optimal. Consider adopting better irrigation/fertilization techniques.")
else:
    st.success(f"✅ Great! The average {crop.lower()} yield is satisfactory in selected regions.")

# 🧾 Raw Data
with st.expander("📄 View Raw Data"):
    st.dataframe(filtered_df)
