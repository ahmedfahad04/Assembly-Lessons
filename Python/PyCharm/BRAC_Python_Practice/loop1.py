n = 5
j = 0
for i in range(1, 2*n):     # 2n-1-----> 2n (i<=2n-1)
    if i<n:
        print(i, end='')
    else:
        print(n-j, end='')
        j += 1

#1234
#54321