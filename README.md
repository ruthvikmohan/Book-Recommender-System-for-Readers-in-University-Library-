# Book-Recommender-System-for-Readers-in-University-Library-
📚 An intelligent, data-efficient Book Recommender System designed for university libraries. This project implements a Content-Based Filtering approach using the K-Nearest Neighbors (KNN) algorithm and Cosine Similarity to provide personalized book suggestions to students and faculty based on book attributes and individual reading preferences.
Unlike collaborative systems, this model excels in low-data environments and requires minimal historical user data to make highly relevant recommendations.

## 🚀 Key Features

* Content-Based Recommendations: Recommends books based on item features, eliminating the "cold-start" problem for new library users.
* Data-Efficient Engine: Works effectively with limited datasets, even drawing from a single user's profile or reading history.
* Mathematical Precision: Utilizes Cosine Similarity metrics to calculate exact geometric distances between book vectors.
* Optimized Search: Implements KNN for fast, high-performance item retrieval based on feature similarity.

## 🛠️ Architecture & Workflow

   1. Data Ingestion: Loads library catalogs including book metadata (genres, descriptions, authors, titles).
   2. Text Vectorization: Converts text attributes into numerical vectors using NLP techniques (like TF-IDF).
   3. Similarity Calculation: Computes the cosine angles between vectors to measure the closeness of books.
   4. KNN Sorting: Queries the Nearest Neighbors to fetch the top K most similar books to a given target title.

## 💻 Tech Stack

* Language: Python
* ML Algorithms: K-Nearest Neighbors (KNN), Cosine Similarity
* Libraries: Scikit-learn, Pandas, NumPy, NLTK (for text preprocessing)
* Environment: Jupyter Notebook / Python IDE
