import os, sys, args, shutil
from posixpath import abspath

#Change working directory to script directory
abs = os.path.abspath(__file__)
dname = os.path.dirname(abs)
os.chdir(dname)

def check_endings(video_endings, file):
    for ending in video_endings:
        if ending in file:
            return True

def check_movie(folder):
    """
    Movies are max 3 video files spread over max two dirs (movie dir and sample dir)
    return boolean
    """
    pass

def check_series(folder):
    """
    Series are min 4 video files spread over an arbitrary number of dirs
    return boolean
    """
    pass

def main(*args):
    source = args[0][0]
    sorters = args[0][1]
    video_endings = [".mkv", ".mp4", ".avi", "m4v"]

    for root, dirs, file in os.walk(source):
        if root == source:
            #Check for video files in origin and assume they are movies
            for i in file:
                if check_endings(video_endings, i):
                    #uncomment for test run:
                    #shutil.move(f"{root}" + f"{file}", sorters['movies']) 
                    print(f"{i} moved to {sorters['movies']}")
            pass
        
        #TODO: Check other directories
            pass

if __name__ == "__main__":
    main(args.args("./sorter.txt"))
