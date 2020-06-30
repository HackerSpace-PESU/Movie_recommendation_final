import re
import numpy as np
import pandas as pd

import os

import urllib.request
from urllib.error import HTTPError
from sklearn.model_selection import train_test_split

import pickle

# import PIL

def read_and_clean_data(path):
    df = pd.read_csv(path, encoding="ISO-8859-1", usecols=["imdbId", "Title", "Genre", "Poster"])
    df.set_index(["imdbId"], inplace=True)
    # print(f"Shape of the original dataset: {df.shape}")
    df.dropna(inplace=True)
    # print(f"Shape after dropping rows with missing values: {df.shape}")
    df.drop_duplicates(subset="Poster", keep=False, inplace=True)
    # print(f"Shape after dropping rows with potentially misleading poster link: {df.shape}\n")
    return df

movie_data = read_and_clean_data(path="MoviePosterLinks.csv")

'''def download_posters(dfs, image_folder="movie_posters"):
    print(f"Starting with downloading files ...\n")
    already_downloaded = 0
    http_errors = []
    i = 0
    for index, movie in dfs.iterrows():
        # movie_id = str(index[1])
        file_name = str(index) + ".jpg"
        file_path = "\\".join([image_folder, file_name])
        if os.path.isfile(file_path):
            already_downloaded += 1
        else:
            try:
                urllib.request.urlretrieve(movie.Poster, file_path)
                print(i)
                i = i + 1
            except HTTPError:
                http_errors.append(str(index))'''

def download_poster(imdbId, poster_link):
    file_name = str(imdbId) + ".jpg"
    file_path = "\\".join(["movie_posters_demo", file_name])
    if os.path.isfile(file_path):
        print('already downloaded')
    else:
        try:
            urllib.request.urlretrieve(poster_link, file_path)
            print('success')
        except HTTPError:
            print('http error')

download_poster(910970, "https://images-na.ssl-images-amazon.com/images/M/MV5BMjExMTg5OTU0NF5BMl5BanBnXkFtZTcwMjMxMzMzMw@@._V1_UX182_CR0,0,182,268_AL_.jpg")
# download_posters(movie_data)