# 외장함수 만들어서 돌리면 무조건 Runtime Error
# 내장함수를 써야 해결


from itertools import combinations

N, M = map(int, input().split())

lst = list(map(int, input().split()))

alst = list(combinations(lst, 3))

mn = 100000
sm = 0

for x in alst:
    if sum(x) == M:
        sm = sum(x)
        break
    elif sum(x) < M and mn > M - sum(x):
        mn = M - sum(x)
        sm = sum(x)

print(f'{sm}')