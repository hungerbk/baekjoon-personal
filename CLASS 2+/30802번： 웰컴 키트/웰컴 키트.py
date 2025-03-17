import sys

def input():
    return sys.stdin.readline().rstrip()

n = int(input())
shirts = map(int, input().split())
t, p = map(int, input().split())

count_t = 0

for i in shirts:
    if i % t:
        count_t += 1
    count_t += i // t

count_p = n // p
rest_p = n % p

print(count_t)
print(count_p, rest_p)