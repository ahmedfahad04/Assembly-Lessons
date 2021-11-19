# Exercise 15: Remove special symbols / punctuation from a string
import string

data = input("str1 = ")
newstr = ''

# for i in data:
#     if i.isalpha(): newstr+=i
#     elif i.isspace(): newstr+=i

new_str = data.translate(str.maketrans('', '', string.punctuation))
print(new_str)