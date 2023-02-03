for task in range(1, 11):
    
    dump_num = int(input())
    height = sorted(list(map(int, input().split())))

    def dump_func(num, lst):

        for _ in range(num):
            if (lst[len(lst) - 1] - lst[0]) <= 1:
                return lst[len(lst)-1] - lst[0]

            else:
                lst[len(lst) - 1] = lst[len(lst) - 1] - 1
                lst[0] = lst[0] + 1
            
        return lst[len(lst) - 1] - lst[0]

    result = dump_func(dump_num, height)

    print(f'#{task} {result}')


