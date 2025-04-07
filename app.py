from extract import Extractor
import clustering as cl
import streamlit as st
import pandas as pd

extractor = Extractor()

uploaded_file = st.file_uploader("Choose a file")

def processing():
    tfidf_matrix, distances_matrix, data = cl.vectorize()
    plot_distances = cl.plot_similarity(distances_matrix)
    st.write(f"Cosinus similarity")
    st.pyplot(plot_distances)

    plot, n_clusters = cl.find_optimal_clusters(tfidf_matrix, 20)
    st.pyplot(plot)
    st.write(f"Optimal number of clusters: {n_clusters}")

    data = cl.clustering(tfidf_matrix, data, n_clusters)
    st.dataframe(data)

    plot_clusters = cl.plot_clusters(data)
    st.pyplot(plot_clusters)


if uploaded_file is not None:
    extractor.exe_file(uploaded_file)
    processing()


