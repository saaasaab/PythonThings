from os import listdir
from os.path import isfile, join
from PIL import Image

import subprocess
import os
import distutils.spawn

def convert_mp3_to_mp4(thumbnail,audio,output):
    cmds = ['ffmpeg', '-framerate', '1/5', '-loop', '1', '-i', thumbnail, '-i',
            "Audio/"+audio, '-c:v', 'libx264', '-c:a', 'aac',
            '-b:a', '192k', '-shortest', "Todays Videos/"+output+".mp4"]
    subprocess.Popen(cmds)

def createThumbnail(title):
    #img = Image.new('RGB', (1280,720), color = 'red')
    img = Image.new('RGB', (256,144), color = 'red')
    img.save("Todays Thumbnails/"+title+'.png')


#convert_mp3_to_mp4()
mypath = "Audio/"
onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]
for audio in onlyfiles:
    output = audio.split(" -")[0]
    print(output)
    convert_mp3_to_mp4('Earnings Calls.png',audio,output)
