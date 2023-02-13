import sys

sys.stdin = open("input.txt", "r")

N = int(input())

# 가로 세로 좌표 중 최대값을 구해서 곱하고, 들어간 꼭짓점을 찾아 사각형을 뺀다.
# 결국 최대 길이를 보충하려면, 같은 방향으로 2번씩 움직여야 한다.
# 그 2번씩 반복되는 움직임 중 사이에 있는 움직임이 들어간 꼭짓점
# 반대로 1번씩 움직이는 길이가 최대

vertex_lst = []

for _ in range(6):
    vertex = list(map(int, input().split()))
    vertex_lst.append(vertex)


