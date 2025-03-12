import sys, math

def input():
    return sys.stdin.readline().rstrip()

n, m = map(int, input().split())

# 파이썬 내장 함수 > 내장함수가 더 빠름
print(math.gcd(n, m))
print(math.lcm(n, m))

# 유클리드 호제법
def gcd(n, m):
    while m > 0:
        n, m = m, n % m
    return n

def lcm(n, m):
    return n * m // gcd(n, m)

print(gcd(n, m))
print(lcm(n, m))