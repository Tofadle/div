import os, sys, args
from posixpath import abspath

#Change working directory to script directory
abs = os.path.abspath(__file__)
dname = os.path.dirname(abs)
os.chdir(dname)



def main():
    pass
    
    #for root, dirs, file in os.walk()
    #pass

if __name__ == "__main__":
    args.args("./sorter.txt")
