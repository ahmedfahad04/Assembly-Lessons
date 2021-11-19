# Exercise 16: Removal all characters from a string except integers

data = input("str1 = ")
words = data.split()
newstr = ''

for i in words:
    if i.isnumeric():
        newstr += i

print(newstr)