import sys

sys.stdin = open("input.txt", "r")

for tck in range(1, 11):
    dummy = int(input())

    lst = [list(map(int, input().split())) for _ in range(100)]

    mx = 0

    # 행의 합
    for i in range(100):
        sum_row = 0
        for j in range(100):
            sum_row += lst[i][j]

        if mx < sum_row:
            mx = sum_row

    # 열의 합
    for j in range(100):
        sum_column = 0
        for i in range(100):
            sum_column += lst[i][j]

        if mx < sum_column:
            mx = sum_column

    # 대각선의 합
    for x in range(100):
        sum_diagonal1 = 0
        sum_diagonal1 += lst[x][x]
        sum_diagonal2 = 0
        sum_diagonal2 += lst[x][99-x]

        if mx < sum_diagonal1:
            mx = sum_diagonal1
        if mx < sum_diagonal2:
            mx = sum_diagonal2

    print(f'#{tck} {mx}')