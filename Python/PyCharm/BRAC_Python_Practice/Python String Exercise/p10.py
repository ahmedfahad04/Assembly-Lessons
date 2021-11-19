# Exercise 9: Calculate the sum and average of the digits present in a string

data = input("str1 = ")

avg = 0
cnt = 0
for alpha in data:
    if alpha.isdigit():
        cnt += 1
        avg += int(alpha)

print("Sum is: " + str(avg) + " Average is: " + str(avg/cnt) )

