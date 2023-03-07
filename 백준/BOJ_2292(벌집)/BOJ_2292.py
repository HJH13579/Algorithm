# 1, 7, 19, 37, 61...
#  +6 +12 +18 +24
N = int(input())

arr = [[1]]

n = 1
cnt = 1

while n < N:
    lst = []
    for k in range(n+1, 6*cnt + n + 1):
        lst.append(k)

    arr.append(lst)
    cnt += 1
    n = 6*cnt + n

last_lst = []
for p in range(n+1, N+1):
    last_lst.append(p)

arr.append(last_lst)

print(arr)