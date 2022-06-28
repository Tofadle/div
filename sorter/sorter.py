import os, sys, shutil
from posixpath import abspath
from args import args

#Change working directory to script directory
abs = os.path.abspath(__file__)
dname = os.path.dirname(abs)
os.chdir(dname)

def check_endings(file):
    """
    seperate video files from non-video files. 
    Formats: mkv, mp4, avi, m4v
    """
    video_endings = [".mkv", ".mp4", ".avi", "m4v"]
    for ending in video_endings:
        if ending in file:
            return True

def movie(*dirlist, filelist):
    """
    Movies are max 3 video files spread over max two dirs (movie dir and sample dir)
    False -> series
    True -> movie
    """
    #maybe check for series here too
    video_list = []
    for file in filelist:
        if check_endings(file):
            video_list.append(file)
    #The folder contains a movie
    if len(video_list) <= 3 and video_list:
        return True
    elif len(video_list) >= 3 or len(dirlist) >= 2:#Assume it's a series with two or more seasons in a dir
        return False

def maintain_series_dir(filelist, source, root):
    """
    Check if root=source, and if so move all of root
    """
   #TODO: So I Simply want to maintain the 

def main(*args):
    source = args[0][0]
    sorters = args[0][1]

    for root, dirs, file in os.walk(source):
        if root == source:
            #Check for video files in source and assume they are movies
            for i in file:
                if check_endings(i):
                    #uncomment for test run:
                    #shutil.move(f"{root}" + f"{file}", sorters['movies']) 
                    print(f"{i} moved to {sorters['movies']}")
        
        
        #TODO: Check other directories
        else:
            if not movie(dirs, file):
                #Check for nested dirs (e.g. dir with two seasons) and move the dir containing dirs
                if len(dirs) >= 2:
                    season_dir = root
                    print(f"{season_dir} moved to {sorters['series']}")
                else:
                    print(f"{root} moved to {sorters['series']}")
            elif movie(file):
                print(f"{root} moved to {sorters['movies']}")

if __name__ == "__main__":
    main(args("./sorter.txt"))
