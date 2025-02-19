# import sys

# def input():
#   return sys.stdin.readline().rstrip()

# n = int(input())
# word_set = set()

# for i in range(n):
#   word_set.add(input())

# sorted_list = sorted(word_set)

# for i in sorted(sorted_list, key= lambda x: len(x)):
#   print(i)

import sys

def input():
  return sys.stdin.readline().rstrip()

n = int(input())
answer = set()

for _ in range(n):
  answer.add(input())

answer = sorted(answer, key=lambda x: (len(x), x))

for i in answer:
  print(i)