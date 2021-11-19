# Exercise 18: Replace each special symbol with # in the following string
import string

data = input("str1 = ")

newstr = ''
# for alpha in data:
#
#     if alpha.isspace():
#         newstr += alpha
#
#     elif not alpha.isalpha():
#         newstr += '#'
#
#     else:
#         newstr += alpha

for char in string.punctuation:
    print(char)
    data = data.replace(char, "#")


print(data)
