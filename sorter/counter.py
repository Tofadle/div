from pathlib import Path
import os
import re
import pandas as pd

"""
This file doesn't really do much except give you an idea of which file endings should be included in autoSotert.
It was made primarily to recap some basic regex
"""

def file_ending_extractor():
    """
    Extract file endings from all files in directory
    """
    #If you make a lentest list and append all files, it will be exactly one element longer than the endings list
    #Find out why at some point
    f = open("path.txt", "r")
    #base_path = Path(f.readline())
    base_path = Path(f.readline().strip("\n"))
    f.close()
    print(base_path, type(base_path))
    format = re.compile(r'\.\w{3,4}$')
    endings = []
    for root, dir, file in os.walk(base_path):
        for i in file:
            mo = format.search(i)
            if mo is not None:
                endings.append(mo.group())
    return endings

def counter():
    endings = file_ending_extractor()
    df = pd.DataFrame(endings).value_counts()
    return df
    
    

if __name__ == "__main__":
    print(counter())