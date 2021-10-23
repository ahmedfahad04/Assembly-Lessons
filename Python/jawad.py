def factorial(x):

    if x == 0 or x == 1:
        return 1

    else:
        return factorial(x-1)*x

def permutation(n, r):
    return factorial(n)//factorial(n-r)


def combination(n, r):
    return factorial(n)//(factorial(r)*factorial(n-r))


a = int(input("Enter the value of n: "))
b = int(input("Enter the value of r: "))

p = permutation(a, b)
c = combination(a, b)

print("P = %d" % p)
print("C = %d" % c)
