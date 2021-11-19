# Exercise 14: Remove empty strings from a list of strings

str_list = ["emma", "jon", "", "kelly", None, "eric", ""]
print("Orginal list of String")
print(str_list)

newl = []
for item in str_list:
    if item == None:
        continue
    if len(item) :
        newl.append(item)

    # or simple if item: newl.append(item)

print("After removing empty string")
print(newl)