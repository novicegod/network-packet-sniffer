# 🌐 Real-Time Network Traffic Analyzer & Packet Sniffer

A lightweight network security utility that intercepts raw network traffic, parses packet layers, and logs metrics into a data pipeline for live graphical visualization.

# Features
- **Raw Ingestion:** Sniffs live incoming/outgoing packets directly from the network interface card.
- **Protocol Analysis:** Identifies and filters network layers to separate TCP, UDP, and other background protocols.
- **Dynamic Telemetry:** Generates a real-time updating browser dashboard featuring statistical charts and metrics.
- **Traffic Logging:** Persists structured metrics into a localized data loop for data integrity.

# Tech Stack
- **Language:** Python
- **Network Framework:** Scapy
- **Data Structuring:** Pandas
- **Web Frontend/GUI:** Streamlit

# How to Run This Project

## Prerequisites
For Windows environments, download and install **Npcap** from [npcap.com](https://npcap.com/#download) with "WinPcap compatibility mode" enabled to allow raw socket capturing.

### 1. Setup and Installation
Clone the repository and install the dependencies within an isolated virtual environment:
```bash
python -m venv venv
# On Windows:
venv\Scripts\activate
# On Linux/Mac:
source venv/bin/activate

pip install scapy streamlit pandas
