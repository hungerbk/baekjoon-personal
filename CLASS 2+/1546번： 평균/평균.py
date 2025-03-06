import sys

def input():
  return sys.stdin.readline().rstrip()

n = int(input())

grade_list = list(map(int, input().split()))
max_grade = max(grade_list)

print(sum([x/max_grade*100 for x in grade_list])/n)

