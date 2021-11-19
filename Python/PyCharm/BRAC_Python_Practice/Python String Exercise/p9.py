# Exercise 8: Find all occurrences of a substring in a given string by ignoring the case

data = input("str1 = ")
words = data.split()

ans = dict()
data = data.lower()

for sub in words:
   cnt = data.count(sub.lower())
   ans[str(sub)] = cnt

given_substr = 'USA'
for key, val in ans.items():
    if key.lower() == given_substr.lower():
        print("The " + given_substr + " count is: " + str(val))

