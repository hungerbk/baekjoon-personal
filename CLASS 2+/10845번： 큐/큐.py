import sys

def input():
    return sys.stdin.readline().rstrip()

n = int(input())
queue = []

for _ in range(n):
    keyword = input()
    if 'push' in keyword:
        _, number = keyword.split()
        queue.append(int(number))
    elif keyword == 'pop':
        if len(queue) > 0:
            print(queue.pop(0))
        else:
            print(-1)
    elif keyword == 'size':
        print(len(queue))
    elif keyword == 'empty':
        if len(queue) > 0:
            print(0)
        else:
            print(1)
    elif keyword == 'front':
        if len(queue) > 0:
            print(queue[0])
        else:
            print(-1)
    else:
        if len(queue) > 0:
            print(queue[-1])
        else:
            print(-1)