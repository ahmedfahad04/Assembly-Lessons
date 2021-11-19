# Exercise 10: Write a program to count occurrences of all characters within a string

data = input("str1 = ")
letters = dict()

for letter in data:
    cnt = data.count(letter)
    letters[letter] = cnt

print(letters)