import sys
sys.stdin = open("input.txt", "r")

T = int(input())

for tck in range(1, T+1):
    N = int(input())

    num_1 = int(input())

    candidate_lst = []

    for _ in range(N-1):
        vote = int(input())
        candidate_lst.append(vote)

    cnt = 0

    if candidate_lst == []:
        cnt = 0
    else:
        while num_1 <= max(candidate_lst):
            max_idx = 0
            for idx in range(len(candidate_lst)):
                if candidate_lst[idx] == max(candidate_lst):
                    max_idx = idx

            num_1 += 1
            candidate_lst[max_idx] -= 1

            cnt += 1

    print(cnt)