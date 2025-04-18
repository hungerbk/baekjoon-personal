import sys

def input():
  return sys.stdin.readline().rstrip()

n = int(input())
people = [list(map(int, input().split())) for _ in range(n)]

ranks = []

for i in range(n):
    count = 0
    for j in range(n):
        if i == j:
            continue
        # j가 i보다 덩치가 더 크면
        if people[j][0] > people[i][0] and people[j][1] > people[i][1]:
            count += 1
    ranks.append(count + 1)

print(' '.join(map(str, ranks)))
