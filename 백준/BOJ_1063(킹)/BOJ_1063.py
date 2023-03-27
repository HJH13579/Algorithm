import sys
sys.stdin = open("input.txt", "r")

T = int(input())

x_dic = {'A':1, 'B':2, 'C':3, 'D':4, 'E':5, 'F':6, 'G':7, 'H':8}
move_dic = {'R':(0,1), 'L':(0,-1), 'B':(-1,0), 'T':(1,0), 'RT':(-1,1), 'R':(0,1), 'R':(0,1), 'R':(0,1), }

for tck in range(1, T+1):
