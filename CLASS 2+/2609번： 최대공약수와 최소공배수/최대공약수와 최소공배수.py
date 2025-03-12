import sys, math

def input():
    return sys.stdin.readline().rstrip()

n, m = map(int, input().split())

print(math.gcd(n, m))
print(math.lcm(n, m))