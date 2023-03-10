K = int(input())

direction_lst = []
length_lst = []

for _ in range(6):
    direction_num, length = map(int, input().split())
    direction_lst.append(direction_num)
    length_lst.append(length)

# 큰사각형은 가장 긴 너비와 높이를 가지고 있다.
# 가장 긴 너비/높이를 구한 후, 순서 상 바로 앞과 뒤의 길이(높이/너비)를 빼면 작은 사각형의 너비와 높이를 구할 수 있따.

max_width = 0
max_height = 0

for idx in range(6):
    if direction_lst[idx] == 1 or direction_lst[idx] == 2:
        if length_lst[idx] > max_width:
            max_width = length_lst[idx]
            x_idx = idx
    elif direction_lst[idx] == 3 or direction_lst[idx] == 4:
        if length_lst[idx] > max_height:
            max_height = length_lst[idx]
            y_idx = idx

big_square = max_width * max_height

if x_idx == 5:
    small_square = abs(length_lst[0] - length_lst[x_idx - 1]) * abs(length_lst[y_idx + 1] - length_lst[y_idx - 1])
elif y_idx == 5:
    small_square = abs(length_lst[x_idx + 1] - length_lst[x_idx - 1]) * abs(length_lst[0] - length_lst[y_idx - 1])
else:
    small_square = abs(length_lst[x_idx+1] - length_lst[x_idx-1]) * abs(length_lst[y_idx+1] - length_lst[y_idx-1])

ans = K * (big_square - small_square)

print(ans)