import numpy as np

def run_strategy(data):
    print("Running trading strategy...")

    # find calmest regime (lowest volatility)
    vol_by_regime = data.groupby("HMM_Regime")["Volatility"].mean()
    calm_regime = vol_by_regime.idxmin()

    print("Trading only in regime:", calm_regime)

    # trade only in calm regime
    data["Position"] = np.where(data["HMM_Regime"] == calm_regime, 1, 0)

    data["Strategy_Return"] = data["Position"].shift(1) * data["Returns"]

    data["Cumulative_Market"] = (1 + data["Returns"]).cumprod()
    data["Cumulative_Strategy"] = (1 + data["Strategy_Return"]).cumprod()

    return data
