import sys
sys.stdin = open("input.txt", "r")

for tck in range(1, 6):
    N = int(input())
    lst = list(map(int, input().split()))

    ans_lst = []

    if N == 1:
        ans = 1

    else:
        mx1 = 0
        cnt1 = 1
        for idx1 in range(N - 1):
            if lst[idx1] <= lst[idx1 + 1]:
                cnt1 += 1
                if idx1 == N - 2:
                    if mx1 < cnt1:
                        mx1 = cnt1
            else:
                if mx1 < cnt1:
                    mx1 = cnt1
                cnt1 = 1

        mx2 = 0
        cnt2 = 1
        for idx2 in range(N - 1):
            if lst[idx2] >= lst[idx2 + 1]:
                cnt2 += 1
                if idx2 == N - 2:
                    if mx2 < cnt2:
                        mx2 = cnt2
            else:
                if mx2 < cnt2:
                    mx2 = cnt2
                cnt2 = 1

        ans = max(mx1, mx2)

    print(ans)