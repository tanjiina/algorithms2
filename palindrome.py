def palindrome(string):
    for i in range(len(string)//2)
        if string[i] != string[len(string) - i - 1]
            return False
    return True

print(palindrome("kayak"))
print(palindrome("hello"))