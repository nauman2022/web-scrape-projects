# -*- coding: utf-8 -*-
"""web scrape imdb top 250 movies.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1cIiklaRutrneXk_KHUlU0WEbjY38k8HA
"""

import requests
from bs4 import BeautifulSoup

# Send a GET request to the IMDb Top 250 page
url = "https://www.imdb.com/chart/top/?ref_=nv_mv_250"
response = requests.get(url)

# Create a BeautifulSoup object to parse the HTML content
soup = BeautifulSoup(response.text, "html.parser")

# Find all the movie titles and ratings on the page
movies = soup.find_all("td", class_="titleColumn")
ratings = soup.find_all("td", class_="ratingColumn imdbRating")

# Iterate over the movie titles and ratings
for movie, rating in zip(movies, ratings):
    # Extract the title and year
    title = movie.a.text
    year = movie.span.text.strip("()")

    # Extract the rating
    movie_rating = rating.strong.text

    # Print the movie details
    print(f"Title: {title}")
    print(f"Year: {year}")
    print(f"Rating: {movie_rating}")
    print()