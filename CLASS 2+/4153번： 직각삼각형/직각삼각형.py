import sys

def input():
    return sys.stdin.readline().rstrip()

num_list = list(map(int, input().split()))

while(0 not in num_list):
    max_num = max(num_list)
    num_list.remove(max_num)
    a, b = num_list
    if a*a + b*b == max_num*max_num:
        print('right')
    else:
        print('wrong')
    num_list = list(map(int, input().split()))