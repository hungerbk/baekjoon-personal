import sys

def input():
  return sys.stdin.readline().rstrip()

n, m = map(int, input().split())
arr = [i for i in range(1, n+1)]
answer = []
target = m - 1
while arr:
    target %= len(arr)
    answer.append(arr[target])
    arr.pop(target)
    target += m - 1 
print('<'+', '.join(map(str,answer))+'>')