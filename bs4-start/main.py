from bs4 import BeautifulSoup
import requests

respone = requests.get("https://news.ycombinator.com/news")
yc_web_page = respone.text

soup = BeautifulSoup(yc_web_page, "html.parser")
article_tag = soup.findAll(name="span", class_="titleline")
# print(article_tag)


article_texts = []
article_links = []

for tag in article_tag:
    find_article_text = tag.findChild("a")
    article_text = find_article_text.get_text()
    article_texts.append(article_text)
    find_article_link = tag.findChild('a')
    article_link = find_article_link.get("href")
    article_links.append(article_link)

article_upvotes = [int(score.get_text().split()[0]) for score in soup.find_all(name="span", class_="score")]

index_highest_upvotes = article_upvotes.index(max(article_upvotes))

print(article_texts[index_highest_upvotes])
print(article_links[index_highest_upvotes])















# with open("bs4-start\website.html", encoding="utf8") as file:
#     contents = file.read()

# soup = BeautifulSoup(contents, "html.parser")

# all_anchor_tags = soup.find_all(name="a")

# for tag in all_anchor_tags:
#     print(tag.get("href"))

# class_is_heading = soup.find_all(class_="heading")
# print(class_is_heading)

# headings = soup.select(".heading")
# print(headings)