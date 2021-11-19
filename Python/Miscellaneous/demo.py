x = int(input("Enter a number: "))

y = str(x)

a,b = y.split("0")

sum1 = 0
for digit in a:
    sum1 += int(digit)


sum2 = 0
for digit in b:
    sum2 += int(digit)

print(sum1-sum2)
    



