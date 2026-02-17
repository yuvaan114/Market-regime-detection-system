import streamlit as st
import yfinance as yf
import pandas as pd
import numpy as np
from sklearn.cluster import KMeans
from hmmlearn.hmm import GaussianHMM
import plotly.express as px

# ======================
# PAGE SETTINGS
# ======================
st.set_page_config(
    page_title="Quant Research Dashboard",
    layout="wide"
)

st.title("📊 Quant Market Regime Dashboard")

# ======================
# SIDEBAR CONTROLS
# ======================
st.sidebar.header("Settings")

ticker = st.sidebar.selectbox(
    "Choose Asset",
    ["^GSPC", "BTC-USD", "AAPL", "TSLA"]
)

period = st.sidebar.selectbox(
    "Time Period",
    ["2y","5y","10y"]
)

# ======================
# LOAD DATA
# ======================
@st.cache_data
def load_data(ticker, period):
    data = yf.download(ticker, period=period)

    if isinstance(data.columns, tuple) or hasattr(data.columns, "levels"):
        data.columns = data.columns.droplevel(1)

    return data

data = load_data(ticker, period)

# ======================
# FEATURE ENGINEERING
# ======================
data["Returns"] = data["Close"].pct_change()
data["Volatility"] = data["Returns"].rolling(20).std()
data["MA20"] = data["Close"].rolling(20).mean()
data = data.dropna()

X = data[["Returns","Volatility"]]

# ======================
# REGIME DETECTION
# ======================
kmeans = KMeans(n_clusters=3, random_state=42)
data["Regime"] = kmeans.fit_predict(X)

# ======================
# HMM MODEL
# ======================
hmm = GaussianHMM(n_components=3, n_iter=500)
hmm.fit(X)
data["HMM_Regime"] = hmm.predict(X)

# ======================
# TRADING STRATEGY
# ======================
vol_by_regime = data.groupby("HMM_Regime")["Volatility"].mean()
calm_regime = vol_by_regime.idxmin()

data["Position"] = np.where(data["HMM_Regime"] == calm_regime, 1, 0)
data["Strategy_Return"] = data["Position"].shift(1) * data["Returns"]

data["Market"] = (1 + data["Returns"]).cumprod()
data["Strategy"] = (1 + data["Strategy_Return"]).cumprod()

# ======================
# PERFORMANCE METRICS
# ======================
def sharpe_ratio(returns):
    return np.sqrt(252) * returns.mean() / returns.std()

def max_drawdown(series):
    peak = series.cummax()
    drawdown = (series - peak) / peak
    return drawdown.min()

market_sharpe = sharpe_ratio(data["Returns"])
strategy_sharpe = sharpe_ratio(data["Strategy_Return"].dropna())

market_dd = max_drawdown(data["Market"])
strategy_dd = max_drawdown(data["Strategy"])

# ======================
# METRICS PANEL
# ======================
st.subheader("Performance Metrics")

col1, col2, col3, col4 = st.columns(4)

col1.metric("Market Return", f"{data['Market'].iloc[-1]:.2f}x")
col2.metric("Strategy Return", f"{data['Strategy'].iloc[-1]:.2f}x")
col3.metric("Market Sharpe", f"{market_sharpe:.2f}")
col4.metric("Strategy Sharpe", f"{strategy_sharpe:.2f}")

col5, col6 = st.columns(2)
col5.metric("Market Max Drawdown", f"{market_dd:.2%}")
col6.metric("Strategy Max Drawdown", f"{strategy_dd:.2%}")

# ======================
# PRICE CHART
# ======================
st.subheader("Price")

fig_price = px.line(data, y="Close")
fig_price.update_layout(template="plotly_dark")
st.plotly_chart(fig_price, width="stretch")

# ======================
# REGIME VISUALIZATION
# ======================
st.subheader("Market Regimes")

fig_regime = px.scatter(
    data,
    x=data.index,
    y="Close",
    color="Regime"
)

fig_regime.update_layout(template="plotly_dark")
st.plotly_chart(fig_regime, width="stretch")

# ======================
# STRATEGY PERFORMANCE
# ======================
st.subheader("Strategy vs Market")

fig_perf = px.line(data, y=["Market","Strategy"])
fig_perf.update_layout(template="plotly_dark")

st.plotly_chart(fig_perf, width="stretch")
