for task in range(1, 11):
    
    dump_num = int(input())
    height = list(map(int, input().split()))

    def dump_func(num, lst):

        for _ in range(num):
            if (max(lst) - min(lst)) <= 1:
                return (max(lst) - min(lst))

            else:
                lst = dumping(lst)
            
        return (max(lst) - min(lst))

    def dumping(lst):
        
        max_lst = max(lst)
        min_lst = min(lst)

        lst.remove(max_lst)
        lst.remove(min_lst)

        max_lst = max_lst - 1
        min_lst = min_lst + 1

        lst.append(max_lst)
        lst.append(min_lst)

        return lst
     

    result = dump_func(dump_num, height)

    print(f'#{task} {result}')