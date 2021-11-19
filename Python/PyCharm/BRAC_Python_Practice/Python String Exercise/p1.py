# Exercise 1A: Create a string made of the first, middle and last character

data = input("Str1 = ")

s1 = data[0]
s2 = data[int(len(data)//2)]
s3 = data[int(len(data))-1]

print(s1 + s2 + s3)