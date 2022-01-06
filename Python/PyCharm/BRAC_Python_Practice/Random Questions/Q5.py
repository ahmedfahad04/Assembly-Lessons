# Question-3:
# Write a python function that takes a string as an argument and returns a 
# new string by replacing all occurrences of repetitive characters with "#".
# [You are NOT allowed to use count(), sort(), sorted()]
# ================================================
# Function call1:
# function_name("blueberry")
# Sample Output 1:
# #lu#####y
# Explanation 1:
# The argument string had more than one occurrence of “b”, “e” and “r”. Thus 
# they are replaced with "#".

def myfunc(mystr):
    newstr = ''

    rep_chars = []
    for i in range(0, len(mystr), 1):
        for j in range(i+1, len(mystr), 1):
            if mystr[i] == mystr[j]:
                rep_chars.append(mystr[i])

    for item in mystr:
        if item in rep_chars:
            newstr += "#"
        else:
            newstr += item

    return newstr

print(myfunc('pythonbook'))