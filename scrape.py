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
