N = int(input())

total = 0

for n in range(1, N+1):
    cnt = 0

    for a in range(1, int(n ** (1/2))+1):
        if n % a == 0:
            cnt += 1

    total += cnt

print(total)