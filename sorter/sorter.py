#! python3
#Sorter - sorts movies and TV shows into corresponding folders for plex media server
import os
from os import path
import shutil
import sys


    
    


#[python3, sorter.py, <source>, <category:path>, <category:path>][4]
#Add functionality for a flag -f which reads arguments from a .txt file in the same directory
def args():
    usage_message = "\nUsage:\npython3 sorter.py <source> <category>:<path> <category>:<path>\n\n-help, -h for help"
    help_message = "-file, -f <sorter.txt> to open from file\ntext format:\n" + usage_message 
    arglist = []

    if len(sys.argv) == 4:
        source, cat1, pat1, cat2, pat2 = sys.argv[2], sys.argv[3].split(":")[0], sys.argv[3].split(":")[1],
        sys.argv[4].split(":")[0], sys.argv[4].split(":")[1]
        return source, cat1, pat1, cat2, pat2
    elif sys.argv[1] == "-f" or "-file":
        try:
            with open("sorter.txt", 'r') as f:
                #TODO: use regex to test args in .txt file
                args = f.readlines()
                source, split1, split2 = args[0].split(" ")#maybe find a more elegant way to get rid of the space
                cat1, pat1, cat2, pat2 = split1.split(":")[0], split1.split(":")[1], split2.split(":")[0], split2.split(":")[1]
            return source, cat1, pat1, cat2, pat2
        except FileNotFoundError:
            print(help_message)
    elif sys.argv[1] == "-h" or "-help":
        print(help_message)
    else:
        print(usage_message)
        quit()


#List the contents of the Downloads folder
def main(source, cat1, pat1, cat2, pat2):    
    os.chdir(source)
    for item in os.listdir():
            #moved = source + "/" +  item
            sort = input(f"is {item} a {cat1} or {cat2}?\n")
            if sort == f"{cat1}":
                newpat1 = pat1 + "/" + item
                #if not os.path.isdir(pat1):
                    #What happens if the movie isnt a dir?
                print(f"moving {item}...")
                shutil.move(item, newpat1)
                #else:
                    #continue
            elif sort == f"{cat2}":#!This doesn't move the file at all
                #if not os.path.isdir(pat2):
                newpat2 = pat2 + "/" + item
                shutil.move(item, newpat2)
                print(f"moving {item}")
                #else:
                    #continue
            else:
                print(f"leaving {item}")

if __name__ == "__main__":
    one, two, three, four, five = args()
    main(one, two, three, four, five)