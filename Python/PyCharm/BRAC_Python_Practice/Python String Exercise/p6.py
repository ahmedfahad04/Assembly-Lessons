# Exercise 5: Count all letters, digits, and special symbols from a given string

data = input("str1 = ")

letter = 0
digit = 0
symbol = 0

for alpha in data:

    if alpha.isdigit():
        digit += 1
    elif alpha.isalpha():
        letter += 1
    else:
        symbol += 1

print("Chars = " , letter)
print("Digits = " , digit)
print("Symbol = " , symbol)