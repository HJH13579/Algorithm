import sys
sys.stdin = open("input.txt", "r")

for _ in range(2):
    N, K = map(int, input().split())
    lst = list(map(int, input().split()))

    mx = 0
    for x in range(5):
        mx += sorted(lst, reverse=True)[x]

    max_sum = -100 * K

    for idx in range(N-K+1):
        sm = 0
        for i in range(idx, idx+K):
            sm += lst[i]

        if sm == mx:
            max_sum = mx
            break

        elif max_sum < sm:
            max_sum = sm

    print(max_sum)