def cal(x1,l1,x2,l2):
    if x1 > x2:
        x1,x2 = x2,x1
        l1,l2 = l2,l1

    tmp1 = max(0,x1+l1 - x2)
    tmp2 = l2

    return min(tmp1,tmp2)

t = int(input())
for case in range(t):
    x1,y1,x2,y2,x3,y3,x4,y4 = map(int,input().split())

    x = cal(x1, x2-x1, x3, x4-x3)
    y = cal(y1, y2-y1, y3, y4-y3)

    print((x2-x1)*(y2-y1) - x*y)