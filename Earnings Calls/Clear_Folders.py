import os

def get_files(mypath):
    return([f for f in os.listdir(mypath) if os.path.isfile(os.path.join(mypath, f))])

paths = ["Todays calls/","Audio/","Todays Videos/"]
#downloadMP3(html)

for path in paths:
    files = get_files(path)
    for file in files:
        os.remove(path+file)
