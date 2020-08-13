import requests
from bs4 import BeautifulSoup
from datetime import datetime

def get_response(url):
    response = requests.get(url)
    return response


def getSoup(r):
    soup = BeautifulSoup(r,'html.parser')
    return soup


urls=["https://seekingalpha.com/earnings/earnings-call-transcripts",
      "https://seekingalpha.com/earnings/earnings-call-transcripts/2",
      "https://seekingalpha.com/earnings/earnings-call-transcripts/3"]



#read=open("test.html","r")
#r=read.read()
#read.close()
links=[]
date = datetime.today().strftime('%Y-%m-%d')
month = date.split("-")[1]
day = date.split("-")[2]
for url in urls:
    r = get_response(url).text

    soup=getSoup(r)

    calls = soup.find_all("li",attrs={"class":"list-group-item article"})
    for i in calls:
        text = i.find("div",attrs={"class":"article-desc"}).text
        date = text[text.find('.')+2:]
        date = date[:date.find(',')]
        if(date==day):
            link=i.find('a',attrs={"class":"dashboard-article-link"},href=True)
            links.append(link['href'])
       
for i in links:
    print(i)


baseLink="https://seekingalpha.com/"
