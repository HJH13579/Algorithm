N, K = map(int, input().split())

arr = [[0]*2 for _ in range(6)]

for x in range(N):
    S, Y = map(int, input().split())
    arr[Y-1][S] += 1

cnt = 0

for i in range(6):
    for j in range(2):
       if arr[i][j] % K == 0:
           cnt += arr[i][j] // K
       else:
           cnt += (arr[i][j] // K) + 1

print(cnt)