# Exercise 7: String characters balance Test

s1 = input("s1 = ")
s2 = input("s2 = ")

flag = False
for char in s1:
    if char in s2:
        flag = True
    else:
        flag = False
        break

print(flag)

