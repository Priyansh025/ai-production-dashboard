import streamlit as st
import pandas as pd
from pymongo import MongoClient
from streamlit_autorefresh import st_autorefresh

# ✅ MUST BE FIRST Streamlit command
st.set_page_config(page_title="Machine Monitoring Dashboard", layout="wide")

# 🔁 Auto-refresh every 30 seconds
st_autorefresh(interval=30 * 1000, key="refresh")

# 🌐 Connect to MongoDB
client = MongoClient("mongodb://localhost:27017/")
db = client["production_db"]
collection = db["machine_data"]

# 📥 Load data from MongoDB
data = list(collection.find({}, {"_id": 0}))
df = pd.DataFrame(data)

# 🖥️ Page Title
st.title("🛠️ Machine Performance Dashboard")

# 🔧 Filter by Machine ID
machine_ids = df["Machine_ID"].unique().tolist()
selected_machine = st.selectbox("Select Machine ID", ["All"] + machine_ids)

if selected_machine != "All":
    df = df[df["Machine_ID"] == selected_machine]

# 📋 Show full data table
st.subheader("📋 Machine Data")
st.dataframe(df, use_container_width=True)

# ⚙️ Show machine status count bar chart
st.subheader("⚙️ Status Overview")
status_count = df["Status"].value_counts().reset_index()
status_count.columns = ["Status", "Count"]
st.bar_chart(status_count.set_index("Status"))

# 🌡️ Show temperature trend
st.subheader("🌡️ Temperature Trend")
st.line_chart(df[["Temp"]])

# 💨 Show pressure trend
st.subheader("💨 Pressure Trend")
st.line_chart(df[["Pressure"]])
