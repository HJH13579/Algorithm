# 1, 7, 19, 37, 61...
#  +6 +12 +18 +24
N = int(input())

n = 0
start_num = 1
floor = 1

while 6 * n + start_num < N:
    start_num += 6 * n
    n += 1
    floor += 1

# 1 : 0 1 1
# 2~7 : 1 1 2
# 8~19 : 2 7 3
# 20~37 : 3 19 4

print(floor)