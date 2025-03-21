import sys

def input():
    return sys.stdin.readline().rstrip()

# n, k = map(int, input().split())

# n의 현재 위치를 x라 했을 때
# 1초 뒤 x+1, x-1   
# 순간이동 시 1초 뒤 2x

# dp = [0] * max(n, k)

from collections import deque

def bfs(N, K):
    visited = [0] * 100001  # 각 위치까지 걸린 시간 저장 (방문 체크도 겸함)

    queue = deque()
    queue.append(N)

    while queue:
        x = queue.popleft()

        if x == K:  # 도착했으면 시간 반환
            return visited[x]

        for nx in (x - 1, x + 1, 2 * x):
            if 0 <= nx <= 100000 and visited[nx] == 0: # 방문하지 않은 경우
                visited[nx] = visited[x] + 1  # 현재 시간 + 1
                queue.append(nx)

# Time 0: [5]
# Time 1: [4, 6, 10]
# Time 2: [3, 7, 8, 9, 11, 12, 20]
# Time 3: [2, 13, 14, 18]
# Time 4: [17] ← 도착!

# 입력
N, K = map(int, input().split())

# 결과 출력
print(bfs(N, K))