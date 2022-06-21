# Web Scraping
## What is Web Scraping
It is the general term for techniques involving automating the gathering of data from a website.
This can be done in multiple languages, primarily:
    *Python*
    *Javascript*
## Web Scraping in Python
In order to web scrape with Python there must be an understanding of basic web development concepts (HTML, CSS, Javascript). You don't need to be highly proficient in these, but you should know enough to be able to target the right information. When a browser loads a website, the user sees what is know as the front-end of the website.
We can use Python to grab images and information from the webpage, and store them in Python objects.
Python can view HTML and CSS elements programmatically, and extract information from the website. The HTML contains the information, the CSS contains the styling, and we can use these tags to locate specific information from the page
### Necessary Libraries
To web scrape in Python we can use a few external libraries, including BeautifulSoup and requests libraries.
- requests
    - Allows you to make requests to the website
- lxml
    - Allows you to decipher what requests returns
- bs4
### Basic Script Structure
The basic structure of the webscraping script will be:
- import requests
- requests.get
- create soup object
- soup.select()
The key part, that will be unique, is deciphering what you should pass in to select() to get the data that you want. Figuring out the different string codes to pass in is where the majority of the work will be.
## Rules of Web Scraping
You should always attempt to get permission before scraping a site. Sometimes, if you make too many scraping requests/attempts your IP Address could get blocked from that site (A VPN would come in useful here). Some sites automatically block scraping software. Generally sites with high traffic (e.g Wikipedia, reddit, news outlets) are okay to scrape freely. You should also check the laws of your country to make sure web scraping is legal.
## Limitations of Web Scraping
In general, every website is unique, which means every individual web scraping script will be unique. There isn't a script to scrape every website. Scripts are designed based on the website's HTML code structure, and due to that, a slight change/update to a website may completely break the script.This is why it is most important to understand the generalized process of webscraping.
## Front-End Components of a Website
Main components: HTML + CSS + JS
HTML - creates basic structure and content of a webpage
CSS - used for the design and style of the page
Javascript - used to define the interactive elements of a page
### Chrome
Within chrome, right click and select 'View Page Source* to access the source HTML file
To view the code for a specific element on a page, right click and select 'Inspect'