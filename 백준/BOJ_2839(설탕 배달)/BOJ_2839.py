def least_bag(N, quotient):
    left_over = N - 5 * quotient
    if quotient == 0 and left_over % 3 != 0:
        return -1
    else:
        if left_over % 3 == 0:
            return quotient + (left_over // 3)
        else:
            return least_bag(N, quotient-1)

N = int(input())
quotient = N // 5

print(least_bag(N, quotient))