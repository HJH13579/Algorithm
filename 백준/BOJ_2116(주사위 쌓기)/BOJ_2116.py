import sys

dic_dice_idx = {0: 5, 1: 3, 2: 4, 3: 1, 4: 2, 5: 0}

def dice_side_sum(idx, n, sm):
    global ans
    visited = [0] * 6

    opposite_idx = dic_dice_idx[idx]
    visited[idx] = 1
    visited[opposite_idx] = 1

    mx = 0
    for j in range(6):
        if visited[j] == 0:
            if mx < arr[n][j]:
                mx = arr[n][j]

    if n == N-1:
        ans = max(ans, sm + mx)
        return ans

    next_idx = 0
    for i in range(6):
        if arr[n][opposite_idx] == arr[n+1][i]:
            next_idx = i
            break

    dice_side_sum(next_idx, n+1, sm + mx)

N =  int(sys.stdin.readline())

arr = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

ans = -1e9

for start_idx in range(6):
    dice_side_sum(start_idx, 0, 0)

print(ans)