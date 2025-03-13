import sys

def input():
    return sys.stdin.readline().rstrip()

n = int(input())
stack = []

for _ in range(n):
    keyword = input()
    if 'push' in keyword:
        _, number = keyword.split()
        stack.append(int(number))
    elif keyword == 'pop':
        if len(stack) > 0:
            print(stack.pop())
        else:
            print(-1)
    elif keyword == 'size':
        print(len(stack))
    elif keyword == 'empty':
        if len(stack) > 0:
            print(0)
        else:
            print(1)
    else:
        if len(stack) > 0:
            print(stack[-1])
        else:
            print(-1)