dic_direction = {1: (-1, 0), 2: (1, 0), 3: (0, 1), 4:(0, -1)}

# [3] 상어 이동
def shark_migration():
    new_arr = [[0] * (C + 2) for _ in range(R + 2)]
    for idx_y in range(1, R+1):
        for idx_x in range(1, C+1):
            if arr[idx_y][idx_x] != 0:
                for key in dic_direction.keys():
                    if key == arr[idx_y][idx_x][1]:
                        new_idx_y = idx_y + dic_direction[key][0]
                        new_idx_x = idx_x + dic_direction[key][1]

    return new_arr



R, C, M = map(int, input().split())

arr = [[0]*(C+2) for _ in range(R+2)]

for _ in range(M):
    r, c, s, d, z = map(int, input().split())
    arr[r][c] = [s, d, z]

n = 0
sm = 0

# 낚시왕이 가장 오른쪽 열의 오른쪽 칸에 이동할 때까지
while n != C+1:
    # 1초동안

    # [1] 낚시왕이 오른쪽으로 한 칸 이동
    fisher = arr[0][n]
    n += 1

    # [2] 낚시왕이 있는 열에 있는 상어 중 가장 땅에 가까운 상어 잡기
    for idx_column in range(1, R+1):
        if arr[idx_column][n] != 0:
            sm += arr[idx_column][n][2]
            arr[idx_column][n] = 0
            break

    # [3] 상어 이동
    arr = shark_migration()

print(arr)

