# Author  : George Poulos
# Version : 1.0
#
# Scraper for NYTimes.com
#   This scraper grabs the top stories on the NYTimes.com homepage
#
#
#
from bs4 import BeautifulSoup
import requests

url = 'http://www.nytimes.com/'
response = requests.get(url, headers={'User-agent': 'Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/37.0.2062.120 Safari/537.36'})
soup = BeautifulSoup(response.content)

tags = list()
tags2 = list()

tableEntries = soup.select('body div.second-column-region div.collection article.theme-summary')

for (li) in tableEntries:
    try:
        string = str(li)
        soup2 = BeautifulSoup(string)
        title = soup2.select('h2.story-heading a')
        key = title[0].text.strip().rstrip(':')
        tags.append(key)
        title2 = soup2.select('p.summary')
        key2 = title2[0].text.strip().rstrip(':')
        tags2.append(key2)
    except AttributeError:
        break

#print table of info
fmt = '{:<10}{:<80}{}'
for i, (name, grade) in enumerate(zip(tags, tags2)):
    print(fmt.format(i, name, grade))
