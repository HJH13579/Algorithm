def subset(lst, m, n, k, s, sm):
    global mn
    global close_sm

    if s == n:
        if sum(visited) == k:
            if sm <= m and mn > m - sm:
                mn = m - sm
                close_sm = sm
            return

    else:
        visited[s] = 1
        subset(lst, m, n, k, s+1, sm+lst[s])
        visited[s] = 0
        subset(lst, m, n, k, s+1, sm)

N, M = map(int, input().split())

lst = list(map(int, input().split()))

# DFS 재귀 쓸 때는 visited 배열은 함수 밖에다 둘 것
visited = [0] * N

mn = 100000
close_sm = 0

subset(lst, M, N, 3, 0, 0)

print(f'{close_sm}')