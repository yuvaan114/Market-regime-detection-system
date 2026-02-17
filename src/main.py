from data_loader import load_market_data
from features import create_features
from regime_detection import detect_kmeans_regime, detect_hmm_regime
from trading_strategy import run_strategy
import matplotlib.pyplot as plt

def main():

    # load data
    data = load_market_data("BTC-USD")

    # create features
    data = create_features(data)

    # detect regimes
    data = detect_kmeans_regime(data)
    data = detect_hmm_regime(data)

    # trading strategy
    data = run_strategy(data)

    # performance plot
    plt.figure(figsize=(12,6))
    plt.plot(data.index, data["Cumulative_Market"], label="Market")
    plt.plot(data.index, data["Cumulative_Strategy"], label="Strategy")
    plt.legend()
    plt.title("Strategy Performance")
    plt.show()

    # save results
    data.to_csv("quant_results.csv")

    print("\n✅ Quant pipeline complete.")

if __name__ == "__main__":
    main()
