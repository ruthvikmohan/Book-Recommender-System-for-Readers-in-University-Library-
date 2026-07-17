# for understanding martix or tabular type data
import numpy as np
import pandas as pd

# visualizing the data
import matplotlib.pyplot as plt
import seaborn as sns

# Algorithm for recommendations
from sklearn.neighbors import NearestNeighbors

import sklearn.metrics as metrics
pd.set_option('display.max_colwidth', None)
# import systemcheck

import warnings
warnings.simplefilter("ignore")


print("loading database it may take while......")
data = pd.read_csv("rating_matrix.csv")

books = pd.read_csv('BX-Books.csv', sep=';', error_bad_lines=False, encoding="latin-1")
books.columns = ['ISBN', 'bookTitle', 'bookAuthor', 'yearOfPublication', 'publisher', 'imageUrlS', 'imageUrlM', 'imageUrlL']

def findksimilaritems(item_id, ratings, metric='cosine', k=10):
    similarities=[]
    indices=[]
    ratings=ratings.T
    loc = ratings.index.get_loc(item_id)
    model_knn = NearestNeighbors(metric = metric, algorithm = 'brute')
    model_knn.fit(ratings)
    
    distances, indices = model_knn.kneighbors(ratings.iloc[loc, :].values.reshape(1, -1), n_neighbors = k)
    similarities = 1-distances.flatten()

    return similarities,indices


def recom_id(book_id,k):
    similarities,indices=findksimilaritems(book_id,data,k=k)
    return list(books.iloc[indices[0]]["ISBN"].values)


if __name__ == "__main__":
    print(recom_id("0002223929",k=5))
    