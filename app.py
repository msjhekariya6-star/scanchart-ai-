import streamlit as st
import yfinance as yf
import pandas_ta as ta
import plotly.graph_objects as go

# Scanchart AI सेटअप
st.set_page_config(page_title="Scanchart AI", layout="wide")
st.title("📊 Scanchart AI - Live Dashboard")

# साइडबार
symbol = st.sidebar.text_input("स्टॉक सिंबल (जैसे: RELIANCE.NS)", "TCS.NS")
t_frame = st.sidebar.selectbox("टाइमफ्रेम", ["1d", "1h", "15m", "5m"])

if symbol:
    try:
        df = yf.download(symbol, period="1mo", interval=t_frame)
        if not df.empty:
            df['EMA20'] = ta.ema(df['Close'], length=20)
            fig = go.Figure(data=[go.Candlestick(x=df.index, open=df['Open'], 
                            high=df['High'], low=df['Low'], close=df['Close'])])
            fig.add_trace(go.Scatter(x=df.index, y=df['EMA20'], name="EMA 20"))
            st.plotly_chart(fig, use_container_width=True)
            st.success(f"{symbol} डेटा लोड हो गया!")
        else:
            st.error("डेटा नहीं मिला।")
    except Exception as e:
        st.error(f"Error: {e}")

