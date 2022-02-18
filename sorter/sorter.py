#! python3
#Sorter - Sorts files from a source to two destination folders based on two respective categories, e.g. movies and tv shows or movies and pictures
import os, shutil, sys

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


#List the contents of the source folder
def main(source, cat1, pat1, cat2, pat2):    
    os.chdir(source)
    for item in os.listdir():
            sort = input(f"is {item} a {cat1} or {cat2}?\n--->{cat1}/{cat1[0]} or {cat2}/{cat2[0]} to sort\n(Any key to skip)\n> ")
            #sort in category 1
            if sort == f"{cat1}" or sort == f"{cat1[0]}":
                newpat1 = pat1 + "/" + item
                print(f"moving {item}...")
                shutil.move(item, newpat1)
                #sort in category 2
            elif sort == f"{cat2}" or sort == f"{cat2[0]}":
                newpat2 = pat2 + "/" + item
                shutil.move(item, newpat2)
                print(f"moving {item}")
            else:
                print(f"leaving {item}")

if __name__ == "__main__":
    one, two, three, four, five = args()
    main(one, two, three, four, five)