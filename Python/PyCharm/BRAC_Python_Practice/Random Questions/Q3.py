# Question-3:
# Write a python function that takes a number(integer) as an argument and 
# generates a pattern according to the outputs shown below.
# ================================================
# Function call 1:
# function_name(4)
# Sample Output 1:
# AAAA
# #A**A
# ##A**A
# ###AAAA

usr_in = int(input())

print(usr_in*'A')
l1 = 1
for run in range(usr_in-2):    
    print(l1*'#',end='')
    print('A', end='')
    l1+=1

    print((usr_in-2)*'*', end='')
    print('A')

print(l1*'#'+usr_in*'A')