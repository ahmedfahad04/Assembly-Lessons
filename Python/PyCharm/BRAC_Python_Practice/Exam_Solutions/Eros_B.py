num = int(input())

if num%2==1 and num > 2:
    sign = 1
    sum = 0
    signval = 1


    for i in range(1, num+1):
        if sign%3==0:
            signval = -1

        val = 1*signval
        for j in range(i,i+3):
            val *= j
            i += 1

        sum += val

        sign += 1

    print(sum)
else:
    print("Invalid Input")