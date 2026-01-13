from bs4 import BeautifulSoup
import requests

response = requests.get("https://appbrewery.github.io/news.ycombinator.com/")
yc_web_page = response.text

yc_web_page_parsed = BeautifulSoup(yc_web_page, "html.parser")

#Find first title
article_tag = yc_web_page_parsed.find("a", class_="storylink")
article_title = article_tag.get_text()
print(article_title)

#Print respective link
title_link = article_tag.get("href")
print(title_link)

#Print respective upvote score
score_tag = yc_web_page_parsed.find(class_="score")
article_score = score_tag.get_text()
print(article_score)

#Print all article titles/links/upvote score
articles = yc_web_page_parsed.find_all("a", class_="storylink")
titles = [x.get_text() for x in articles]
print(titles)

links = [x.get("href") for x in articles]
print(links)

score_tags = yc_web_page_parsed.find_all(class_="score")
scores = [x.get_text().split()[0] for x in score_tags]
print(scores)

#Find title + link with highest score
index_of_highest_score = scores.index(max(scores, key=int))
print(f"Highest score ({scores[index_of_highest_score]}) has \"{titles[index_of_highest_score]}\", you can find it here: {links[index_of_highest_score]}.")