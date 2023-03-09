K = int(input())

direction_x_lst = []
length_x_lst = []
direction_y_lst = []
length_y_lst = []

for _ in range(6):
    direction_num, length = map(int, input().split())
    if direction_num == 1 or direction_num == 2:
        direction_x_lst.append(direction_num)
        length_x_lst.append(length)
    else:
        direction_y_lst.append(direction_num)
        length_y_lst.append(length)

# 1개(큰 직사각형의 변)/2개(작은 직사각형의 변)씩 나오는 숫자 파악
# 큰 직사격형의 변의 (idx + 2) % 6에 위치한 idx가 작은 직사각형의 변
big_square = 1
small_square = 1

for x_idx in range(3):
    if direction_x_lst.count(direction_x_lst[x_idx]) == 1:
        big_square *= length_x_lst[x_idx]
        small_square *= length_x_lst[(x_idx + 2) % 3]

for y_idx in range(3):
    if direction_y_lst.count(direction_y_lst[y_idx]) == 1:
        big_square *= length_y_lst[y_idx]
        small_square *= length_y_lst[(y_idx + 2) % 3]

print(direction_x_lst)
print(direction_y_lst)
print(length_x_lst)
print(length_y_lst)
print(big_square)
print(small_square)






# 시작점을 무조건 가장 긴 변 2개가 만나는 꼭짓점으로 지정
# 그러면 반복해서 나오는 번호(ex. 3131)에서 중간에 있는 번호의 길이만 추출

# 1 시작 : 4242 (2: 2개, 4: 2개)
# 2 시작 : 3131 (1: 2개, 3: 2개)
# 3 시작 : 1414 (1: 2개, 4: 2개)
# 4 시작 : 2323 (2: 2개, 3: 2개)
# 2개씩 나오는 숫자만 파악해도, Case와 순서는 정해져 있으니, 어떤 숫자가 2개씩 나오는 지만 파악

# if double_num_lst == [1, 3]:
#     small_square = dictionary[1][0] * dictionary[3][1]
# elif double_num_lst == [1, 4]:
#     small_square = dictionary[1][1] * dictionary[4][0]
# elif double_num_lst == [2, 3]:
#     small_square = dictionary[2][1] * dictionary[3][0]
# elif double_num_lst == [2, 4]:
#     small_square = dictionary[2][0] * dictionary[4][1]
#
# ans = (big_square - small_square) * K
#
# print(ans)