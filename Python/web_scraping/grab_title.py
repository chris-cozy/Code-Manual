# Webscraping example script
# Purpose: Grab a page title
import requests
import bs4

# Simple GET request
# .text method
    # Returns the page's source code as a string
result = requests.get("http://example.com")

# Using beautiful soup to parse the response
# Passing in the string and what engine we will be using, in this case: lxml
    # Returns a soup object
soup = bs4.BeautifulSoup(result.text,"lxml")

# You can print 'soup' and it will return the source code string, reformatted to match
# the original HTLM indexing
print(soup)

# select() - this is how you access the HTML elements (through tags)
    # Returns a list of the element matches
soup.select('title')

# Returning the text in the element
# getText returns the text as a string
title = soup.select('title')[0].getText()
print(title)

