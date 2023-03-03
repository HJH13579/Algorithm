# 목적지에서 시작(2를 찾고 거슬러 올라간다)

# 1순위 : 좌우로 길이 있는 경우 => 왔던 길을 다시 방문하는 문제점 발생
# 2순위 : 위로

# 범위체크! => 안하는 것이 최선! => 좌우에 0을 붙여서 범위체크 생략 (좌우만 0으로 padding)
# But! ans - 1

# 재방문 방지
# (1) visited[] 배열 : debug 용이
# (2) 이동한 길 지우기! (= 지나온 1을 0으로 바꾸기)

# [1] 2 위치 찾기 : ci, cj 시작좌표, ci = N - 1

# [2] while ci > 0 : 0행 도착 시 종료!
#       arr[ci][cj] = 0 # 재방문 방지
#   좌우 길이 있는 경우 거기로 이동
#         if arr[ci][cj-1] == 1 # 왼쪽
#             cj -= 1 # 이동
#         elif arr[ci][cj + 1] == 1  # 오른쪽
#             cj += 1  # 이동
#         else:   # 위

import sys

sys.stdin = open("input.txt", "r")

T = 10
for test_case in range(1, T + 1):
    _ = input()
    N = 100
    # 좌, 우 양쪽을 0으로 padding해서 입력
    arr = [[0] + list(map(int, input().split())) + [0] for _ in range(N)]

    # [1] 시작위치(2) 찾기
    ci = N - 1
    for j in range(1, N + 1):
        if arr[ci][j] == 2:
            cj = j
            break

    # [2] N-1행 시작위치에서 위쪽으로 사다리이동
    while ci > 0:
        arr[ci][cj] = 0  # 재방문 방지
        if arr[ci][cj - 1]:  # 왼쪽!
            cj -= 1  # 이동
        elif arr[ci][cj + 1]:  # 오른쪽!
            cj += 1  # 이동
        else:
            ci -= 1  # 위쪽이동
    # print(f'#{test_case} {arr}')
    print(f'#{test_case} {cj - 1}')
