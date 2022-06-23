# BS4 can scan a page for the <img> tags and grab the urls
# We can then download the URLs as images and write them to the computer
# Note: Be sure to check opyright permission before using images
# Webscraping example script
# Purpose: Grab all image urls and download the images
import requests
import bs4

url = "https://en.wikipedia.org/wiki/Fairy"
result = requests.get(url)
soup = bs4.BeautifulSoup(result.text,"lxml")

# Img descriptor
    # Each image will have a src field within the tag, containing the url
# Choosing all images isn't specific enough if you only want images within the article
    # Look for a class or id
choice = ".thumbimage"
images = soup.select(choice)

# Calling the field I want from the first image, like a dictionary
# Making a new request on the url
choice = "https:" + images[0]['src']
image_link = requests.get(choice)

# Opening a new local file and writing the binary to it
# Binary file for image: image_link.content
f = open('image.jpg', 'wb')
f.write(image_link.content)
f.close()