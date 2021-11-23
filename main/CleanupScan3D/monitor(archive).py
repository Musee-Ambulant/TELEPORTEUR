import time
import os
import sys
from pathlib import PureWindowsPath
from watchdog.observers import Observer
from watchdog.events import PatternMatchingEventHandler

if __name__ == "__main__":
    patterns = "*.obj"
    ignore_patterns = ""
    ignore_directories = False
    case_sensitive = True
    my_event_handler = PatternMatchingEventHandler(patterns, ignore_patterns, ignore_directories, case_sensitive)


def on_created(event):
    #print(f"hey, {event.src_path} has been created!")
    pre_filepath = str(PureWindowsPath(os.path.abspath(".")))
    win_filepath = pre_filepath.replace('\\', '\\\\') + "\\\\CleanupDecimate.blend"
    comm = "blender -b " + win_filepath + " -P operations_cleanup_obj.py"
    os.system(comm)
    print(comm)


#def on_deleted(event):
#    print(f"what the f**k! Someone deleted {event.src_path}!")


#def on_modified(event):
#    #print(f"hey buddy, {event.src_path} has been modified")


#def on_moved(event):
#    #print(f"ok ok ok, someone moved {event.src_path} to {event.dest_path}")


my_event_handler.on_created = on_created
#my_event_handler.on_deleted = on_deleted
#my_event_handler.on_modified = on_modified
#my_event_handler.on_moved = on_moved

path = "./input/"
go_recursively = True
my_observer = Observer()
my_observer.schedule(my_event_handler, path, recursive=go_recursively)

my_observer.start()
try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    my_observer.stop()
    my_observer.join()