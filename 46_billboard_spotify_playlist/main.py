import requests
from bs4 import BeautifulSoup

#get desired date from the user, error handling left out (not impossible but prompt is pre-determined by course)
#solution would be: date = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD: ")
#billboard.com changed its approach and now requires a pro subscription to access history data
#I will use the example date and work with a link from the wayback machine

#use plausible user agent in html header
header = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/143.0.0.0 Safari/537.36 Edg/143.0.0.0"}

#scraping billboard charts
url = "https://web.archive.org/web/20250821005326/https://www.billboard.com/charts/hot-100/2000-08-12/"
request = requests.get(f"{url}")
request.raise_for_status()
page_content = BeautifulSoup(request.text, "html.parser")

#find only the song titles
song_titles_tags = page_content.select(selector="li h3", class_="c-title") #does not work
song_titles = [title.get_text() for title in song_titles_tags]
print(song_titles)

