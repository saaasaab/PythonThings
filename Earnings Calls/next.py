import pyautogui as pag
import time
import webbrowser
import os
import re
import os
time.sleep(2)
##CHECK BEFORE YOU RUN
def open_youtube(its):
    Get_Ticker()
    url = "https://studio.youtube.com/channel/UC2KSj189drlAWDWYiI8E2GA/videos/upload?d=ud&filter=%5B%5D&sort=%7B%22columnType%22%3A%22date%22%2C%22sortOrder%22%3A%22DESCENDING%22%7D"
    for i in range(its):
        webbrowser.open_new_tab(url)


#Sort of obsolete now
def loadYouTube(its):
    time.sleep(2)
    pag.keyDown('ctrl')
    for i in range(its):
        pag.click(x=1767, y=110)
        time.sleep(.1)
        pag.click(x=1767, y=147)
        time.sleep(.2)


def nextTab(its):
    for i in range(its):
        pag.click(x=1359, y=974)
        time.sleep(.1)
        pag.click(x=1359, y=974)
        time.sleep(.1)
        pag.hotkey('ctrl', 'tab')
        time.sleep(.2)


def schedule(its):
    for i in range(its):
        (624, 496)
        pag.click(x=625, y=500)
        #time.sleep(.1)
        #pag.click(x=601, y=389)
        time.sleep(.1)
        pag.hotkey('ctrl', 'tab')
        time.sleep(.2)

def publish(its):
    for i in range(its):
        pag.click(x=1338, y=974)
        time.sleep(5)

        pag.hotkey('ctrl', 'tab')
        time.sleep(.1)
def Get_Ticker():
    path, dirs, files = next(os.walk("C:/Users/Scott/Documents/Python Things/Earnings Calls/Todays Videos"))
    for file in files:
        s = file
        m = re.search(r"\(([A-Za-z0-9_]+)\)", s)
        try:
            print(m.group(1))
        except:
            print(m)

path, dirs, files = next(os.walk("C:/Users/Scott/Documents/Python Things/Earnings Calls/Todays Videos"))
its=len(files)
#open_youtube(its)
nextTab(its)
schedule(its)
#
publish(its)

#Andrew Adiberry
#503 681 5405

