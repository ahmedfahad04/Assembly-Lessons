# Exercise 2: Append new string in the middle of a given string

str1 = input("Main String: ")
str2 = input("String to be inserted: ")

l = int(len(str1))
mid = str1[:(l//2)]
lst = str1[(l//2):]
ans = mid + str2 + lst

print(ans)