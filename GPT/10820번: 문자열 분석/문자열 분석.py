import sys

# def input():
#   return sys.stdin.readline().rstrip()

# # 소문자, 대문자, 숫자, 공백 순서
# string = input()
# answer = [0] * 4
# for i in string:
#     if i.islower():
#         answer[0] += 1
#     elif i.isupper():
#         answer[1] += 1
#     elif i.isdigit():
#         answer[2] += 1
#     else:
#         answer[3] += 1
# print(' '.join(map(str, answer)))

for line in sys.stdin:
    answer = [0, 0, 0, -1]
    for i in line:
        if i.islower():
            answer[0] += 1
        elif i.isupper():
            answer[1] += 1
        elif i.isdigit():
            answer[2] += 1
        else:
            answer[3] += 1
    print(' '.join(map(str, answer)))