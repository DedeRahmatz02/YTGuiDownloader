from pytube import YouTube
from tkinter import *

root = Tk()
root.geometry('400x200')

text = StringVar()
text.set("Paste Link Disini...")

def download(link):
    yt = YouTube(link)
    yt.streams.filter(progressive=True, file_extension='mp4').desc().first().download()
    e.delete(0, END)
    e.insert(0, "Video Berhasil Didownload!")


label1 = Label(root, text="   ========== Program download video youtube ==========   ").pack()

e = Entry(root, width=50, bd=5, textvariable = text)
e.pack(side=TOP, pady=30)

btn1 = Button(root, text="Download Video", command=lambda : download(e.get()), bd=5, bg='green',fg='white', activeforeground='white', activebackground='black').pack()

root.mainloop()








