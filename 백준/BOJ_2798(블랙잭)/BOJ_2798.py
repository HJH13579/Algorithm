import sys
sys.stdin = open("input.txt", "r")

def subset(lst, n, k, s):
    if s == n:
        if sum(visited) == k:
            subset_lst = []
            for i in range(n):
                if visited[i] == 1:
                    subset_lst.append(lst[i])
            alst.append(subset_lst)
            return

    else:
        visited[s] = 1
        subset(lst, n, k, s+1)
        visited[s] = 0
        subset(lst, n, k, s+1)


T = int(input())

for tck in range(1, T+1):
    N, M = map(int, input().split())

    lst = list(map(int, input().split()))

    alst = []
    # DFS 재귀 쓸 때는 visited 배열은 함수 밖에다 둘 것
    visited = [0] * N

    subset(lst, N, 3, 0)

    mn = 100000
    sm = 0

    for x in alst:
        if sum(x) == M:
            sm = sum(x)
            break
        elif sum(x) < M and mn > M - sum(x):
            mn = M - sum(x)
            sm = sum(x)

    print(f'#{tck} {sm}')