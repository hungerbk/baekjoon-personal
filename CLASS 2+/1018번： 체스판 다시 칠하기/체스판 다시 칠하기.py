import sys

def input():
  return sys.stdin.readline().rstrip()

# 모든 경우의 수를 구하고 최솟값을 리턴한다

n, m = map(int, input().split())

board = []
count_list = []

# 제일 첫번째 색이 검정색인 올바른 체스판
black_started_chess = [
    "BWBWBWBW",
    "WBWBWBWB",
    "BWBWBWBW",
    "WBWBWBWB",
    "BWBWBWBW",
    "WBWBWBWB",
    "BWBWBWBW",
    "WBWBWBWB",
]

# 제일 첫번째 색이 흰색인 올바른 체스판
white_started_chess = [
    "WBWBWBWB",
    "BWBWBWBW",
    "WBWBWBWB",
    "BWBWBWBW",
    "WBWBWBWB",
    "BWBWBWBW",
    "WBWBWBWB",
    "BWBWBWBW",
]

for _ in range(n):
  board.append(input())

# 8*8 보드 탐색 (범위를 벗어나지 않게 하기 위해서 -7까지만)
for i in range(n-7):
  for j in range(m-7):

    # i, j부터 시작하는 8*8 보드를 새로 만든다
    check_board = [tmp[j:j+8] for tmp in board[i:i+8]]
    # 검정색으로 시작하는 보드의 count
    black = 0
    # 흰색으로 시작하는 보드의 count
    white = 0

    for a in range(8):
      for b in range(8):
        # 검정으로 시작하는 올바른 체스판이랑 일치하는 지 확인하고, 일치하지 않으면 카운트를 추가한다
        if check_board[a][b] != black_started_chess[a][b]:
          black += 1
        # 흰색으로 시작하는 올바른 체스판이랑 일치하는 지 확인하고, 일치하지 않으면 카운트를 추가한다
        if check_board[a][b] != white_started_chess[a][b]:
          white += 1
    # 둘 중 더 작은 값을 리스트에 추가 
    count_list.append(min(black, white))
# 최솟값을 보여준다
print(min(count_list))
