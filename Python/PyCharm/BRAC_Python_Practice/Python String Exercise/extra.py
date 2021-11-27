import string

data = input("str1 = ")

vowel = ['a', 'e', 'i', 'o', 'u']
v = 'aeiou'

vcnt = 0
pos = 0
ans = ''
posL = []
for alpha in data:

    if alpha in vowel:
        vcnt += 1
    elif vcnt < 3:

        vcnt = 0
    else:
        posL.append(pos-3)
        vcnt = 0
    pos += 1

j = 0
for i in range(0, len(data)):
    if i == posL[j]:
        for k in range(3):
            print('#',end='')
            i+=1
        j+=1
    else:
        print(data[i],end='')

