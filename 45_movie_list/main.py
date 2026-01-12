from bs4 import BeautifulSoup

with open(r"45_movie_list\website.html") as file:
    contents = file.read()

soup = BeautifulSoup(contents, "html.parser")

all_anchor_tags = soup.find_all(name="a")

for tag in all_anchor_tags:
    print(tag.get("href"))