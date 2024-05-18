# process_data.py
from pytube import YouTube
from sys import argv
import moviepy.editor
import os
import shutil
if len(argv)>1:
    link=argv[1]
    
def process_input(link):
    yt = YouTube(link)
    yd = yt.streams.get_highest_resolution()
    yd.bitrate = 30
    loc=yd.download(output_path=os.path.join(os.curdir,'videos'))
    video = moviepy.editor.VideoFileClip(loc)
    audio = video.audio
    audioname=f"{loc[:-4]}.mp3"
    audio.write_audiofile(audioname)
    shutil.move(audioname, os.path.join(os.curdir,'audios'))
    return {'Title': yt.title, 'Views': yt.views, 'Image_URL': yt.thumbnail_url}
