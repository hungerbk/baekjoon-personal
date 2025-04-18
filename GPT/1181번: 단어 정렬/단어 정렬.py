import sys

def input():
  return sys.stdin.readline().rstrip()

n = int(input())

str_list = set()

for _ in range(n):
  str_list.add(input())

for i in sorted(str_list, key=lambda x: (len(x), x)):
  print(i)