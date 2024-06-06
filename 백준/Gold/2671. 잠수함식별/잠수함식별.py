import re

p = r'(1+0+01|10)+'

st = input()[::-1]

tmp = re.match(p,st)
if tmp == None:
    print('NOISE')

else:
    res = tmp.span()[1]
    if res == len(st):
        print('SUBMARINE')
    else:
        print('NOISE')