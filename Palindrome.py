def palindrome(input):
    flag = False
    for i in range(0, len(input)):
        if input[i] != input[len(input)-1-i]:
            flag = False
            break
        else:
            flag = True
    return flag
