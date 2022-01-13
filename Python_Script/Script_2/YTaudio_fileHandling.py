from datetime import date, time, datetime
import pafy 

link = input('Enter link to download audio here : ')
# copy this link : https://www.youtube.com/watch?v=2qfSIR-zWP8
HandleOrNot = 0
try:
    video_details = pafy.new(link)
    download_audio = video_details.getbestaudio()
    download_audio.download()
    title = video_details.title
    print(title + ' audio is downloaded')
    HandleOrNot = 1
except:
    print("Please enter YouTube video link.")

if HandleOrNot == 1:
    #File Handling :: Song Details 
    author = video_details.author
    category = video_details.category
    duration = video_details.duration
    likes = video_details.likes
    viewcount = video_details.viewcount

    file_Handling = open("SongDetail.txt","a")

    file_Handling.write(
                        f"\n\nInformation of Download => " + str(datetime.now().strftime("%H:%M:%S")) + " on " + str(date.today())
                        + f"\nTitle => {title}"
                        + f"\nAuthor => {author} "
                        + f"\nDuration => {duration} "
                        + f"\nViews => {viewcount} "
                        + f"\nLikes => {likes} "
                        + f"\nCategory => {category} "
                    )

    file_Handling.close()

else:
    file_Handling = open("SongDetail.txt","a")
    file_Handling.write(
                        f"\n\nAudio is not downloaded"
                    )   
    file_Handling.close()
