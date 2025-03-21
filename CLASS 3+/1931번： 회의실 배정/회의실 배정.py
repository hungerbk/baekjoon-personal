import sys
input = sys.stdin.readline

n = int(input())
meetings = [tuple(map(int, input().split())) for _ in range(n)] # tuple로 감싸는 이유: (시작, 끝) 시간 쌍으로 만들기 위해서

# 종료 시간 오름차순 정렬, 같으면 시작 시간 오름차순
meetings.sort(key=lambda x: (x[1], x[0]))

count = 0
end_time = 0

for start, end in meetings:
    if start >= end_time:
        count += 1
        end_time = end

print(count)
