N = int(input())

lst = list(map(int, input().split()))

sort_lst = sorted(lst)
ans = []

for x in range(len(sort_lst)):
    sm = 0
    for y in range(x+1):
        sm += sort_lst[y]
    ans.append(sm)

print(sum(ans))
