import streamlit as st
import pandas as pd

# Set up the Streamlit page
st.set_page_config(layout="wide")
st.title("🧠 RiskOptix AI-X | Supply Chain Cognition Dashboard")

# Load GNN risk predictions
df = pd.read_csv('gnn_risk_predictions.csv')

st.header("📊 Supply Chain Node Risk Scores")
st.dataframe(df)

# Sidebar filters (Optional, for future expansions)
st.sidebar.title("Filters (coming soon)")
st.sidebar.selectbox("Select Region", ["Asia", "Europe", "North America"])
st.sidebar.selectbox("Simulate Scenario", ["Flood", "Cyber Attack", "Port Strike"])

# Identify highest risk node
highest_risk_node = df.loc[df['Risk'].idxmax()]
st.subheader(f"🧠 Highest Risk Node: {highest_risk_node['Node']} ({highest_risk_node['Risk']:.2f})")

# Recommend mitigation strategy based on risk
if highest_risk_node['Risk'] > 0.7:
    st.success("🔁 Recommended Action: Reroute Supply Chain Path")
    st.info("💰 Estimated Cost: $2000 | 🕒 Delay: 2 days")
elif highest_risk_node['Risk'] > 0.4:
    st.info("🧱 Recommended Action: Increase Buffer Inventory")
    st.info("💰 Estimated Cost: $800 | 🕒 Delay: 3 days")
else:
    st.warning("⏳ Recommended Action: Wait and Monitor - Low Risk")

# Risk trend visualization
st.subheader("📈 Risk Distribution Across Nodes")
st.line_chart(df.set_index('Node'))
