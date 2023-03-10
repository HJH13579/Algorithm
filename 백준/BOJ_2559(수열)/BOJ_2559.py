import sys
sys.stdin = open("input.txt", "r")

for _ in range(2):
    N, K = map(int, input().split())
    lst = list(map(int, input().split()))

    sum_lst = []

    for idx in range(N-K+1):
        sm = 0
        for i in range(idx, idx+K):
            sm += lst[i]

        sum_lst.append(sm)

    print(max(sum_lst))