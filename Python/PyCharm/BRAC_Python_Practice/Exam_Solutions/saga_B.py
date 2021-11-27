data = input()

ln = []
for item in data.split():
    ln.append(len(item))

for item in data.split():
    print(item[0]+str(len(item)-2)+item[len(item)-1], end=' ')

