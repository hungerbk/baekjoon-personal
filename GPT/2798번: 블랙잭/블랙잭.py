import sys
import itertools

def input():
  return sys.stdin.readline().rstrip()

# N, M = map(int, input().split())
# arr = list(map(int, input().split()))
# three_card = list(itertools.combinations(arr, 3))
# possible_list = []

# for i in three_card:
#     if sum(i) == M:
#         print(M)
#         break
#     elif sum(i) < M:
#         possible_list.append(sum(i))
# else:
#     print(max(possible_list))    

n, m = map(int, input().split())
card_list = list(map(int, input().split()))
answer = 0

for i in list(itertools.combinations(card_list, 3)):
    if sum(i) <= m:
        answer = max(answer, sum(i))

print(answer)