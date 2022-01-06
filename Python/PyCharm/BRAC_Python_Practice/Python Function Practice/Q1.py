# Question-1:
# Write a Python program that takes an integer Y from 10 to 20 inclusive as 
# an input from the user and prints “The user entered Y”. Then the program 
# should print a series of numbers, starting at Y as the first term of the 
# series and then the following terms will be according to the formula 
# Y = (2 x Y) - 5 until Y is less than 100. If the user enters an integer that is 
# beyond the range mentioned above, your program should print “Wrong input”.

# ====================================================
# Sample Input 1:
# 10
# Sample Output 1:
# The user entered 10
# 10, 15, 25, 45, 85

num = int(input("Enter a nubmer: "))

if num>=20 or num<=10:
    print("Wrong input")
else:
    ans = num
    print("The user entered ", ans)
    while ans < 100:
        print(ans, end=', ')
        ans = 2*ans - 5