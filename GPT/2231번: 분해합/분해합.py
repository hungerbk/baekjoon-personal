import sys
input = sys.stdin.readline

n = int(input())

for i in range(1, n):
        digit_sum = sum(map(int, str(i)))  # 자릿수 합
        if i + digit_sum == n:
            print(i)   # 가장 작은 생성자
            break
else:
    print(0)