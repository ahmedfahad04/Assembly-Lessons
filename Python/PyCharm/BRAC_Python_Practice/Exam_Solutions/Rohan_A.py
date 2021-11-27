num = int(input())

days = ['Tuesday', 'Saturday']

val = num//7 * 2

print("He can read " + str(val) + " books")
for i in range(1,val+1):
    if i%2==1: print("Book " + str(i) + " on " + "Tuesday")
    else: print("Book " + str(i) + " on " + "Saturday")