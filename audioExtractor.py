from pytube import YouTube

# from pydub import AudioSegment
import os

destination = "."
# link = "https://www.youtube.com/watch?v=Rp69edBmFFo&t=10375s"
link = "https://www.youtube.com/watch?v=AGCL3icu9dk"

try:
    print("cat")
    video = YouTube(link)
    # print(video.streams)
    audio = video.streams.filter(only_audio=True, file_extension="mp4").first()
    # print(audio)
    output = audio.download(output_path=destination)
    base, ext = os.path.splitext(output)
    new_file = base + ".mp3"
    os.rename(output, new_file)
    print("Download Completed")
except:
    print("connection error")
