import sys
sys.stdin = open("input.txt", 'r')

T = int(input())

cru_alphabet = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

for tck in range(1, T+1):
    word = input()

    stk = []
    cnt = 0

    for idx in range(len(word)-1, -1, -1):
        if word[idx] == '=' or '-' or 'j':
            if not stk:
                stk.append(word[idx])
            else:
                stk.pop()
                cnt += 1
                stk.append(word[idx])

        elif word[idx] == 'c':
            if stk[0] == '=' or '-':
                stk.pop()
                cnt += 1
            else:
                stk.pop()
                cnt += 1

        elif word[idx] == 'z':
            stk.append(word[idx])
        elif word[idx] == 'd':

        elif word[idx] == 'l':

        elif word[idx] == 'n':

        elif word[idx] == 's':

        else:
            cnt += 1


    print(word)