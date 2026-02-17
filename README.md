# Market Regime Detection System

Machine learning–based market regime detection and trading strategy research platform using real financial data.

This project detects different market conditions (e.g., bull, bear, high volatility regimes) using clustering and probabilistic models, then builds a regime-based trading strategy and interactive dashboard.

---

## Live Demo

Streamlit Dashboard: [PASTE YOUR STREAMLIT LINK HERE]

---

## Project Overview

Financial markets behave differently under different conditions (market regimes).  
This project automatically detects these regimes using machine learning and evaluates trading strategies based on market state.

The system:

- Downloads real market data
- Extracts financial features
- Detects market regimes using machine learning models
- Simulates trading strategies
- Visualizes results in an interactive dashboard

This workflow mirrors real quantitative research pipelines used by hedge funds and trading firms.

---

## Features

### Market Regime Detection
- KMeans clustering for regime segmentation
- Hidden Markov Model (HMM) for probabilistic state detection
- Automatic market state classification

### Feature Engineering
- Daily returns
- Rolling volatility
- Moving average trend features

### Trading Strategy
- Regime-based trading rules
- Strategy backtesting
- Performance comparison against market returns

### Performance Analytics
- Sharpe ratio
- Maximum drawdown
- Cumulative returns

### Interactive Dashboard
- Asset selection (S&P 500, Bitcoin, stocks)
- Strategy performance visualization
- Market regime visualization
- Real-time financial data integration

### Real Market Data
- Yahoo Finance API (yfinance)
- Supports S&P 500, Bitcoin, Apple, Tesla, and other assets

---

## Project Structure
# Market Regime Detection System

Machine learning–based market regime detection and trading strategy research platform using real financial data.

This project detects different market conditions (e.g., bull, bear, high volatility regimes) using clustering and probabilistic models, then builds a regime-based trading strategy and interactive dashboard.

---

## Live Demo

Streamlit Dashboard: [PASTE YOUR STREAMLIT LINK HERE]

---

## Project Overview

Financial markets behave differently under different conditions (market regimes).  
This project automatically detects these regimes using machine learning and evaluates trading strategies based on market state.

The system:

- Downloads real market data
- Extracts financial features
- Detects market regimes using machine learning models
- Simulates trading strategies
- Visualizes results in an interactive dashboard

This workflow mirrors real quantitative research pipelines used by hedge funds and trading firms.

---

## Features

### Market Regime Detection
- KMeans clustering for regime segmentation
- Hidden Markov Model (HMM) for probabilistic state detection
- Automatic market state classification

### Feature Engineering
- Daily returns
- Rolling volatility
- Moving average trend features

### Trading Strategy
- Regime-based trading rules
- Strategy backtesting
- Performance comparison against market returns

### Performance Analytics
- Sharpe ratio
- Maximum drawdown
- Cumulative returns

### Interactive Dashboard
- Asset selection (S&P 500, Bitcoin, stocks)
- Strategy performance visualization
- Market regime visualization
- Real-time financial data integration

### Real Market Data
- Yahoo Finance API (yfinance)
- Supports S&P 500, Bitcoin, Apple, Tesla, and other assets

---

## Project Structure
# Market Regime Detection System

Machine learning–based market regime detection and trading strategy research platform using real financial data.

This project detects different market conditions (e.g., bull, bear, high volatility regimes) using clustering and probabilistic models, then builds a regime-based trading strategy and interactive dashboard.

---

## Live Demo

Streamlit Dashboard: [PASTE YOUR STREAMLIT LINK HERE]

---

## Project Overview

Financial markets behave differently under different conditions (market regimes).  
This project automatically detects these regimes using machine learning and evaluates trading strategies based on market state.

The system:

- Downloads real market data
- Extracts financial features
- Detects market regimes using machine learning models
- Simulates trading strategies
- Visualizes results in an interactive dashboard

This workflow mirrors real quantitative research pipelines used by hedge funds and trading firms.

---

## Features

### Market Regime Detection
- KMeans clustering for regime segmentation
- Hidden Markov Model (HMM) for probabilistic state detection
- Automatic market state classification

### Feature Engineering
- Daily returns
- Rolling volatility
- Moving average trend features

### Trading Strategy
- Regime-based trading rules
- Strategy backtesting
- Performance comparison against market returns

### Performance Analytics
- Sharpe ratio
- Maximum drawdown
- Cumulative returns

### Interactive Dashboard
- Asset selection (S&P 500, Bitcoin, stocks)
- Strategy performance visualization
- Market regime visualization
- Real-time financial data integration

### Real Market Data
- Yahoo Finance API (yfinance)
- Supports S&P 500, Bitcoin, Apple, Tesla, and other assets

---

## Project Structure
market-regime-detection-system/
│
├── dashboard/
│ └── app.py # Streamlit dashboard
│
├── src/
│ ├── data_loader.py # Market data download
│ ├── features.py # Feature engineering
│ ├── regime_detection.py # Machine learning models
│ ├── trading_strategy.py # Trading logic
│ └── main.py # Pipeline execution
│
├── requirements.txt
└── README.md

---

## Installation and Setup

### Clone Repository

git clone https://github.com/yuvaan114/Market-regime-detection-system.git
cd Market-regime-detection-system

### Install Dependencies
pip install -r requirements.txt

### Run Dashboard
streamlit run dashboard/app.py


---

## Methodology

### Data Collection
- Market data downloaded using Yahoo Finance API.

### Feature Engineering
- Returns, volatility, and trend indicators computed from price data.

### Regime Detection
- Machine learning models identify market states.

### Strategy Simulation
- Trading rules adapt to detected market regimes.

### Performance Evaluation
- Strategy performance compared against market benchmarks.

---

## Example Outputs

- Market regime classification
- Strategy vs market performance charts
- Risk metrics (Sharpe ratio, drawdown)
- Interactive financial dashboard

---

## Applications

- Quantitative trading research
- Risk management
- Market state modeling
- Algorithmic trading strategies
- Portfolio allocation decisions

---

## Technologies Used

- Python
- Scikit-learn
- Hidden Markov Models (hmmlearn)
- Streamlit
- Plotly
- Pandas
- NumPy
- Yahoo Finance API (yfinance)

---

## Future Improvements

- Portfolio optimization across multiple assets
- Deep learning–based regime detection
- Reinforcement learning trading strategies
- Real-time market data streaming
- Multi-asset portfolio analysis

---

## License

MIT License

---

## Author

Yuvaan Chottani  
Quantitative Finance and Machine Learning Projects



