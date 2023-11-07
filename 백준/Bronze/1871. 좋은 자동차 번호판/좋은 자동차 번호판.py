int_ = lambda x:int(x) if x.isdigit() else x

n = int(input())
for _ in range(n):
    st,num = map(int_,input().split('-'))
    for i in range(3):
        num -= (ord(st[i])-ord('A'))*(26**(2-i))

    res = 100-abs(num)
    print('nice' if res>=0 else 'not nice')