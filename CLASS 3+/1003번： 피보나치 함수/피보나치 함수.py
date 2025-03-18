# import sys

# def input():
#     return sys.stdin.readline().rstrip()

# n = int(input())

# def fibonacci(n, num_dict): 
#     if n == 0:
#         num_dict[0] = num_dict.get(0, 0) + 1
#         return 0
#     elif n == 1:
#         num_dict[1] = num_dict.get(1, 0) + 1
#         return 1
#     else:
#         return fibonacci(n-1, num_dict) + fibonacci(n-2, num_dict)

# for _ in range(n):
#     answer = {}
#     fibonacci(int(input()), answer)
#     print(answer.get(0,0), answer.get(1,0))
    
import sys

def input():
    return sys.stdin.readline().rstrip()

# 40까지 미리 저장할 DP 테이블 생성 (N의 범위가 0<=N<=40)
dp = [(0, 0)] * 41  # (0이 호출된 횟수, 1이 호출된 횟수)
dp[0] = (1, 0)  # fibonacci(0) → 0이 1번, 1이 0번 호출
dp[1] = (0, 1)  # fibonacci(1) → 0이 0번, 1이 1번 호출

# DP를 이용해 피보나치 호출 횟수 계산
for i in range(2, 41):
    dp[i] = (dp[i-1][0] + dp[i-2][0], dp[i-1][1] + dp[i-2][1])

# 테스트 케이스 입력
T = int(input())
for _ in range(T):
    N = int(input())
    print(dp[N][0], dp[N][1])  # N에 대한 0과 1 호출 횟수 출력
                                          