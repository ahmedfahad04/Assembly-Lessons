# Exercise 1B: Create a string made of the middle three characters

data = input("Str1 = ")

l = int(len(data))
s1 = data[(l//2)-1]
s2 = data[(l//2)]
s3 = data[(l//2)+1]

print(s1+s2+s3)