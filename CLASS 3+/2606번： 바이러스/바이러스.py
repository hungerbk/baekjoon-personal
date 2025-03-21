# import sys

# def input():
#     return sys.stdin.readline().rstrip()


# # input 값을 알 수 없기 때문에 (순서대로 X) 연쇄적인 연결점을 알 수 없음 
# n = int(input())
# m = int(input())
# computer_net = [tuple(map(int, input().split())) for _ in range(m)]

# count = 0

# virus_list = set([1])

# for start, end in computer_net:
#     if start in virus_list:
#         virus_list.add(end)

# print(len(virus_list)-1)

# BFS
import sys
from collections import deque

def input():
    return sys.stdin.readline().rstrip()

n = int(input())
m = int(input())

# 인접 리스트 생성
graph = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)  # 양방향 연결

# graph = [
#     [],         # index 0 (사용 안 함)
#     [2],        # 1번 → 2와 연결
#     [3, 1],     # 2번 → 3, 1과 연결
#     [2, 4],     # 3번 → 2, 4와 연결
#     [3, 5],     # 4번 → 3, 5와 연결
#     [6, 4],     # 5번 → 6, 4와 연결
#     [5, 7],     # 6번 → 5, 7과 연결
#     [6]         # 7번 → 6과 연결
# ]    

visited = [False] * (n + 1)
queue = deque([1])
visited[1] = True
count = 0

while queue:
    node = queue.popleft()
    for neighbor in graph[node]:
        if not visited[neighbor]:
            visited[neighbor] = True
            queue.append(neighbor)
            count += 1  # 1번을 제외한 감염된 컴퓨터 수

# DFS
# def dfs(node):
#     global count
#     visited[node] = True
#     for neighbor in graph[node]:
#         if not visited[neighbor]:
#             count += 1
#             dfs(neighbor)

print(count)
