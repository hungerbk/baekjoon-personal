import sys

def input():
  return sys.stdin.readline().rstrip()

n = int(input())
card_list = set(map(int, input().split()))
m = int(input())
check_list = list(map(int, input().split()))
# answer = []

for i in check_list:
    print(1 if i in card_list else 0, end=' ')

# for i in check_list:
#     if i in card_list:
#         answer.append(1)
#     else:
#         answer.append(0)

# for i in answer:
#     print(i, end=' ')
# print(' '.join(map(str, answer)))