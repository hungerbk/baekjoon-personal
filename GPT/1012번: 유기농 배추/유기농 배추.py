# import sys
# sys.setrecursionlimit(10**6)

# T = int(input())

# for _ in range(T):
#     M, N, K = map(int, input().split())
#     graph = [[0]*M for _ in range(N)]
#     visited = [[False]*M for _ in range(N)]

#     for _ in range(K):
#         x, y = map(int, input().split())
#         graph[y][x] = 1

#     def dfs(x, y):
#         visited[y][x] = True
#         for dx, dy in [(-1,0), (1,0), (0,-1), (0,1)]:
#             nx, ny = x + dx, y + dy
#             if 0 <= nx < M and 0 <= ny < N:
#                 if not visited[ny][nx] and graph[ny][nx] == 1:
#                     dfs(nx, ny)

#     count = 0
#     for y in range(N):
#         for x in range(M):
#             if graph[y][x] == 1 and not visited[y][x]:
#                 dfs(x, y)
#                 count += 1

#     print(count)

from collections import deque

T = int(input())

for _ in range(T):
    M, N, K = map(int, input().split())
    graph = [[0]*M for _ in range(N)]
    visited = [[False]*M for _ in range(N)]

    for _ in range(K):
        x, y = map(int, input().split())
        graph[y][x] = 1

    def bfs(x, y):
        queue = deque()
        queue.append((x, y))
        visited[y][x] = True

        while queue:
            cx, cy = queue.popleft()

            for dx, dy in [(-1,0), (1,0), (0,-1), (0,1)]:
                nx, ny = cx + dx, cy + dy
                if 0 <= nx < M and 0 <= ny < N:
                    if not visited[ny][nx] and graph[ny][nx] == 1:
                        visited[ny][nx] = True
                        queue.append((nx, ny))

    count = 0
    for y in range(N):
        for x in range(M):
            if graph[y][x] == 1 and not visited[y][x]:
                bfs(x, y)
                count += 1

    print(count)
