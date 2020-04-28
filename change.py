def change(num):
    change = {"q": 0, "d": 0, "n": 0, "p": 0}

    if num >= 25:
        change["q"] = int(num/25)
        num %= 25
    if num >= 10:
        change["d"] = int(num/10)
        num %= 10
    if num >= 5:
        change["n"] = int(num/5)
        num %= 5
    if num >= 1:
        change["p"] = int(num/1)
        num %= 1
    return change

print(change(94))


def change2(num):
    change = {"q": 0, "d": 0, "n": 0, "p": 0}

    while (num > 0):
        if num >= 25:
            change["q"] += 1
            num -= 25
        elif num >= 10:
            change["d"] += 1
            num -= 10
        elif num >= 5:
            change["n"] += 1
            num -= 5
        else:
            change["p"] += 1
            num -= 1
    return change

print(change2(94))
