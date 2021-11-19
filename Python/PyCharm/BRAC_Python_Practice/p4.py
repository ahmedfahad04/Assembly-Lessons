# Exercise 3: Create a new string made of the first, middle, and last characters of each input string

data = input("Str1 = ")

s1 = data[0]
s2 = data[int(len(data)//2)]
s3 = data[int(len(data))-1]

data2 = input("Str2 = ")

ss1 = data2[0]
ss2 = data2[int(len(data2)//2)]
ss3 = data2[int(len(data2))-1]

print(s1+ss1+s2+ss2+s3+ss3)