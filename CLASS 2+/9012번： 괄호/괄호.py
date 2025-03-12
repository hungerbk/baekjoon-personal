import sys

def input():
    return sys.stdin.readline().rstrip()

n = int(input())

for _ in range(n):
    count_list = []
    str_list = input()
    is_valid = True
    for i in str_list:
        if i == '(':
            count_list.append(1)
        else:
            if len(count_list) > 0:
                count_list.pop()
            else:
                print('NO')
                is_valid = False # str_list를 모두 탐색하지 않은 경우
                break

    if len(count_list) == 0 and is_valid: # str_list를 모두 탐색하고, 괄호쌍이 맞을 때
        print('YES')
    elif is_valid: # str_list를 모두 탐색했지만 괄호쌍이 맞지 않을 때
        print('NO')