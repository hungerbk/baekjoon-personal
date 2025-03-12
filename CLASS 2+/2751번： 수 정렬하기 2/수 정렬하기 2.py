import sys

def input():
    return sys.stdin.readline().rstrip()

n = int(input())
num_list = []

for _ in range(n):
    num_list.append(int(input()))

for i in sorted(num_list):
    print(i)