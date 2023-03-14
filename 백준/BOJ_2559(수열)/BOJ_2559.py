# 투포인터 알고리즘

import sys
sys.stdin = open("input.txt", "r")

for _ in range(3):
    N, K = map(int, input().split())
    lst = list(map(int, input().split()))

    start = 0
    end = K-1
    sm = 0

    for s in range(start, end+1):
        sm += lst[s]
        mx = sm

    while end < N-1:
        sm -= lst[start]

        start += 1
        end += 1

        sm += lst[end]

        if mx < sm:
            mx = sm

    print(mx)