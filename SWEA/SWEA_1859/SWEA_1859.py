import sys

sys.stdin = open("input.txt", "r", encoding="UTF8")

T = int(input())

for tck in range(1, T + 1):

    N = int(input())

    lst = list(map(int, input().split()))

    # [1] 매매가 중 최고액
    # [2] 최고액과 그 전까지의 매매가들과의 차의 합
    # [3] 계산된 매매가들 제거 후 마지막 매매가가 최대가 될 때까지 [1]~[2] 반복
    # [4] 맨 앞의 매매가가 최대일 경우 or 빈 리스트가 될 경우 end

    # [1] 매매가 중 최고액 인덱스 구하기
    profit = 0

    while (1):
        mx_idx = 0

        for i in range(len(lst)):
            if lst[mx_idx] < lst[i]:
                mx_idx = i

        if mx_idx == 0:
            break

        # [2] 최고액과 그 전까지의 매매가들과의 차의 합

        for j in range(mx_idx + 1):
            profit += (lst[mx_idx] - lst[j])

        # [3] 계산된 매매가들 제거 후 마지막 매매가가 최대가 될 때까지 [1]~[2] 반복
        for x in range(mx_idx + 1):
            lst.remove(lst[0])

        if lst == []:
            break

    print(f'#{tck} {profit}')