N = int(input())

lst = list(map(int, input().split()))
alst = []

for x in range(1, N + 1):
    if lst[x - 1] != 0:
        alst.insert(-lst[x - 1], x)
    # -lst[x - 1]에서 lst[x - 1] == 0 일 때, 삽입이 끝자리부터 넣어지지 않는다.
    # else로 빼서 append
    else:
        alst.append(x)

print(*alst)