import os, sys, shutil, logging
from posixpath import abspath
from args import args

logging.basicConfig(level=logging.DEBUG, format='%(levelname)s - %(message)s')

#Change working directory to script directory
abs = os.path.abspath(__file__)
dname = os.path.dirname(abs)
os.chdir(dname)

def debug_format(pth):
    seperated = pth.split("/")
    formatted = "/".join([i for i in seperated[-3:] if i != "env"]) 
    return formatted

def check_endings(file):
    """
    seperate video files from non-video files. 
    Formats: mkv, mp4, avi, m4v
    """
    video_endings = [".mkv", ".mp4", ".avi", "m4v"]
    for ending in video_endings:
        if ending in file:
            return True

def movie(dirlist, filelist):
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

def main(*args):
    source = args[0][0]
    sorters = args[0][1]

    for root, dirs, file in os.walk(source):
        try:
            if root == source:
                #Check for video files in source and assume they are movies
                for i in file:
                    if check_endings(i):
                        #uncomment for test run:
                        #shutil.move(f"{root}" + f"{file}", sorters['movies']) 
                        logging.debug(f"{debug_format(source)}/{i} is being moved to {debug_format(sorters['movies'])}")
                        shutil.move(root + "/" + i, sorters["movies"])


            #TODO: Check other directories
            else:
                if not movie(dirs, file):
                    if len(dirs) >= 2:
                        #move nested dir
                        season_dir = root
                        logging.debug(f"{debug_format(season_dir)} is being moved to {debug_format(sorters['series'])}")
                        shutil.move(season_dir, sorters["series"])
                    else:
                        #move single season dir
                        logging.debug(f"{debug_format(root)} is being moved to {debug_format(sorters['series'])}")
                        shutil.move(root, sorters["series"])
                elif movie(dirs, file):
                    #move movie
                    logging.debug(f"{debug_format(root)} is being moved to {debug_format(sorters['movies'])}")
                    shutil.move(root, sorters['movies'])
        except shutil.Error as e:
            logging.info(e)

if __name__ == "__main__":
    main(args("./sorter.txt"))
