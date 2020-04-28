# checks if string of parentheses is valid 
def checkValidation(string):
    counter = 0
    for i in range(len(string)):
        if string[i] == "(":
            counter += 1
        elif string[i] == ")":
            counter -= 1
        else:
            continue
        if counter < 0:
            return False

    if counter == 0:
        return True
    else:
        return False

print(checkValidation("((((()))))"))
print(checkValidation("(())(())(()))"))