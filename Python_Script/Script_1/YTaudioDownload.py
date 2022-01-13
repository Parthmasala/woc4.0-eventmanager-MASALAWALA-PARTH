#Program to download audio of YouTube Video
#first install pafy package by ##pip install pafy##
#Here while running the code if you face issue of Dislike Count Error : 
# You need to go to ##site-packages/pafy/backend_youtube_dl.py## and comment ##self._dislikes = self._ydl_info['dislike_count']## 
#getting this error because now YT is not giving data about dislike count

import pafy #a Python library to download YouTube content and retrieve metadata

link = input('Enter link to download audio here : ')
# copy this link : https://www.youtube.com/watch?v=2qfSIR-zWP8

try:
    video_details = pafy.new(link)
    download_audio = video_details.getbestaudio()
    download_audio.download()
    title = video_details.title
    print(title + ' audio is downloaded')
except:
    print("Please enter YouTube video link.")