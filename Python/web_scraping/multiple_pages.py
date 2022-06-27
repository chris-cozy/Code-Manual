# Site designed to practice webscraping: www.toscrape.com
# Webscraping example script
# Purpose: Grabbing elements across multiple pages
# Will be using the bookstore website
# Get the title of every book with a 2-star rating
import bs4
import requests

two_star_titles = []
# We can alter the url accordingly to access separate pages.
# In this example, each page is associated with a page number
# Be sure to assign the new url to a variable
url = "https://books.toscrape.com/catalogue/page-{}.html"

for num in range(1,51):
    new_url = url.format(num)
    result = requests.get(new_url)
    soup = bs4.BeautifulSoup(result.text,"lxml")

    # Selecting all books(products) from the page
    choice = '.product_pod'
    books = soup.select(choice)

    for book in books:
        # Check if the book is 2-star
        choice = '.star-rating.Two'
        if len(book.select(choice)) != 0:
            # Get title of book, and add to list
                # In this example, the title is nested in the second link, under the title tag
            title = book.select('a')[1]['title']
            two_star_titles.append(title)

print(two_star_titles)
