def bookIndex(arr):
    first = True
    output = ""
    for i in range(len(arr)-1):
        if arr[i+1] == (arr[i]+1):
            if first == True:
                output+=str(arr[i]) + " - "
            first = False
        else: 
            output+=str(arr[i]) + ", "
            first = True

    output += str(arr[len(arr) - 1])
    return output


print(bookIndex([1,5,6,7,10,13,17]))