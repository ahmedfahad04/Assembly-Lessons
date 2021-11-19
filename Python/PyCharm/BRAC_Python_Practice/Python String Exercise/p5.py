# Exercise 4: Arrange string characters such that lowercase letters should come first

data = input("str1 = ")
low = ''
high = ''

for alpha in data:
    if alpha.islower():
        low += alpha
    else:
        high += alpha

print(low+high)