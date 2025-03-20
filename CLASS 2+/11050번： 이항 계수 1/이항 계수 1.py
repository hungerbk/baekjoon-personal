import sys, math

def input():
    return sys.stdin.readline().rstrip()

n, k = list(map(int, input().split()))


print(math.factorial(n) // (math.factorial(k) * math.factorial(n-k)))
