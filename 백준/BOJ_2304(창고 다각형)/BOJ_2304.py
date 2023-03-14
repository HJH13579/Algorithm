N = int(input())

# 1000짜리를 만들지 않고 필요한만큼만 환경 만들기 작업
lst_L = []
lst_H = []

mx_L = 0

for _ in range(N):
    L, H = map(int, input().split())
    lst_L.append(L)
    lst_H.append(H)

    if mx_L < L:
        mx_L = L

buildings = [0] * (mx_L+1)

for idx in range(N):
    buildings[lst_L[idx]] = lst_H[idx]

# 가장 높은 빌딩을 기준으로 왼쪽은 더 높은 빌딩이 나올 때까지 지붕 높이 유지
# 오른쪽은 Reverse해서 같은 법칙
# 가장 높은 빌딩이 2개 이상이면 처음과 끝 빌딩 사이를 전부 최대 높이로 처리

first_max_idx = 0
for idx in range(mx_L+1):
    if buildings[idx] == max(buildings):
        first_max_idx = idx
        break

last_max_idx = 0
for idx in range(mx_L+1):
    if buildings[idx] == max(buildings):
        last_max_idx = idx

area = 0

# 왼쪽 지역 면적
left_idx = 0
left_height = 0
while left_idx < first_max_idx:
    area += left_height

    if left_height < buildings[left_idx+1]:
        left_height = buildings[left_idx+1]

    left_idx += 1

# 중앙 지역 면적(최대 높이 면적)
area += buildings[first_max_idx] * (last_max_idx - first_max_idx + 1)

# 오른쪽 지역 면적
right_idx = mx_L
right_height = buildings[mx_L]
while right_idx > last_max_idx:
    area += right_height

    if right_height < buildings[right_idx-1]:
        right_height = buildings[right_idx-1]

    right_idx -= 1

print(area)