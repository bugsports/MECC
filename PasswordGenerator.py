import random
import string

def inputNum(message): #validates user input as numerical for password length
    while True:
        try:
            userInput = int(input(message))
        except ValueError:
            print("Enter a number and try again.")
            continue
        else:
            return userInput
            break

def boolInput(message):
    userInput = input(message)
    if userInput in ('Y', 'y'):
        return True
    elif userInput in ('N', 'n'):
        return False

strLw = string.ascii_lowercase
strUp = string.ascii_uppercase
strNum = string.digits
strPunc = string.punctuation

while True:
    pLen = inputNum("Enter length of the password: ")
    useLw = boolInput("Use lowercase letters [Y/N]: ")
    useUp = boolInput("Use uppercase letters [Y/N]: ")
    useNum = boolInput("Use numbers [Y/N]: ")
    usePunc = boolInput("Use special characters [Y/N]: ")

    pw = []
    if useLw == True:
        pw.extend(list(strLw))
    if useUp == True:
        pw.extend(list(strUp))
    if useNum == True:
        pw.extend(list(strNum))
    if usePunc == True:
        pw.extend(list(strPunc))
    
    try:
        print("Generated password:", "".join(random.sample(pw, pLen)))
    except ValueError:
        print("You must use at least one condition")
        continue
    else:
        break

