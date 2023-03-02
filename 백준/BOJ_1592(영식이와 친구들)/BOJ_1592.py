import sys
sys.stdin = open("input.txt", "r")

T = int(input())

for tck in range(1, T+1):
    N, M, L = map(int, input().split())

