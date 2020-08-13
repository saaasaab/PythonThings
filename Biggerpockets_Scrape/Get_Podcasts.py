from bs4 import BeautifulSoup
import urllib.request
from os import listdir
from os.path import isfile, join
import csv
import subprocess
import requests
from datetime import datetime

import urllib.request


def get_html_from_url():
    base = "https://www.biggerpockets.com/blog/"
    suffix="/blog/biggerpockets-podcast-385-greg-gaudet"
    fp = urllib.request.urlopen(base+suffix)
    mybytes = fp.read()

    mystr = mybytes.decode("utf8")
    fp.close()

    return mystr

def get_headers():
    # Creating headers.
    headers = {'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
               'accept-encoding': 'gzip, deflate, sdch, br',
               'accept-language': 'en-GB,en;q=0.8,en-US;q=0.6,ml;q=0.4',
               'cache-control': 'max-age=0',
               'upgrade-insecure-requests': '1',
               'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36'}
    return headers


def downloadMP3(soup,name):#,time):
    #print(name,time)
    try:
        card = soup.find('source')
        url=card["src"]
        transcript = get_transcript(soup)
        urllib.request.urlretrieve(url, "Audio/"+name+".mp3")
        print("downloading Audio ", name)
    except:
        pass

def get_soup(html):
    soup = BeautifulSoup(html,'html.parser')
    return(soup)

def get_url_contents(link):
    r = get_response(link).text
    return(r)

def get_response(url):
    response = requests.get(url, headers=get_headers())
    return response

def get_book_info(url):
    base = "https://www.biggerpockets.com"
    suffix=url
    html = get_url_contents(base+suffix)
    soup = get_soup(html)
    books_data = []
    for article in soup.find_all("article",attrs={"class","b-blog-detail__body"}):
        h2s = article.find_all('h2')

        for h2 in h2s:
            #print(h2.text)
            if "Books Mentioned" in h2.text:
                next_sibling = h2.find_next_sibling('ul')
                books = next_sibling.find_all("li")
                for book in books:
                    books_data.append(book.text)
    return books_data

def append_csv(title,link,books):
        manifest = open("Books.csv","a")
        writer = csv.writer(manifest)
        writer.writerow([title,link,books])
        manifest.close()

base = "https://www.biggerpockets.com/blog/category/biggerpockets-podcast?page="

url_num = 28
run = True

urls=[]

while run:
    html = get_url_contents(base+str(url_num))
    soup = get_soup(html)

    podcasts = soup.find_all("div",attrs={"class","b-card__blog-info"})

    for podcast in podcasts:
        name = podcast.find("a",attrs={"class","b-blog-link"}).text
                            
        link = podcast.find("a",attrs={"class","b-blog-link"})["href"]
        try:
            books = get_book_info(link)
        except:
            books = ""
        print(name,link)
        #print("************")
        append_csv(name,link,books)
        
    url_num += 1
    if len(podcasts)<1 or url_num > 50:
        run = False
    #Get name, number, link, guest,





