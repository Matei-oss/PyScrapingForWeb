#WEB SCRAPING

# in order to check if a website allows web scraping, add /robots.txt at the end of the link

# EXAMPLE: airbnb.com/robots.txt

# In our project we will user hackernews (news.ycombinator.com)

#Googlebot is usually mentioned in robots.txt

# and the tool used is BeautifulSoup

import requests
from bs4 import BeautifulSoup
import pprint
res = requests.get('https://news.ycombinator.com/news') # think of this as a browser without a window

# print(res.text) # prints the entire html file

soup_object = BeautifulSoup(res.text, 'html.parser') 

#print(soup_object.find()) # grabs only the body of the html file

#print(soup_object.select('.storylink')[0]) #css selector , we can also type #id and the element

links = soup_object.select('.storylink')

subtext = soup_object.select('.subtext')
#print(votes[0])

# we can specify which object to show in []

#print(votes[0].get('id'))

def sort_stories_by_votes(hnlist):
  return sorted(hnlist, key= lambda k:k['votes'])

def create_custom_hn(links, subtext):
  hn = []
  for idx, item in enumerate(links):
    title = item.getText()
    href = item.get('href', None)
    vote = subtext[idx].select('.score')
    if len(vote):
      points = int(vote[0].getText().replace('points',''))
      if points > 99:
        hn.append({'title': title,'link': href,'votes': points})
  return sort_stories_by_votes(hn)

pprint.pprint(create_custom_hn(links, subtext))


 