data = input().split(',')
ans = []
num = ''
for item in data:
    for alpha in item:
        if alpha.isdigit():
            num += alpha
    ans.append(num)
    num = ''

print(ans)
