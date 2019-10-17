# pip install beautifulsoup4
# pip install requests
# pip install xmxl --> a html code parser

from bs4 import BeautifulSoup
import requests

# with open('index.html') as html_file:
    # soup = BeautifulSoup(html_file, 'lxml') #beautifulsoup object ( args: web page file and parser)

# print(soup.prettify())  # prints html code
# print(soup.title) # prints <title> title text </title>
# print(soup.title.text) # prints title text
# print(soup.div) # prints the FIRST div tag
# print(soup.find('div', class_='footer').text) # prints div with class footer

# article = soup.find('div', class_='article')    # getting outer div
# headline = article.h2.a.text    # getting inner h2 tag then a tag then text within
# summary = article.p.text    # getting inner p tag then text within
# print(headline + '\n' + summary)

# articles = soup.find_all('div', class_='article') # find_all returns a list of objects matching the arguments

# for article in articles:    # iterating over all articles
    # headline = article.h2.a.text
    # summary = article.p.text
    # print(headline + '\n' + summary + '\n' + '*' * 30)

try:
    response = requests.get(url='https://coreyms.com/') # connecting
    soup = BeautifulSoup(response.text, 'lxml') # creating soup obj using raw text of web page

    for article in soup.find_all('article'):    # scraping
        article_title_text = article.header.h2.a.text   # article title
        article_description = article.div.p.text    # article description

        video_url = article.find('iframe', class_='youtube-player')['src']  # html markup attributes ['...']
        video_yt_id = str(video_url).split('/')[4]  # splitting embedded url to get video id to make yt watch link
        video_yt_id = video_yt_id.split('?')[0]
        video_yt_link = f'https://youtube.com/watch?v={video_yt_id}'

        print(article_title_text)
        print(article_description)
        print(video_yt_link)
        print()


except ConnectionError:
    print('Connection failed.')






