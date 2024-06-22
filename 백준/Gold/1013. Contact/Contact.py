import re

r = r'(100+1+|01)+'

t = int(input())
for case in range(t):
    st = input()
    res = re.fullmatch(r,st)
    print('YES' if res!=None else 'NO')