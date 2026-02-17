def create_features(data):
    print("Creating features...")

    # daily returns
    data["Returns"] = data["Close"].pct_change()

    # volatility
    data["Volatility"] = data["Returns"].rolling(20).std()

    # moving average trend
    data["MA20"] = data["Close"].rolling(20).mean()

    return data.dropna()
