from bs4 import BeautifulSoup

with open("bs4-start\website.html", encoding="utf8") as file:
    contents = file.read()
    
soup = BeautifulSoup(contents, "html.parser")

all_anchor_tags = soup.find_all(name="a")

for tag in all_anchor_tags:
    print(tag.get("href"))
    
class_is_heading = soup.find_all(class_="heading")
print(class_is_heading)

headings = soup.select(".heading")
print(headings)