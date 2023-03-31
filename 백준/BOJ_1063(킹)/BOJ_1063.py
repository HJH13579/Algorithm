import sys
sys.stdin = open("input.txt", "r")

T = int(input())

x_dic = {'A':1, 'B':2, 'C':3, 'D':4, 'E':5, 'F':6, 'G':7, 'H':8}
move_dic = {'R':(0,1), 'L':(0,-1), 'B':(-1,0), 'T':(1,0), 'RT':(1,1), 'LT':(1,-1), 'RB':(-1,1), 'LB':(-1,-1)}

for tck in range(1, T+1):
    king_location_str, stone_location_str, move_num_str = map(str, input().split())

    king_location = [int(king_location_str[1]), x_dic[king_location_str[0]]]
    stone_location = [int(stone_location_str[1]), x_dic[stone_location_str[0]]]
    move_num = int(move_num_str)

    for _ in range(move_num):
        move = move_dic[input()]

        # 일단 킹부터 이동
        if king_location[0] + move[0] == 0 or king_location[0] + move[0] == 9 or king_location[1] + move[1] == 0 or king_location[1] + move[1] == 9:
            continue
        else:
            king_location = [king_location[0] + move[0], king_location[1] + move[1]]

            # 만약 킹이 이동할 곳에 돌이 있다면
            # 돌도 이동
            if king_location[0] == stone_location[0] and king_location[1] == stone_location[1]:
                if stone_location[0] + move[0] == 0 or stone_location[0] + move[0] == 9 or stone_location[1] + move[1] == 0 or stone_location[1] + move[1] == 9:
                    king_location = [king_location[0] - move[0], king_location[1] - move[1]]
                else:
                    stone_location = [stone_location[0] + move[0], stone_location[1] + move[1]]

    print(f'#{tck} {[k for k, v in x_dic.items() if v == king_location[1]][0] + str(king_location[0])} {[k for k, v in x_dic.items() if v == stone_location[1]][0] + str(stone_location[0])}')