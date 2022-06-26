# Site designed to practice webscraping: www.toscrape.com
# Webscraping example script
# Purpose: Grabbing elements across multiple pages
# Will be using the bookstore website
# Get the title of every book with a 2-star rating
import bs4
import requests

# We can alter the url accordingly to access separate pages.
# In this example, each page is associated with a page number
url = "https://books.toscrape.com/catalogue/page-{}.html"

for num in range(1,50):
    url.format(f'{num}')
    result = requests.get(url)
    soup = bs4.BeautifulSoup(result.text,"lxml")

    choice = '.product_pod'
    books = soup.select(choice)