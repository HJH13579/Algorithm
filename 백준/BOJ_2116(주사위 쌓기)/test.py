dic_dice_idx = {0: 5, 1: 3, 2: 4, 3: 1, 4: 2, 5: 0}

lst = list(map(int, input().split()))

for idx in range(6):
    c_lst = lst
    opposite_idx = dic_dice_idx[idx]
    c_lst[idx] = 0
    c_lst[opposite_idx] = 0

    print(c_lst)

