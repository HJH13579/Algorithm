import sys
sys.stdin = open("input.txt", "r")

def game(lst_A, lst_B, n):
    if n != 1:
        cnt_n_a = 0
        cnt_n_b = 0
        for x in lst_A[1:]:
            if x == n:
                cnt_n_a += 1
        for y in lst_B[1:]:
            if y == n:
                cnt_n_b += 1

        if cnt_n_a == cnt_n_b:
            return game(lst_A, lst_B, n-1)
        else:
            if cnt_n_a < cnt_n_b:
                return 'B'
            elif cnt_n_a > cnt_n_b:
                return 'A'

    else:
        cnt_1_a = 0
        cnt_1_b = 0
        for x in lst_A[1:]:
            if x == 1:
                cnt_1_a += 1
        for y in lst_B[1:]:
            if y == 1:
                cnt_1_b += 1

        if cnt_1_a == cnt_1_b:
            return 'D'
        else:
            if cnt_1_a < cnt_1_b:
                return 'B'
            elif cnt_1_a > cnt_1_b:
                return 'A'

for tck in range(2):
    N = int(input())

    for _ in range(N):
        lst_A = list(map(int, input().split()))
        lst_B = list(map(int, input().split()))

        print(game(lst_A, lst_B, 4))