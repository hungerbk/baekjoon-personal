import sys

def input():
    return sys.stdin.readline().rstrip()

n = int(input())
position = []

for _ in range(n):
    position.append(list(map(int,input().split())))

for x, y in sorted(position, key=lambda x: (x[0], x[1])):
    print(x , y)
