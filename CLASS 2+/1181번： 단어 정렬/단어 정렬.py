import sys

def input():
  return sys.stdin.readline().rstrip()

n = int(input())
word_set = set()

for i in range(n):
  word_set.add(input())

sorted_list = sorted(word_set)

for i in sorted(sorted_list, key= lambda x: len(x)):
  print(i)