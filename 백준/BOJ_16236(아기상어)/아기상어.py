import sys
sys.stdin = open("input.txt", "r")

def bfs():
    for i in range(N):
        for j in range(N):
            if
    return

T = int(input())

for tck in range(1, T+1):
    N = int(input())

    arr = [list(map(int, input().split())) for _ in range(N)]

    size = 2
    i_index, j_index = 0, 0

    # 아기 상어 위치 찾기
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 9:
                i_index = i
                j_index = j

    # 먹을 수 있는 물고기 중 가장 가까운 물고기로 이동


    print(f'{i_index} {j_index}')