import sys

def input():
  return sys.stdin.readline().rstrip()

n = input()
n_list = set(map(int, input().split()))
m = input()
m_list = map(int, input().split())

for i in m_list:
  if i in n_list:
    print(1)
  else:
    print(0)
  
# n_list가 set 상태가 아니면 시간초과가 발생
# 이전에도 풀었던 문제인데 왜 메모리가 다르게 나오는지는 모르겠다. 같은 코드인 것 같은디...
# 문제 이해가 안돼서 예전에 풀었던 거 다시 봄