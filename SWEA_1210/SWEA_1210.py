import sys

sys.stdin = open("input.txt", "r")

def going_side(y, x):
    if lst[y][x - 1] == 1:
        x -= 1
    if lst[y][x + 1] == 1:
        x += 1
    if

def going_up(y, x):
    if lst[y][x - 1] == 0 and lst[y][x + 1] == 0:
        y -= 1
    else going_side(y, x):




for tck in range(1, 11):
    dummy = int(input())

    lst = [list(map(int, input().split())) for _ in range(100)]

    # 도착점(2)의 index 값 구하기
    for i in range(100):
        if lst[99][i] == 2:
            i_end = i

    y = 99

    # 좌우에 1이 없으면 위로, 있으면 위아래로 1이 있을 때까지 좌/우로 이동
    while(1):
        if lst[y][i_end - 1] == 0 and lst[y][i_end + 1] == 0:
            y -= 1

        else:
            if lst[y][i_end - 1] == 1:
                i_end -= 1
            if lst[y][i_end + 1] == 1:
                i_end += 1

        if y == 0:
            break



    # 재귀함수

    def up_or_side():
        if y == 0:
            return i_end

        if

    print(f'#{tck} {i_end}')