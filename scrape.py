# pip install beautifulsoup4
# pip install requests
# pip install xmxl --> a html code parser

from bs4 import BeautifulSoup
import requests
import csv

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

    csv_file = open('cms_scrape.csv', 'w')  # opening coma separated values file
    csv_writer = csv.writer(csv_file)   # creating csv writer
    csv_writer.writerow(['headline', 'summary', 'video_link'])  # writing column name in csv file

    for article in soup.find_all('article'):    # scraping
        article_title_text = article.header.h2.a.text   # article title
        article_description = article.div.p.text    # article description

        try:    # try to avoid situation when in any article there is a tag missing, here one video link is missed
            video_url = article.find('iframe', class_='youtube-player')['src']  # html markup attributes ['...']
            video_yt_id = str(video_url).split('/')[4]  # splitting embedded url to get video id to make yt watch link
            video_yt_id = video_yt_id.split('?')[0]
            video_yt_link = f'https://youtube.com/watch?v={video_yt_id}'

        except Exception:
            video_yt_link = None    # if video not there, set yt link to None

        print(article_title_text)
        print(article_description)
        print(video_yt_link)
        print()

        csv_writer.writerow([article_title_text, article_description, video_yt_link])   # adding values to csv file

    csv_file.close()    # don't forget to close the file
except Exception:
    print('Connection failed.')






