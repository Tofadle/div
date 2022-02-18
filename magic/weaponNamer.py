#weaponNamer.py - for naming weapons with the trinket in the magic shop
import random

#Open the different .txt files and iterate over the contents, making three lists
def listMaker(file):
    wordListNewline = []
    wordList = []
    rawWords = open(file, 'r', newline='')#Why doesn't newline='' do anything?
    for word in rawWords:
        wordListNewline.append(word)
    for word in wordListNewline:
        if word != wordListNewline[len(wordListNewline)-1]:
            wordList.append(word[:-1])
        else:
            wordList.append(word)
    return wordList

positiveAdj = listMaker("positive_adjectives.txt")
negativeAdj = listMaker("negative_adjectives.txt")
weaponList = listMaker("weaponlist.txt")

#randomly join together positive or negative adjectives with the weaponlist
def weaponNamer(pos, neg, wep):
    coinFlip = random.randint(0,1)
    if coinFlip == 0:
        adjective = pos[random.randint(0,len(pos)-1)].capitalize()
    else:
        adjective = neg[random.randint(0, len(neg)-1)].capitalize()
    
    word = adjective + " " + wep[random.randint(0,len(wep)-1)]
    return word

def priceGenerator(weaponName):
    if weaponName.split(" ")[0].lower() in positiveAdj:
        weaponPrice = random.randint(15, 50)
    else:
        weaponPrice = random.randint(1, 14)
    return weaponPrice

def damageGenerator(weaponName):
    goodtier = ["Claymore", "Longsword", "Broadsword", "Halberd", "Falchion", "Battle axe"]
    if weaponName.split(" ")[1] in goodtier:
        weaponDmg = random.randint(20,30)
    elif weaponName.split(" ")[1] == "Longship":
        weaponDmg = "eternal"
    else:
        weaponDmg = random.randint(1, 20)
    return weaponDmg

""" weaponName = weaponNamer(positiveAdj, negativeAdj, weaponList)
print(f"\t\t**GENERATED WEAPON**\n\n~-*\t~-*\t{weaponName}\t*-~\t*-~\n")
print(f"value: {priceGenerator(weaponName)}")
print(f"damage: {damageGenerator(weaponName)}")
 """