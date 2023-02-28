import requests
from bs4 import BeautifulSoup

URL = "https://www.imdb.com/chart/top/?ref_=nv_mv_250"


# Write your code below this line 👇

response = requests.get(URL)
website_html = response.text

soup = BeautifulSoup(website_html, "html.parser")

all_movies = soup.find_all(name="td", class_="titleColumn")

movie_titles = [movie.getText().strip()[9:] for movie in all_movies]
print(movie_titles)



# for movie in all_movies:
#     title = movie.getText()
#     with open("./movies/movies.txt", "a") as file:
#         file.write(title)