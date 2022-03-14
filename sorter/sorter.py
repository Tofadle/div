#! python3
#Sorter - Sorts files from a source to two destination folders based on two respective categories, e.g. movies and tv shows or movies and pictures
import os, shutil, sys

#Change working directory to script directory
abspath = os.path.abspath(__file__)
dname = os.path.dirname(abspath)
os.chdir(dname)


def args():
    """
    Resolves sys.argvs with the format: \n <source> <category>:<destination path> <category>:<destination path>
    """
    help_message = "-file, -f sorter.txt to open from file\ntext format:\n <source> <category>:<destination path> <category>:<destination path>"
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
    print("Sorting from {source}.\n")
    for item in os.listdir():
            sort = input(f"is {item} a {cat1} or {cat2}?\n---> type: {cat1}/{cat1[0]} or {cat2}/{cat2[0]} to sort\n(Any key to skip)\n> ")
            #sort in categories
            if sort.startswith(cat1[0]):
                newpat = pat1 + "/" + item
            elif sort.startswith(cat2[0]):
                newpat = pat2 + "/" + item
            else:
                continue
            if os.path.isdir(newpat):
                print(f"{item} already exists at Destination. Overwrite? y/n")
                overwrite = input("\n> ")
                if overwrite.lower() == "y":
                    shutil.rmtree(newpat, ignore_errors=True)
                    shutil.move(item, newpat)
                else:
                    print(f"leaving {item}")        
                    print(f"moving {item}...")
            else:
                shutil.move(item, newpat)


if __name__ == "__main__":
    one, two, three, four, five = args()
    main(one, two, three, four, five)