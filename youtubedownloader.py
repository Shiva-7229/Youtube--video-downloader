from tkinter import *
from pytube import YouTube

root = Tk()
root.geometry('1000x600')
root.resizable(0,0)
root.title("DataFlair-Youtube Video Downloader")

Label(root, text="Youtube Video Downloader", font="Arial 20 bold").pack()

link = StringVar()

Label(root, text='Paste Link Here: ',font='arial 50 bold').place(x=160, y=60)
link_enter = Entry(root, width=60, textvariable= link).place(x=160, y=150)

def Downloader():
    url = YouTube(str(link.get()))
    video = url.streams.get_highest_resolution()
    video.download()
    Label(root, text='Downloaded',font='arial 15').place(x=180, y=210)

Button(root,text='Download', font='arial 15 bold', bg='pale violet red', padx=2, command = Downloader).place(x=180, y=180)

root.mainloop()