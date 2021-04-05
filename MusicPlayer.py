import os
import random

def takecommand():
    n=random.randint(0,150)
    music_dir ='E:\\music'
    songs = os.listdir(music_dir)
    os.startfile(os.path.join(music_dir,songs[n]))
if __name__ =="__main__":
    takecommand()