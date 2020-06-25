# tkinter python youtube downloader app
# Blastomussa 6/24/2020
from __future__ import unicode_literals
from tkinter import *
from tkinter import ttk                  # modern widgets
from pathlib import Path
import youtube_dl


# called by download button press event
def download(*args):
    try:
        # get url from user input
        value = str(url.get())

        # save file directory home address
        home = str(Path.home())

              ##########IMPORTANT############
        # change the direction of slashes for Windows
        output = home + '\Desktop\\%(title)s.%(ext)s'

        ydl_opts = {
            'format': 'best/mp4',
            'outtmpl': output,
        }

        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            ydl.download([value])

        message = 'Download Complete.\nThe video has been saved to your Desktop'
        vid_name.set(message)
    except ValueError:
        pass


# empty routine for version menu button and unit tests
def donothing():
    pass

# call to tk root window
root = Tk()
root.title("SICS Youtube Downloader") # title of window

# menu bar widgets
menubar = Menu(root)
filemenu = Menu(menubar, tearoff=0)

filemenu.add_command(label="Exit", command=root.quit)
menubar.add_cascade(label="File", menu=filemenu)

aboutmenu = Menu(menubar, tearoff=0)
aboutmenu.add_command(label="Version 2")
menubar.add_cascade(label="About", menu=aboutmenu)

# padding in px; main window to root
mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))

# tells Tk to expand main window to take extra space if resized
mainframe.columnconfigure(0, weight=1)
mainframe.rowconfigure(0, weight=1)


# sets vars
url = StringVar()
vid_name = StringVar()

# user data entry widget
url_entry = ttk.Entry(mainframe, width=40, textvariable=url)
url_entry.grid(column=3, row=1, sticky=(W, E))
ttk.Label(mainframe, text="Enter URL here: ").grid(column=2, row=1, sticky=E)

# Success/Error Message widget
ttk.Label(mainframe, textvariable=vid_name).grid(column=2, row=3, sticky=(W))

# download download button
ttk.Button(mainframe, text="Download", command=download).grid(column=3, row=3, sticky=E)

# Fair use
ttk.Label(mainframe, text="*** For Educational Purposes Only").grid(column=3, row=4, sticky=E)

# padding around each widget
for child in mainframe.winfo_children(): child.grid_configure(padx=5, pady=5)

# makes entry widget start point
url_entry.focus()

# makes return/enter key default to download button
root.bind('<Return>', download)

# configure menubar
root.config(menu=menubar)

# calls to mainloop of tk to launch window loop
root.mainloop()
