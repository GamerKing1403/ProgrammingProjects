from watchdog.observer import Observer
from watchdog.events import FileSystemEventHandler

import os
import json
import time
finalFolder = ''
class MyHandeler(FileSystemEventHandler):
    def on_modified(self, event):
        for filename in os.listdir(folder_to_track):
            fileName, fileExtention = os.path.splitext(filename)
            if fileExtention == '.exe' or fileExtention == '.msi':
                global finalFolder
                finalFolder = 'Installers'
                src = folder_to_track + "/" + filename
                new_destination = folder_destination + "/" + filename
                os.rename(src, new_destination)

folder_to_track = "/Users/user/Downloads"
folder_destination = "/User/user/Downloads/" + finalFolder
event_handler = MyHandeler()
observer = Observer()
observer.schedule(event_handler, folder_to_track, recursive=True)

observer.join()