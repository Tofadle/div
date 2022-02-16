#! python3
#hex quiz - quizzes hexadecimal numbers from 0 to a user supplied number
import random

correct = 0
#quiz from hex to decimal
def hex2dec(max, correct, numrounds):
        for round in range(0, numrounds):
            num = random.randint(0,max)
            answer = input(f"What is {hex(num)} in decimal?\n")
            if int(answer) == num:
                print("That's correct!")
                correct += 1
            else:
                print("That's unfortunately not the right answer.")
        return correct

#quiz from decimal to hex
def dec2hex(max, correct, numrounds):
    for round in range(0, numrounds):
        num = random.randint(0,max)
        answer = input(f"What is {num} in hexadecimal?\n(remember 0x- prefix and small letters)\n")
        if answer == hex(num):
            print("That's correct!")
            correct += 1
        else:
            print("That's unfortunately not the right answer.")
    return correct



#TODO: Display welcome message
def game(correct):
    print("Welcome to the hexadecimal quiz!")
    default = input("Type 'default' (or 'd') for the default game or ENTER to customize\n")
    #defaul is max 50 and 10 questions
    if default == "default" or default == 'd':
        hex2dec(50, correct, 10)
        print(f"Thank you for playing!\nYou got {correct}/10 right answers")
    #Ask for type of quiz, how many questions, and how many numbers, and game-mode
    else:
        hexOrDec = input("Which type of quiz do you want?\nInput format: 'hex2dec' OR 'dec2hex'\n")
        numrounds = int(input("How many questions do you want?\n"))
        max = int(input("What's the highest number you want to be quizzed on?\n")) + 1

    if hexOrDec == "hex2dec":
        hex2dec(max, correct, numrounds)
        print(f"You got {correct}/{numrounds}!")
    elif hexOrDec == "dec2hex":
        dec2hex(max, correct, numrounds)
        print(f"You got {correct}/{numrounds}!")

    newRound = input("Play again? y/n\n")
    if newRound == "y":
        game(0)
    else:
        print("Okay, bye")

game(0)
