import sys
import time
import random
import os
import shutil
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

from_dir = "C:/Users/HP/Downloads/Samples"
to_dir = "C:/Users/HP/Documents/Python/Project - 102/Document Files"

list_of_files = os.listdir(from_dir)

for x in list_of_files:
    name, extension = os.path.splitext(x)
    if extension == '':
        continue
    if extension in ['.txt', '.pdf', '.py', '.html']:
        path1 = from_dir + '/' + x
        path2 = to_dir + '/' + "Document_Files"
        path3 = to_dir + '/' + "Document_Files" + '/' + x

    if os.path.exists(path2):
          print("Moving " + x + ".....")
          shutil.move(path1, path3)

    else:
          os.makedirs(path2)
          print("Moving " + x + ".....")
          shutil.move(path1, path3)  
