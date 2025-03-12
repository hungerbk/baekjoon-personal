import sys
from itertools import combinations

def input():
    return sys.stdin.readline().rstrip()

n, m = map(int, input().split())
card_list = list(map(int, input().split()))
answer = 0

for i in list(combinations(card_list, 3)):
    if sum(i) <= m:
        answer = max(answer, sum(i))

print(answer)