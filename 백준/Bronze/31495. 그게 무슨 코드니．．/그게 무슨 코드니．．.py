st = input()
flag = len(st) > 2 and st[0]=='"' and st[-1]=='"'
if flag:
    print(st[1:-1])
else:
    print('CE')