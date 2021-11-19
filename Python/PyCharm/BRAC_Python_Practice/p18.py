# Exercise 17: Find words with both alphabets and numbers

data = input("str1 = ").split()

ans = []
for word in data:
    if word.isalpha():
        continue
    else:
        ans.append(word)

print(*ans, sep='\n')
