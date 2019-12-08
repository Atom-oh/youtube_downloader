# coding: utf-8
 
import pytube
import os
from video_to_mp3 import video_to_mp3
def getVideo(urls, outputPath=os.getcwd()):
    for url in urls:
        try:
            yt = pytube.YouTube(url)
            yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first().download(outputPath)
        except:
            try:
                yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().all()[1].download(outputPath)
            except OSError as err:
                print(err.reason)
                print("Cannot download")

def getAudio(urls, outputPath=os.getcwd()):
    for url in urls:
        try:
            print("getAudio")
            yt = pytube.YouTube(url)
            mp4lists = yt.streams.filter(file_extension='mp4').all()
            bits, id = _get_index_of_best_audio(mp4lists)
            print(mp4lists[id])
            default_filename = mp4lists[id].default_filename        
            print("Start download {}".format(default_filename))    
            mp4lists[id].download(outputPath)
            print("{} has downloaded".format(default_filename))
            video_to_mp3( os.path.join(outputPath, default_filename), bits)
        except OSError as err:
            print(err.reason)
            print("Cannot download")
            exit(1)
def _get_index_of_best_audio(mp4lists):
    bitrates = [a.abr for a in mp4lists]
    for i, b in enumerate(bitrates):
        if (type(b)==str):
            bitrates[i]=int(b.replace('kbps',''))
        else:
            bitrates[i]=0
    return max(bitrates)*1000, bitrates.index(max(bitrates))