# import sys

# def input():
#     return sys.stdin.readline().rstrip()

# t = int(input())

# for _ in range(t):

#     n, m , k = list(map(int, input().split()))
#     cabbage_list = [ [0] * n for _ in range(m)]

#     for _ in range(k):
#         y, x = list(map(int,input().split()))
#         cabbage_list[x][y] = 1

#     dx = [0, 1, 0, -1]
#     dy = [1, 0, -1, 0]

import sys
from collections import deque

def input():
    return sys.stdin.readline().rstrip()

def bfs(x, y, field, visited, M, N):
    queue = deque([(x, y)])
    visited[y][x] = True

    # 상, 하, 좌, 우 이동을 위한 방향 벡터
    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]

    while queue:
        cx, cy = queue.popleft() # FIFO. 들어온 순서대로 탐색하며, 탐색한 위치는 제거

        for i in range(4):  # 네 방향 탐색
            nx, ny = cx + dx[i], cy + dy[i]

            if 0 <= nx < M and 0 <= ny < N:  # 범위 내에 있고
                if not visited[ny][nx] and field[ny][nx] == 1:  # 방문하지 않았으며 배추가 있는 경우
                    visited[ny][nx] = True
                    queue.append((nx, ny))

def solve():
    T = int(input())  # 테스트 케이스 개수

    for _ in range(T):
        M, N, K = map(int, input().split())  # 가로, 세로, 배추 개수
        field = [[0] * M for _ in range(N)]  # 배추밭 초기화
        visited = [[False] * M for _ in range(N)]  # 방문 여부 체크

        # 배추 위치 입력
        for _ in range(K):
            x, y = map(int, input().split())
            field[y][x] = 1  # 배추가 있는 위치 표시

        count = 0  # 필요한 배추흰지렁이 개수

        for y in range(N):
            for x in range(M):
                if field[y][x] == 1 and not visited[y][x]:  # 배추가 있고 방문하지 않았다면
                    bfs(x, y, field, visited, M, N)
                    count += 1  # 새로운 배추 덩어리를 찾았으므로 지렁이 +1
        
        print(count)  # 현재 테스트 케이스에 대한 결과 출력

solve()