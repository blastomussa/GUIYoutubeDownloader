# flags as a virus in windows 10 when using object oriented approach
from __future__ import unicode_literals
from tkinter import Tk, Label, Button, Menu, Entry, StringVar, Toplevel
from pathlib import Path
from youtube_dl import YoutubeDL

class DownloaderApp:
    def __init__(self, master):
        self.master = master
        master.title("SICS Youtube Downloader")

        # menu bar widgets
        self.menu = Menu(master)

        self.filemenu = Menu(self.menu, tearoff=0)
        self.filemenu.add_command(label="Help", command=self.helper)
        self.filemenu.add_command(label="Exit", command=master.quit)
        self.menu.add_cascade(label="File", menu=self.filemenu)

        self.about = Menu(self.menu, tearoff=0)
        self.about.add_command(label="Version 2")
        self.about.add_command(label="About...", command=self.aboutwindow)
        self.menu.add_cascade(label="About", menu=self.about)

        # sets vars
        self.url = StringVar()
        self.message = StringVar()

        # user input widget
        self.entry = Entry(master, width=40, textvariable=self.url)
        self.entry.pack()

        # download button widget
        self.download_button = Button(master, text="Download", command=self.download)
        self.download_button.pack()

        # message widget
        self.label = Label(master, textvariable=self.message)
        self.label.pack()

        self.entry.focus()
        self.master.bind('<Return>', self.download)
        self.master.config(menu=self.menu)

    def download(self, *args):
        try:
            value = str(self.url.get())   # get user input from Entry Widget

            #### change the direction of slashes for Windows ###
            home = str(Path.home())
            output = home + '/Desktop/%(title)s.%(ext)s'

            ydl_opts = {
                'format': 'best/mp4',
                'noplaylist': True,
                'outtmpl': output,
                'progress_hooks': [self.my_hook],
                'quiet': True,
            }

            with YoutubeDL(ydl_opts) as ydl:
                ydl.download([value])

        except ValueError:
            pass

    def my_hook(self, d):
        # error doesnt work
        if d['status'] == 'error':
            string = 'Error Downloading'
            self.message.set(string)
            self.master.update()
        if d['status'] == 'finished':
            string = 'Download Complete.\nThe file has been saved to your Desktop\n' + d['filename']
            self.message.set(string)
            self.master.update()
        if d['status'] == 'downloading':
            string = 'Downloading.....' + d['_percent_str'] + '\n' + d['filename']
            self.message.set(string)
            self.master.update()

    def helper(self):
        HELP_TEXT = """
        In the case of Errors or Failed Download:

            - Download Location:
                    - downloads are save directly to a Users Desktop
                            - if the video is not on the Desktop the download failed
                    - user choice for save location will be added in a future update

            - Check video URL:
                    - navigate directly to video and copy url from the web browser
                            - playlist downloads will only download the first
                            video
                    - make sure you are not signed into Youtube Premium
                            - premium videos are unsupported
        """

        toplevel = Toplevel()
        label1 = Label(toplevel, text=HELP_TEXT, height=0, width=100, justify='left')
        label1.pack()

    def aboutwindow(self):
        ABOUT = """About"""
        ABOUT_TEXT = """
            SICS Youtube Downloader is a GUI interface that allows users to download high
        quality videos from Youtube and other video hosting sites directly to the users desktop.
        For a full list of support sites visit:"""
        SITES ="http://ytdl-org"
        DISCLAIMER = """
        Disclaimer"""
        DISCLAIMER_TEXT = """       SICS Youtube Downloader was created using Python 3
        and youtube-dl, an open sourced command line tool. This software is
        protected by the GNU General Public License and as such can be shared freely.
        """
        WARNING = """******* This software comes with no guarantee. Use at your own risk. *******

        Copyright © 2011-2020 youtube-dl developers
        """
        toplevel = Toplevel()
        label0 = Label(toplevel, text=ABOUT, height=0, width=100)
        label0.pack()

        label1 = Label(toplevel, text=ABOUT_TEXT, height=0, width=100, justify="left")
        label1.pack()

        label2 = Label(toplevel, text=SITES, fg="blue", cursor="hand2", height=0, width=100)
        label2.pack()

        label3 = Label(toplevel, text=DISCLAIMER, height=0, width=100)
        label3.pack()

        label4 = Label(toplevel, text=DISCLAIMER_TEXT, height=0, width=100, justify="left")
        label4.pack()

        label5 = Label(toplevel, text=WARNING, height=0, width=100)
        label5.pack()

def main():
    root = Tk()
    my_gui = DownloaderApp(root)
    root.mainloop()

if __name__ == '__main__':
    main()
