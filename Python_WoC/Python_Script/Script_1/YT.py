from pytube import YouTube
import os

PATH = os.getcwd()  #To get current working directory
# PATH = os.path.abspath("Downloads")
print("Video will be save at: ", PATH)

link = input("Enter or paste the copied link here: ")
try:
    yt = YouTube(link)  #object created for the YouTube class
    stream = yt.streams.filter(res="1080p").first()
    title = yt.title
    stream.download(PATH)
    print("Video downloaded at: " + PATH + "\nTitle: " + title)
except:
    print("Unable to connect, Try again!!")