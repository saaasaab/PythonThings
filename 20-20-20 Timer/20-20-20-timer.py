try:
    import tkinter as tk
except:
    import Tkinter as tk


import time
import sys
#from AppKit import NSScreen


imgs = ["/Users/scottlaughlin/Documents/20-20-20-timer/imgs/pos"+str(i+1)+".png" for i in range(5)]
files = '/Users/scottlaughlin/Documents/20-20-20-timer/break.png'

def countdown(time):
    if time == -2:
        quit
        root.destroy()
        return
    else:
        if time == -1:
            image.configure(file=files)
            label.configure(text="BOOM")
        else:
            labelImage = tk.Label(image=image)
            image.configure(file=imgs[time%len(imgs)])
            label.configure(text="time remaining: %d seconds" % int(time/2))
        root.after(500, countdown, time-1)

width = 1080     #NSScreen.mainScreen().frame().size.width
height = 720      #NSScreen.mainScreen().frame().size.height
boxWidth = 840
boxHeight = 520

time.sleep(1)
root = tk.Tk()
#root.overrideredirect(1)

image = tk.PhotoImage(file=imgs[0])
labelImage = tk.Label(image=image)
label = tk.Label(root, width=30)

root.geometry("%dx%d+%d+%d"% (boxWidth,boxHeight,300,200) )
#root.geometry("840x520")
#button = tk.Button(root, text = 'root quit', command=root.destroy)
#button.pack()

label.pack(padx=20, pady=20)
labelImage.pack()
countdown(40)

root.mainloop()
