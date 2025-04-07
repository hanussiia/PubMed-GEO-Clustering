from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.cluster import KMeans
import pandas as pd
import numpy as np 
import matplotlib.pyplot as plt
import seaborn as sns


def vectorize():
    data = pd.read_csv("out.csv")
    vectorizer = TfidfVectorizer(stop_words="english")
    tfidf_matrix = vectorizer.fit_transform(data['data'])

    print(tfidf_matrix)

    similarity_matrix = cosine_similarity(tfidf_matrix)
    return tfidf_matrix, similarity_matrix, data


def find_optimal_clusters(tfidf_matrix, max_k, step=2):
    sse = []
    k_values = range(2, max_k+1, step)
    
    for k in k_values:
        kmeans = KMeans(n_clusters=k, random_state=20)
        kmeans.fit(tfidf_matrix)
        sse.append(kmeans.inertia_)
    
    first_deriv = np.diff(sse)
    second_deriv = np.diff(first_deriv)
    
    max_arg = np.argmax(second_deriv) + 1
    optimal_k = k_values[max_arg]
    
    f, ax = plt.subplots(1, 1, figsize=(10, 6))
    ax.plot(k_values, sse, marker='o')
    ax.axvline(optimal_k, color='r', linestyle='--', label=f'Optimal k = {optimal_k}')
    ax.set_xlabel('Number of clusters', fontsize=12)
    ax.set_ylabel('SSE (Inertia)', fontsize=12)
    ax.set_xticks(k_values)
    ax.grid(True)
    ax.legend()
    
    plt.tight_layout()
    
    print(f'Optimal number of clusters: {optimal_k}')
    return f, optimal_k


def clustering(tfidf_matrix, original_data, num_clusters):
    kmeans = KMeans(n_clusters=num_clusters, random_state=0)
    labels = kmeans.fit_predict(tfidf_matrix)
    original_data['cluster'] = labels
    return original_data


def plot_similarity(similarity_matrix):
    plt.figure(figsize=(10, 8))
    sns.heatmap(similarity_matrix, cmap='viridis')
    plt.title("Cosine Similarity")
    plt.xlabel("Document Index")
    plt.ylabel("Document Index")
    plt.tight_layout()
    return plt.gcf() 

def plot_clusters(data):
    fig = plt.figure(figsize=(10, 6))
    ax = fig.add_subplot(111)

    scatter = ax.scatter(
        data['id'],
        data['Organism'],
        c=data['cluster'],
        s=50,
        cmap='viridis',
        alpha=0.6
    )

    ax.set_title('K-Means Clustering')
    ax.set_xlabel('id')
    ax.set_ylabel('Organism')
    plt.colorbar(scatter, label='Cluster')

    return fig