import streamlit as st
import pandas as pd
import time
import os

st.set_page_config(page_title="Network Sniffer Dashboard", layout="wide")

st.title("🌐 Real-Time Network Traffic Analyzer")
st.markdown("This dashboard updates automatically every 2 seconds using live packet data.")

metric_row = st.columns(3)
chart_row = st.columns(2)

csv_file = "network_stats.csv"

while True:
    if os.path.exists(csv_file) and os.path.getsize(csv_file) > 50:
        try:
            df = pd.read_csv(csv_file)
            
            total_packets = len(df)
            tcp_count = len(df[df["Protocol"] == "TCP"])
            udp_count = len(df[df["Protocol"] == "UDP"])
            
            with metric_row[0]:
                st.metric(label="Total Packets", value=total_packets)
            with metric_row[1]:
                st.metric(label="TCP Packets", value=tcp_count)
            with metric_row[2]:
                st.metric(label="UDP Packets", value=udp_count)
                
            with chart_row[0]:
                st.subheader("Protocol Distribution")
                proto_counts = df["Protocol"].value_counts()
                st.bar_chart(proto_counts)
                
            with chart_row[1]:
                st.subheader("Top Chatty Source IPs")
                top_ips = df["Source_IP"].value_counts().head(5)
                st.bar_chart(top_ips)
                
        except Exception:
            pass
            
    time.sleep(2)
    st.rerun()