import sys

def input():
  return sys.stdin.readline().rstrip()

n = int(input())
score_list = list(map(int, input().split()))

max_score = max(score_list)

answer = sum([i/max_score*100 for i in score_list])/n

print(answer)