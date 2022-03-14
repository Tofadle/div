#! python3
#Sorter - Sorts files from a source to two destination folders based on two respective categories, e.g. movies and tv shows or movies and pictures
import os, shutil, sys

#Change working directory to script directory
abspath = os.path.abspath(__file__)
dname = os.path.dirname(abspath)
os.chdir(dname)


def args():
    help_message = "-file, -f sorter.txt to open from file\ntext format:\n <source> <category>:<path> <category>:<path>"
    arglist = []

    if sys.argv[1] == "-f" or "-file":
        try:
            with open("./sorter.txt", 'r') as f:
                #TODO: use regex to test args in .txt file
                args = f.readlines()
                source, split1, split2 = args[0].split(" ")#maybe find a more elegant way to get rid of the space
                cat1, pat1, cat2, pat2 = split1.split(":")[0], split1.split(":")[1], split2.split(":")[0], split2.split(":")[1]
                if "\n" in pat2:
                    pat2 = pat2[:-1]
            return source, cat1, pat1, cat2, pat2
        except FileNotFoundError:
            print(help_message)
    elif sys.argv[1] == "-h" or "-help":
        print(help_message)
    else:
        print(help_message)
        quit()


#List the contents of the source folder
#TODO: Figure out a way to display progress when moving files
def main(source, cat1, pat1, cat2, pat2):    
    os.chdir(source)
    for item in os.listdir():
            sort = input(f"Sorting from {source}.\nis {item} a {cat1} or {cat2}?\n---> type: {cat1}/{cat1[0]} or {cat2}/{cat2[0]} to sort\n(Any key to skip)\n> ")
            #sort in category 1
            #TODO: Make sure shutil.Error: Destination path already exists doesn't happen
            if sort == f"{cat1}" or sort == f"{cat1[0]}":
                newpat1 = pat1 + "/" + item
                print(f"moving {item}...")
                shutil.move(item, newpat1)
                #sort in category 2
            elif sort == f"{cat2}" or sort == f"{cat2[0]}":
                newpat2 = pat2 + "/" + item
                print(f"moving {item}")
                shutil.move(item, newpat2)
            else:
                print(f"leaving {item}")

if __name__ == "__main__":
    one, two, three, four, five = args()
    main(one, two, three, four, five)