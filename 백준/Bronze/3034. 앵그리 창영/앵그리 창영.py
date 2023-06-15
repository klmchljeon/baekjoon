#앵그리 창영
n,w,h = map(int,input().split())
for i in range(n):
    x = int(input())
    if x**2 <= w**2 + h**2:
        print('DA')
    else:
        print('NE')