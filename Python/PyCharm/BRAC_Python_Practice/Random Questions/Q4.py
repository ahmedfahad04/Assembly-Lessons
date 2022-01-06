# Write a python code that will take a string as an input from the user where 
# multiple numbers are separated by commas. Make a list of numbers using that 
# string & print it. Then create a new list consisting only of the numbers 
# which are greater than the average of the previous list. Print the two 
# lists as shown and then if the average of all the elements in the new list 
# is greater than  the SECOND highest of the FIRST list then your program 
# should print “It’s a miracle!!!” otherwise your program should print “Just 
# another normal day!!!”
# ================================================
# Sample Input 1:
# 10, 12, 2, 17, 14

# Sample Output 1:
# Input list: [10, 12, 2, 17, 14]
# Average of input list: 11.0
# New list: [12, 17, 14]
# Average of the new list: 14.333333333333334
# The 2nd highest number from the list1: 14
# It’s a miracle!!!

num = input().split(', ')
num = [int(i) for i in num]
s = 0

for i in num:
    s += i

avg = s/len(num)
ns = 0

newls = []
for i in num:
    if i > avg:
        newls.append(i)
        ns += i
    
navg = ns/len(newls)

sorted_list = sorted(num)

print("Input list: ", num)
print("Average of input list: ", avg)
print("New list: ", newls)
print("Average of the new list: ", navg)
print("The 2nd highest number from the list1: ", sorted_list[-2])
print("It's a miracle") if navg > sorted_list[-2] else print("Just another normal day")