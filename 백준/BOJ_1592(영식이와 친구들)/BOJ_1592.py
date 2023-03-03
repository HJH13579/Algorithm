import sys
sys.stdin = open("input.txt", "r")

T = int(input())

for tck in range(1, T+1):
    N, M, L = map(int, input().split())

    lst = [0]*N
    location = 1

    while 1:
        if max(lst) == M:
            break

        lst[location] += 1

        # 파이썬의 음수의 몫, 나머지 계산법 활용
        if lst[location] % 2 == 1:
            location = (location + L) % N
        else:
            location = (location - L) % N

    # lst : 각 사람하다 던진 횟수 리스트, -1 해주는 이유는 처음 받은 사람도 카운트 되었기 때문
    ans = sum(lst) - 1

    print(f'#{tck} {ans}')