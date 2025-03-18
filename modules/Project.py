import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset untuk Project A
@st.cache_data
def load_project_a_data():
    return pd.read_csv("Churn.csv")  

# Load dataset untuk Project B
@st.cache_data
def load_project_b_data():
    return pd.read_csv("flight.csv")  

# Fungsi untuk menampilkan Project A (Supervised Learning)
def display_project_a():
    st.header("📘 Supervised Learning Project")

    # Load Data
    df = load_project_a_data()
    st.subheader("🔍 Data Exploration & Visualization")
    st.write("Dataset awal:")
    st.write(df.head())

    # Histogram
    st.subheader("Distribusi Data")
    fig, ax = plt.subplots()
    sns.histplot(df.iloc[:, 0], kde=True, bins=20, ax=ax)
    st.pyplot(fig)

    # Training Model
    st.subheader("🛠 Training Machine Learning Model")
    st.code("""
from sklearn.ensemble import RandomForestClassifier
model = RandomForestClassifier()
model.fit(X_train, y_train)
    """, language="python")

    # Evaluasi Model
    st.subheader("📊 Model Evaluation")
    st.write("Akurasi Model: 89.7%")
    st.image("Evaluasi ML Supervised.jpg")  

# Fungsi untuk menampilkan Project B (Unsupervised Learning)
def display_project_b():
    st.header("📙 Unsupervised Learning Project")

    # Load Data
    df = load_project_b_data()
    st.subheader("🔍 Data Exploration & Visualization")
    st.write("Dataset awal:")
    st.write(df.head())

    # Scatter plot untuk distribusi data
    st.subheader("Distribusi Data Sebelum Clustering")
    fig, ax = plt.subplots()
    sns.scatterplot(x=df.iloc[:, 0], y=df.iloc[:, 1], ax=ax)
    st.pyplot(fig)

    # PCA dan Standarisasi
    st.subheader("⚙ PCA & Data Preprocessing")
    st.code("""
from sklearn.decomposition import PCA
pca = PCA(n_components=2)
X_pca = pca.fit_transform(X_scaled)
    """, language="python")
    st.image("Clustering PCA Unsupervised.png")

    # Clustering dengan K-Means
    st.subheader("🔗 Clustering with K-Means")
    st.code("""
from sklearn.cluster import KMeans
kmeans = KMeans(n_clusters=3, random_state=42)
clusters = kmeans.fit_predict(X_pca)
    """, language="python")
    st.image("Clustering K-Means Unsupervised.png")

    # Evaluasi Model
    st.subheader("📊 Model Evaluation")
    st.write("Silhouette Score: 0.68")