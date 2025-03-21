import sys

def input():
    return sys.stdin.readline().rstrip()

n ,m = map(int, input().split())

name_dict = {}
answer = []

for _ in range(n+m):
    name = input()
    name_dict[name] = name_dict.get(name, 0) + 1
    if name_dict[name] == 2:
        answer.append(name)

print(len(answer))
print('\n'.join(sorted(answer)))