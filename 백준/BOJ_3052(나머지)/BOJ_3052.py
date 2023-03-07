import sys
sys.stdin = open("input.txt", "r")

T = int(input())

for tck in range(1, T+1):
    set_leftover = set([])

    for _ in range(10):
        n = int(input())
        set_leftover.add(n % 42)

    print(f'#{tck} {len(set_leftover)}')