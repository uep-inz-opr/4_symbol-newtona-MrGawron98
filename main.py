import math

def newton(n,k):
    return int(math.factorial(n)/(math.factorial(k)*math.factorial(n-k)))

numbers = input().split()

n = int(numbers[0])
k = int(numbers[1])

print(newton(n,k))

