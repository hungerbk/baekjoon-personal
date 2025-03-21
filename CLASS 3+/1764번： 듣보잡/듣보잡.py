import sys

def input():
    return sys.stdin.readline().rstrip()

n ,m = map(int, input().split())

name_dict = {}
answer = []

for _ in range(n+m):
    name = input()
    name_dict[name] = name_dict.get(name, 0) + 1
    if name_dict[name] == 2:
        answer.append(name)

print(len(answer))
print('\n'.join(sorted(answer)))

# GPT 풀이. set 이용

n, m = map(int, input().split())

hear = set(input().strip() for _ in range(n))
see = set(input().strip() for _ in range(m))

# 교집합 & 정렬
answer = sorted(hear & see)

print(len(answer))
print('\n'.join(answer))

# 입력 데이터가 매우 많고, 집합적 비교가 핵심	🔥 set 방식 추천
# 중복 횟수 기반 분석이나 확장 가능성 있음	✅ dict 방식 추천