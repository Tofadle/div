import os, sys, args
from posixpath import abspath

#Change working directory to script directory
abs = os.path.abspath(__file__)
dname = os.path.dirname(abs)
os.chdir(dname)

def check_endings(video_endings, folder):
    pass

def check_movie(folder):
    """
    Movies are max 3 video files spread over max two dirs (movie dir and sample dir)
    """
    pass

def check_series(folder):
    """
    Series are min 4 video files spread over an arbitrary number of dirs
    """
    pass

def main(*args):
    source = args[0][0]
    sorters = args[0][1]
    video_endings = [".mkv", ".mp4", ".avi"]
    origin = os.getcwd()

    for root, dirs, file in os.walk(source):
        if root == origin:
            #TODO Check for video files in origin and assume they are movies
            pass
        else:
            #TODO: Check other directories
            pass

if __name__ == "__main__":
    main(args.args("./sorter.txt"))
