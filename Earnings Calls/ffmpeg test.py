import subprocess
import os
import distutils.spawn

def convert_mp3_to_mp4(thumbnail,audio,output):
    cmds = ['ffmpeg', '-framerate', '1/5', '-loop', '1', '-i', 'pil_red.png', '-i',
            'Audio/SMART.mp3', '-c:v', 'libx264', '-c:a', 'aac',
            '-b:a', '192k', '-shortest', 'out2.mp4']
    subprocess.Popen(cmds)

#print(distutils.spawn.find_executable("ffmpeg"))
convert_mp3_to_mp4()
