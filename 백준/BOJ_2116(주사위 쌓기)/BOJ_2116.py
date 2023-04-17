def popping(lst, idx):
    if idx <= 3:
        second_idx = idx + 2
    else:
        second_idx = idx - 2
    a = lst[idx]
    b = lst[second_idx]
    lst.remove(a)
    lst.remove(b)
    return max(lst)

def dice_side_sum(idx, n, sm):
    global ans
    if n == N-1:
        ans = max(ans, sm)
        return

    next_idx = 0
    for i in range(6):
        if arr[n][idx] == arr[n+1][i]:
            next_idx = i
            break

    dice_side_sum(next_idx, n+1, sm+popping(arr[n], idx))

N = int(input())

arr = [list(map(int, input().split())) for _ in range(N)]

ans = 0

for start_idx in range(6):
    dice_side_sum(start_idx, 0, 0)

print(ans)