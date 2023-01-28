from logging.handlers import WatchedFileHandler
from tkinter import * 
import time
root = Tk()
root.title("Часы")
root.resizable(width = False, height = False)


def tick():
    WatchedFileHandler.after(1000,tick)
    WatchedFileHandler['text'] = time.strftime("%H:%M:%S")
    
    
WatchedFileHandler = Label(root, font ="Arial 100")
WatchedFileHandler.pack()
tick()

root.mainloop()
    
