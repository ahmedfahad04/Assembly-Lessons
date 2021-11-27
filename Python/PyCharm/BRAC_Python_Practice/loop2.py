
# a b z
#   a b z
#     a b z

# z = a(0) + b(1) = 1
# z = a(1) + b(1->z) = 2
# z = a(1) + b(2->z)

a = 0
b = 1

print(a, end=' ')

n = 7
# 0 1 1 2 3 5 8 13

for i in range(n):
    z = a + b
    a = b
    b = z

    print(a,end=' ')


