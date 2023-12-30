import sys
input = sys.stdin.readline

q = int(input())
for query in range(q):
    x1,y1,x2,y2,w = map(int,input().split())
    r1 = (x1**2 + y1**2)
    r2 = (x2**2 + y2**2)

    x = 1
    cnt = 0
    while x**2 < w:
        y = int((w - x**2)**0.5)
        if x**2 + y**2 != w:
            x += 1
            continue
        
        if w*y2**2 <= r2*y**2 and r1*y**2 <= w*y1**2:
            cnt += 1

        x += 1

    print(cnt)