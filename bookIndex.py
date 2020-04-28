def bookIndex (arr):
    counter = 0
    output = ""
    for i in range (len(arr)-1):
        if arr[i+1] == (arr[i]+1):
            if counter == 0:
                output += str(arr[i]) + "-"
            counter += 1
        else:
            output += str(arr[i]) + ", "
            counter = 0
            # if counter == 1:
            #     output += str(arr[i]) + ", "
    output += str(arr[i])
    return output
    
print(bookIndex([1,5,6,7,10,13,14]))