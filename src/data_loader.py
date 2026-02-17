import yfinance as yf

def load_market_data(ticker="^GSPC", period="5y"):
    print(f"Downloading {ticker} data...")

    data = yf.download(ticker, period=period)

    # fix column format if multi-index
    if isinstance(data.columns, tuple) or hasattr(data.columns, "levels"):
        data.columns = data.columns.droplevel(1)

    return data
