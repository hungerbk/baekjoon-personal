import sys
import heapq

# 파이썬엔 힙 라이브러리가 존재.. 기본은 최소 힙
# 그렇기 때문에 최대 힙을 만들고 싶으면 음수로 만들어서 사용
# heap = []
# heapq.heappush(heap, -5)
# heapq.heappush(heap, -1)
# heapq.heappush(heap, -10)
# print(-heapq.heappop(heap))  # 출력: 10 출력할 때도 앞에 - 붙이는 거 잊지 말기

input = sys.stdin.readline

n = int(input())
heap = []

for _ in range(n):
    x = int(input())
    
    if x == 0:
        if heap:
            print(heapq.heappop(heap)) # 최솟값 제거
        else:
            print(0)
    else:
        heapq.heappush(heap, x) # 값 추가
