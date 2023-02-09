# IndexError: list index out of range
# 인덱스에러의 해결 방법 중 하나 : Padding

# 돌아가지 못하도록 코딩을 강제로 짜는 것보다 지나간 변수를 막거나 제거하는 것이 더 효율적일 수 있다.

import sys

sys.stdin = open("input.txt", "r")

di = [-1, 0, 0]
dj = [0, -1, 1]

for tck in range(1, 11):
    dummy = int(input())

    arr = [[0] + list(map(int, input().split())) + [0] for _ in range(100)]

    # 도착점(2)의 index 값 구하기
    for j in range(102):
        if arr[99][j] == 2:
            j_end = j
            break

    i = 99
    j = j_end
    dr = 0

    while i > 0:

        ni, nj = i + di[dr], j + dj[dr]
        i, j = ni, nj

        if arr[i][j - 1] == 1:
            j -= 1
            while arr[i - 1][j] == 0:
                dr = 1
                ni, nj = i + di[dr], j + dj[dr]
                i, j = ni, nj
            i -= 1
        elif arr[i][j + 1] == 1:
            j += 1
            while arr[i - 1][j] == 0:
                dr = 2
                ni, nj = i + di[dr], j + dj[dr]
                i, j = ni, nj
            i -= 1
        elif arr[i][j + 1] == 0 and arr[i][j - 1] == 0:
            dr = 0

    print(f'#{tck} {j}')