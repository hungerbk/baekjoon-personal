import sys

def input():
    return sys.stdin.readline().rstrip()

n, k = map(int, input().split())
arr = [i+1 for i in range(n)]
answer = []
tmp = 0

while len(arr) > 0:
    tmp += k - 1
    if tmp >= len(arr):
        tmp %= len(arr)

    answer.append(arr.pop(tmp))

formatted_string = '<' + ', '.join(map(str, answer)) + '>'

print(formatted_string)
