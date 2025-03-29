lst = [(1,3),(6,8),(2,5)]
for i in range(3):
    p = int(input())
    if not p in lst[i]:
        print('EI')
        break

else:
    print('JAH')