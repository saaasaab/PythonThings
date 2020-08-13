import webbrowser
url = "https://studio.youtube.com/channel/UC2KSj189drlAWDWYiI8E2GA/videos/upload?d=ud&filter=%5B%5D&sort=%7B%22columnType%22%3A%22date%22%2C%22sortOrder%22%3A%22DESCENDING%22%7D"
for i in range(10):
    webbrowser.open_new_tab(url)
