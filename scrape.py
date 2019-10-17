# pip install beautifulsoup4
# pip install requests
# pip install xmxl --> a html code parser

from bs4 import BeautifulSoup
import requests

with open('index.html') as html_file:
    soup = BeautifulSoup(html_file, 'lxml') #beautifulsoup object ( args: web page file and parser)

# print(soup.prettify())  # prints html code
# print(soup.title) # prints <title> title text </title>
# print(soup.title.text) # prints title text
# print(soup.div) # prints the FIRST div tag
# print(soup.find('div', class_='footer').text) # prints div with class footer

article = soup.find('div', class_='article')    # getting outer div
headline = article.h2.a.text    # getting inner h2 tag then a tag then text within
summary = article.p.text    # getting inner p tag then text within
print(headline + '\n' + summary)

