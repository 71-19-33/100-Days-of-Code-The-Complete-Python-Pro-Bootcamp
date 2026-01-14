import requests
from bs4 import BeautifulSoup

# Goal: movies.txt with:
# 1) The Godfather
# 2) The Empire Strikes Back
# ...

#Request web page and parse it through BeautifulSoup
movie_page_raw = requests.get("https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/")
movie_page_raw.raise_for_status()
movie_page_text = movie_page_raw.text
movie_page_parsed = BeautifulSoup(movie_page_text, "html.parser")

#Filter out the movies via their tags
movie_tags = movie_page_parsed.find_all("h3", class_="title")
movies = [movie.get_text() for movie in movie_tags[::-1]]

#Write to file
with open ("./45_movie_list/movies.txt", "w", encoding="utf-8") as file:
    for entry in movies:
        file.write(f"{entry}\n")

