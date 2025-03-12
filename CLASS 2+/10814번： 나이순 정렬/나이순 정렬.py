import sys

def input():
    return sys.stdin.readline().rstrip()

n = int(input())
user_list = []

for i in range(n):
    user_list.append((i, input().split()))

sorted_user_list = sorted(user_list, key=lambda x: (int(x[1][0]), x[0]))

for i in sorted_user_list:
    a, b = i
    print(' '.join(b))