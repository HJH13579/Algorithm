value_dic = {'(': 0, '+': 1, '-': 1, '*': 2, '/': 2}

E = list(input())

stk = []
eq = []

for x in E:
    if x.isalpha():
        eq.append(x)
    else:
        if x == ')':
            while stk[-1] != '(':
                eq.append(stk.pop())
            stk.pop()
        else:





print(E)