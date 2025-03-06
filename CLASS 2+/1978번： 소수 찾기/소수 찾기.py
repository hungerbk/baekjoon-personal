import sys, math

def input():
    return sys.stdin.readline().rstrip()

def is_prime(x):
    # 2부터 제곱근까지의 모든 수를 확인
    for i in range(2, int(math.sqrt(x))+1):
        # 나누어 떨어지는 수가 있다면 False 리턴
        if x % i == 0:
            return False
    return True

n = input()
num_list = map(int, input().split())
answer = 0

for i in num_list:
    if i > 1 and is_prime(i):
        answer += 1

print(answer)