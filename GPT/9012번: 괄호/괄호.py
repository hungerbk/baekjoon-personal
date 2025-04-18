import sys

def input():
  return sys.stdin.readline().rstrip()

n = int(input())

for _ in range(n):
    str = input()
    stack = []
    for i in str:
        if i == '(':
            stack.append('(')
        else:
            if len(stack) == 0:
                print('NO')
                break
            else:
                stack.pop()
    else:
        if len(stack) == 0:
            print('YES')
        else:
            print('NO')