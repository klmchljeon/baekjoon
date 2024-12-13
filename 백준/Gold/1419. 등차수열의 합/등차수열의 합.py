l = int(input())
r = int(input())
k = int(input())
if k == 2:
    m = 3
    l = max(l,m)
    print(max(0, r - (l-1)))

elif k == 3:
    m = 6
    l = max(l,m)
    print(max(0, r//3 - (l-1)//3))

elif k == 4:
    m = 10
    l = max(l,m)
    res = max(0,r//2 - (l-1)//2)
    if l <= 12 <= r:
        res -= 1

    print(res)

elif k == 5:
    m = 15
    l = max(l,m)
    print(max(0, r//5 - (l-1)//5))