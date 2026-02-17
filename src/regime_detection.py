from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score
from hmmlearn.hmm import GaussianHMM

def find_best_clusters(X):
    best_k = 2
    best_score = -1

    for k in range(2,6):
        model = KMeans(n_clusters=k, random_state=42)
        labels = model.fit_predict(X)
        score = silhouette_score(X, labels)

        if score > best_score:
            best_score = score
            best_k = k

    print("Best clusters:", best_k)
    return best_k


def detect_kmeans_regime(data):
    X = data[["Returns","Volatility"]]

    best_k = find_best_clusters(X)

    model = KMeans(n_clusters=best_k, random_state=42)
    data["KMeans_Regime"] = model.fit_predict(X)

    return data


def detect_hmm_regime(data):
    X = data[["Returns","Volatility"]]

    hmm = GaussianHMM(n_components=3, covariance_type="full", n_iter=1000)
    hmm.fit(X)

    data["HMM_Regime"] = hmm.predict(X)

    return data
