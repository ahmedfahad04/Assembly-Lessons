# Exercise 6: Create a mixed String using the following rules

data = input("str1 = ")
data2 = input("str2 = ")

newstr = ''
l1 = len(data)
l2 = len(data2)

if l1 > l2:
    for i in range(0, l2, 1):
        newstr += (data[i] + data2[l2 - i - 1])

    newstr += data[l2:]
else:
    for i in range(0, l1, 1):
        newstr += (data[i] + data2[l2 - i - 1])
    newstr += data2[:(l2-l1)]

print(newstr)
