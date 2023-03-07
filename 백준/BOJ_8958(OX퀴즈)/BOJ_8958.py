import sys
sys.stdin = open("input.txt", "r")

T = int(input())

for tck in range(1, T+1):
    lst = list(map(str, input()))
    point_lst = []

    point = 0

    for x in range(len(lst)):
        if lst[x] == 'X':
            point = 0
            point_lst.append(point)
        else:
            point += 1
            point_lst.append(point)

    print(sum(point_lst))
