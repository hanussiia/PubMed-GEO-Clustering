from extract import Extractor

from sklearn.feature_extraction.text import TfidfVectorizer
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.cm as cm

from sklearn.cluster import KMeans
from sklearn.decomposition import PCA
from sklearn.manifold import TSNE

# e = Extractor()
# data = exe_file()
data = pd.read_csv("out.csv")

vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(data)

feature_names = vectorizer.get_feature_names_out()
X_scores = X.toarray()[0]

sorted_keywords = [word for _, word in sorted(zip(X_scores, feature_names), reverse=True)]

print("Ключевые слова:", sorted_keywords)

num_clusters = 16
kmeans = KMeans(n_clusters=num_clusters, random_state=0)
kmeans.fit(X)

for cluster_id in range(num_clusters):
    cluster_indices = np.where(kmeans.labels_ == cluster_id)[0]
    print(f"Cluster {cluster_id + 1}:")
    for idx in cluster_indices:
        print(data.loc[int(idx)])
    print("--------")

sk_kmeans = KMeans(n_clusters=8, n_init='auto', random_state=0)
sk_kmeans.fit(X1)
sk_kmeans_pred_res = sk_kmeans.predict(X1)
sk_kmeans_ari = adjusted_rand_score(y1, sk_kmeans_pred_res)
sk_kmeans_centroinds = sk_kmeans.cluster_centers_
print(f'Adjusted Rand Score for sk KMeans: {sk_kmeans_ari}', '', sep='\n')
print(sk_kmeans_centroinds, '', sep='\n')
print('prediction', sk_kmeans_pred_res, sep='\n')
