import os, sys
from posixpath import abspath

#Change working directory to script directory
abs = os.path.abspath(__file__)
dname = os.path.dirname(abs)
os.chdir(dname)

def args():
    """
    Resolves sys.argvs with the format: \n <source> movies:<movie folder path> series:<series folder path>
    """
    help_message = "Needs to have sorter.txt in script directory\ntext format:\n <source> <category>:<destination path> <category>:<destination path>"
    try:
        with open("./sorter.txt", 'r') as f:
            #TODO: use regex to test args in .txt file
            args = f.readlines()
            source, split1, split2 = args[0].split(" ")#maybe find a more elegant way to get rid of the space
            cat1, pat1, cat2, pat2 = split1.split(":")[0], split1.split(":")[1], split2.split(":")[0], split2.split(":")[1]
            if "\n" in pat2:
                pat2 = pat2[:-1]
        return [source, cat1, pat1, cat2, pat2]
    except FileNotFoundError:
        print(help_message)
    if sys.argv[1] == "-h" or "-help":
        print(help_message)
    else:
        print(help_message)
        quit()

def main(*args):
    print(type(args))

print(type(args()))
print(len(args()))
main(args)