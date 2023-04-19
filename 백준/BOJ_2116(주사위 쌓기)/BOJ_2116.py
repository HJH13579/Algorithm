dic_dice_idx = {0: 5, 1: 3, 2: 4, 3: 1, 4: 2, 5: 0}

def dice_side_sum(idx, n, sm):
    global ans
    if n == N-1:
        final_idx = dic_dice_idx[idx]
        arr[n][idx] = 0
        arr[n][final_idx] = 0
        ans = max(ans, sm + max(arr[n]))
        return

    opposite_idx = 0
    next_idx = 0
    for i in range(6):
        if arr[n][idx] == arr[n+1][i]:
            opposite_idx = dic_dice_idx[idx]
            next_idx = i
            break
    arr[n][idx] = 0
    arr[n][opposite_idx] = 0

    dice_side_sum(next_idx, n+1, sm + max(arr[n]))

N = int(input())

arr = [list(map(int, input().split())) for _ in range(N)]

ans = 0

for start_idx in range(6):
    dice_side_sum(start_idx, 0, 0)

print(ans)