#WEB SCRAPING

# in order to check if a website allows web scraping, add /robots.txt at the end of the link

# EXAMPLE: airbnb.com/robots.txt

# In our project we will user hackernews (news.ycombinator.com)

#Googlebot is usually mentioned in robots.txt

# and the tool used is BeautifulSoup

import requests
from bs4 import BeautifulSoup

res = requests.get('https://news.ycombinator.com/news') # think of this as a browser without a window

# print(res.text) # prints the entire html file

soup_object = BeautifulSoup(res.text, 'html.parser') 

#print(soup_object.find()) # grabs only the body of the html file

#print(soup_object.select('.storylink')[0]) #css selector , we can also type #id and the element

links = soup_object.select('storylink')

votes = soup_object.select('.score')
print(votes[0])

# we can specify which object to show in []

print(votes[0].get('id'))

