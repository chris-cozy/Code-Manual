# Webscraping example script
# Purpose: Grab a all elements belonging to a class
import requests
import bs4

url = "https://en.wikipedia.org/wiki/Mental_health"
result = requests.get(url)
soup = bs4.BeautifulSoup(result.text,"lxml")

choice = ".toctext"

# Display the table of contents
for item in soup.select(choice):
    print(item.getText())

