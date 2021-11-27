num1 = int(input())
num2 = int(input())

if abs(num2 - num1) < 5:
    print("Invalid Input")
else:
    for i in range(num1, num2+1, 1):
        n = i**3-(3*i)-2
        if n%7==0:
            print(i)


