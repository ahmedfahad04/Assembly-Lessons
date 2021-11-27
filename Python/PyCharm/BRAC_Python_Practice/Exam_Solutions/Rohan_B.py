data = input()

letter = []
for alpha in data:
    letter.append(alpha)

lettercnt = []
for item in letter:
    cnt = 0
    for alpha in data:
        if alpha.lower() == item.lower():
            cnt+=1

    lettercnt.append(cnt)

ans = []
for i in range(0,len(lettercnt)):
    if lettercnt[i]%2!=0:
        if letter[i] not in ans:
            ans.append(letter[i])

print(ans)