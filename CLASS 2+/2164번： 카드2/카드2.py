import sys, collections

def input():
    return sys.stdin.readline().rstrip()

n = int(input())
card_queue = collections.deque([i+1 for i in range(n)])

while len(card_queue) > 1:
    card_queue.popleft()
    card_queue.append(card_queue.popleft())

print(card_queue[0])

