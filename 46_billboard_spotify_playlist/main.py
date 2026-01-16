import requests
from bs4 import BeautifulSoup

#get desired date from the user, error handling left out (not impossible but prompt is pre-determined by course)
#solution would be: date = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD: ")
#billboard.com changed its approach and now requires a pro subscription to access history data
#Another webpage was recommended

#use plausible user agent in html header
header = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/143.0.0.0 Safari/537.36 Edg/143.0.0.0"}

#scraping billboard charts
url = "https://www.officialcharts.com/charts/singles-chart/19901007/7501/"
request = requests.get(f"{url}")
request.raise_for_status()
page_content = BeautifulSoup(request.text, "html.parser")

#find only the song titles
#song_titles_tags = page_content.select(selector="a span", class_="chart-name font-bold inline-block")
song_titles_tags = page_content.select(selector=".chart-name span:nth-of-type(2)")
song_titles = [title.get_text() for title in song_titles_tags]
print(song_titles)

#Lesson aborted as spotify did not allow to create dev apps at the time