# Exercise 12: Find the last position of a given substring

data = input("str1 = ")
sub = input("Substring: ")
words = data.split()

pos = []
cnt = 0
id = 0
for word in words:
    id += len(word) + 1
    if word == sub:
        pos.append(id-len(word)-1)

    cnt += 1

# or,  index = str1.rfind("Emma")
print("Last occurance of ",sub," starts at index ",pos[-1])
