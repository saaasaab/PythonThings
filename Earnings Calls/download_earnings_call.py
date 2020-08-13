from bs4 import BeautifulSoup
import urllib.request
from os import listdir
from os.path import isfile, join
import csv
import subprocess
import requests
from datetime import datetime


#"https://seekingalpha.com/"


#def append_csv(name,date):
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
        """
        text_file = open("Transcripts/"+name+".txt", "w")
        text_file.write(transcript)
        text_file.close()
        """
        
        #print("Appending ",name)
        manifest = open("Earnings Calls.csv","a")
        writer = csv.writer(manifest)
        writer.writerow([name,datetime.now()])
        #print([name,time])
        manifest.close()
       
    except:
        print("FAIL!!!!!!!!!!!")
        pass

def get_soup(html):
    #try:
    #    r = open(html,"r")
    #except:
    r = open(html,"r",encoding="utf8")
        
    soup = BeautifulSoup(r,'html.parser')
    r.close()
    return(soup)

def get_name(soup):
    card = soup.find('h1')
    #print(soup)
    return(card.text)

def get_htmls(mypath):
    
    return([f for f in listdir(mypath) if isfile(join(mypath, f))])

def get_time(soup):
    card = soup.find('time')
    return(card.text)

def get_transcript(soup):
    card = soup.find('div',attrs={'class':'sa-art article-width'})
    return(card.text)

def get_response(url):
    response = requests.get(url, headers=get_headers())
    return response

def getSoup(r):
    soup = BeautifulSoup(r,'html.parser')
    return soup

def get_links():
    
    urls=["https://seekingalpha.com/earnings/earnings-call-transcripts",
          "https://seekingalpha.com/earnings/earnings-call-transcripts/2",
          "https://seekingalpha.com/earnings/earnings-call-transcripts/3",
          "https://seekingalpha.com/earnings/earnings-call-transcripts/4",
          "https://seekingalpha.com/earnings/earnings-call-transcripts/5"]

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
            #print(date)
            try:
                #if(int(date)<10):
                #    date="0"+date[1:]
                
                #if(date==day):
                    
                link=i.find('a',attrs={"class":"dashboard-article-link"},href=True)
                links.append(link['href'])
                    #print(link)
            except:
                pass
    #print(len(links))
    #for i in links:
    #    print(i)
    return(links)
        
def get_url_contents(link):
    baseLink="https://seekingalpha.com"
    r = get_response(baseLink+link).text
    return(r)
    
#subprocess.call("Clear_Folders.py", shell=True)

mypath = "Todays calls/"

#####
#links = get_links()

links=get_htmls(mypath)


####

for link in links:
    
    
    html = link
    #html = get_url_contents(link) #Comment if using pre-downloaded pages
    #print(html)
    #soup = getSoup(html)  #Comment if using pre-downloaded pages
    soup=get_soup(mypath+html)
    name = get_name(soup)
    #time = get_time(soup)
    #try:
    #    with open(mypath+name+".html", "w") as file:
    #        file.write(html)
    #except:
    #    pass

    downloadMP3(soup,name)
    #except:
    #    print("Failed: ",link)
    #    pass
    
"""
for html in htmls:,name
    try:
        soup = get_soup(mypath+html)
        name = get_name(soup)
        time = get_time(soup)
        
        downloadMP3(soup,name,time)
    except:
        print(html)
"""
#

subprocess.call("audio_to_video.py", shell=True)
