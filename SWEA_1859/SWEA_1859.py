import sys

sys.stdin = open("input.txt", "r", encoding="UTF8")

T = int(input())

for tck in range(1, T + 1):

    N = int(input())

    lst = list(map(int, input().split()))

    # [1] 매매가 중 최고액
    # [2] 최고액과 그 전까지의 매매가들과의 차의 합
    # [3] 계산된 매매가들 제거 후 마지막 매매가가 최대가 될 때까지 [1]~[2] 반복
    # [4] 마지막 매매가가 최소일 경우 0

    # [1] 매매가 중 최고액 인덱스 구하기
    mx_idx = 0
    for i in range(N):
        if lst[mx_idx] < lst[i]:
            mx_idx = i

    # [2] 최고액과 그 전까지의 매매가들과의 차의 합
    profit = 0

    for j in range(mx_idx + 1):
        profit += (lst[mx_idx] - lst[j])





    print(f'#{tck} {profit}')