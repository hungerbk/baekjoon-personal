import sys
import itertools

def input():
  return sys.stdin.readline().rstrip()

n ,m = map(int, input().split())
for i in itertools.permutations(range(1, n+1), m):
    print(' '.join(map(str, i)))