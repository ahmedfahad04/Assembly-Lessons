# 1. Write a function in Python that will take a string text as 
# input from the user and returns the list of unique characters concatenated 
# with their ASCII value at the front and back side.
# ==================================================
# Sample Input:
# "pythonbook"

# Function Calling:
# function_name("pythonbook")

# Sample Output:
# ['112p112', '121y121', '116t116', 
# '104h104', '111o111', '110n110', '98b98', '107k107']

def myfunc(mystr):
    newstr = []

    rep_chars = []
    for i in range(0, len(mystr), 1):
        for j in range(i+1, len(mystr), 1):
            if mystr[i] == mystr[j]:
                rep_chars.append(mystr[i])

    for item in mystr:
        nstr = ''
        if item not in rep_chars:
            nstr += str(ord(item))
            nstr += item
            nstr += str(ord(item))
            newstr.append(nstr)

    return newstr

print(myfunc('pythonbook'))