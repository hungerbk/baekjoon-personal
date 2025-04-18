import sys
input = sys.stdin.readline

n = int(input())
sequence = [int(input()) for _ in range(n)]

stack = []
result = []
current = 1  # 1부터 시작

for num in sequence:
    # 필요한 숫자까지 push
    while current <= num:
        stack.append(current)
        result.append('+')
        current += 1

    # 원하는 숫자가 스택 맨 위에 있으면 pop
    if stack[-1] == num:
        stack.pop()
        result.append('-')
    else:
    # 꺼내야 하는 숫자가 스택에 없으면 불가능
        print("NO")
        exit()

# 성공적으로 수열을 만들었으면 출력
print('\n'.join(result))