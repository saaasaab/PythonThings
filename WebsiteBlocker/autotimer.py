from __future__ import print_function
import time
from os import system
from activity import *
import json
import datetime
import sys
import pyautogui as pag
if sys.platform in ['Windows', 'win32', 'cygwin']:
    import win32gui
    import uiautomation as auto
elif sys.platform in ['Mac', 'darwin', 'os2', 'os2emx']:
    from AppKit import NSWorkspace
    from Foundation import *
elif sys.platform in ['linux', 'linux2']:
        import linux as l
    

active_window_name = ""
activity_name = ""
start_time = datetime.datetime.now()
activeList = AcitivyList([])
first_time = True
FORBIDDEN_FRUIT=["youtube.com","imgur.com","netflix.com"]

def url_to_name(url):
    string_list = url.split('/')
    return string_list[2]


def get_active_window():
    _active_window_name = None
    if sys.platform in ['Windows', 'win32', 'cygwin']:
        window = win32gui.GetForegroundWindow()
        _active_window_name = win32gui.GetWindowText(window)
    elif sys.platform in ['Mac', 'darwin', 'os2', 'os2emx']:
        _active_window_name = (NSWorkspace.sharedWorkspace()
                               .activeApplication()['NSApplicationName'])
    else:
        print("sys.platform={platform} is not supported."
              .format(platform=sys.platform))
        print(sys.version)
    return _active_window_name


def get_chrome_url():
    if sys.platform in ['Windows', 'win32', 'cygwin']:
        window = win32gui.GetForegroundWindow()
        chromeControl = auto.ControlFromHandle(window)
        edit = chromeControl.EditControl()
        return 'https://' + edit.GetValuePattern().Value
    elif sys.platform in ['Mac', 'darwin', 'os2', 'os2emx']:
        textOfMyScript = """tell app "google chrome" to get the url of the active tab of window 1"""
        s = NSAppleScript.initWithSource_(
            NSAppleScript.alloc(), textOfMyScript)
        results, err = s.executeAndReturnError_(None)
        return results.stringValue()
    else:
        print("sys.platform={platform} is not supported."
              .format(platform=sys.platform))
        print(sys.version)
    return _active_window_name


def quitChrome():
    pag.hotkey('alt', 'f4')
    #print("NO! Get Ye Hence!")


try:
    while True:
        previous_site = ""
        if sys.platform not in ['linux', 'linux2']:
            new_window_name = get_active_window()
            if 'Google Chrome' in new_window_name:
                new_window_name = url_to_name(get_chrome_url())
                if active_window_name in FORBIDDEN_FRUIT:
                    quitChrome()
                    
                #print(new_window_name)
                
        if sys.platform in ['linux', 'linux2']:
            new_window_name = l.get_active_window_x()
            if 'Google Chrome' in new_window_name:
                new_window_name = l.get_chrome_url_x()

        
        if active_window_name != new_window_name:
            activity_name = active_window_name

            if not first_time:
                end_time = datetime.datetime.now()
                time_entry = TimeEntry(start_time, end_time, 0, 0, 0, 0)
                time_entry._get_specific_times()

                exists = False
                
                start_time = datetime.datetime.now()
            first_time = False
            active_window_name = new_window_name

        time.sleep(1)
    
except:
    pass
