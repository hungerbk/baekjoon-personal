import sys

def input():
  return sys.stdin.readline().rstrip()

n = int(input())

for _ in range(n):
    str = input()
    answer = []
    for i in range(len(str)):
        if str[i] == 'X':
            answer.append(0)
        else:
            if i == 0:
                answer.append(1)
            else:
                answer.append(answer[i-1] + 1)
    print(sum(answer))