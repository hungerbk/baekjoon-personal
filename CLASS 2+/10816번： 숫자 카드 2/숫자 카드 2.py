import sys

def input():
    return sys.stdin.readline().rstrip()

n = input()
card_list = input().split()
m = input()
check_list = input().split()
answer = []

# 시간초과
# for i in check_list:
#     answer.append(str(card_list.count(i)))

# print(' '.join(answer))

count_dict = {}
for i in card_list:
    count_dict[i] = count_dict.get(i, 0) + 1

for i in check_list:
    answer.append(str(count_dict.get(i, 0)))

print(' '.join(answer))