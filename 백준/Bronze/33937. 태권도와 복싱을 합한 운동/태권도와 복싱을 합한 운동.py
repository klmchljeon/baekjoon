def find(st):
    flag1 = False
    flag2 = False
    res = ''
    for i in st:
        if flag1 and not i in 'aeiou':
            return res

        if i in 'aeiou':
            flag1 = True

        res += i

a = find(input())
b = find(input())
if a!=None and b!=None:
    print(a+b)
else:
    print('no such exercise')