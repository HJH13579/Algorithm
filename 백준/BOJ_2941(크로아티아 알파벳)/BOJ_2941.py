import sys
sys.stdin = open("input.txt", 'r')

T = int(input())

cru_alphabet = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

for tck in range(1, T+1):
    word = input()

    cnt = 0

    for idx in range(len(word), -1, -1):
        if word[idx] == '=':

        elif word[idx] == '-':

        elif word[idx] == '+':

        elif word[idx] == 'j':

        else:
            cnt += 1
            word.pop()

    print(word)