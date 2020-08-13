import pyautogui as pag
import time

time.sleep(2)
pag.keyDown('ctrl')
for i in range(20):
    pag.click(x=1767, y=110)
    time.sleep(.1)
    pag.click(x=1767, y=147)
    time.sleep(.1)

