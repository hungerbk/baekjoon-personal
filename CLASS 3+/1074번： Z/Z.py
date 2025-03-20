import sys

def input():
    return sys.stdin.readline().rstrip()

def find_z_order(n, r, c):
    if n == 0:  # 더 이상 분할할 수 없는 경우 (2^0 = 1x1)
        return 0
    
    size = 2 ** (n - 1)  # 현재 배열의 절반 크기
    area = size * size  # 한 사분면의 크기

    if r < size and c < size:  # 1번 사분면
        return find_z_order(n - 1, r, c)
    elif r < size and c >= size:  # 2번 사분면
        return area + find_z_order(n - 1, r, c - size) #순서를 구하는 것이기 때문에, area(1사분면 개수)를 더해주는 것. c >= size이기 때문에 size 내부 좌표로 변경
    elif r >= size and c < size:  # 3번 사분면
        return 2 * area + find_z_order(n - 1, r - size, c)
    else:  # 4번 사분면
        return 3 * area + find_z_order(n - 1, r - size, c - size)

# 입력 받기
N, r, c = map(int, input().split())

# 결과 출력
print(find_z_order(N, r, c))