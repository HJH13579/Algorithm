import sys
sys.stdin = open("input.txt", "r")

T = int(input())

for tck in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range()]


    print(f'#{tck} {ans}')