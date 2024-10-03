dx = (0,1,0,-1)
dy = (1,0,-1,0)

dic = dict(zip("WDSA",range(4)))

x,y = 0,0
i = 0
n = int(input())
for _ in range(n):
    st = input()
    if st[0] == 'M':
        i = (i + (1 if st[1]=='R' else -1))%4
    else:
        x += dx[(i + dic[st])%4]
        y += dy[(i + dic[st])%4]

    cx = x + dx[(i+2)%4]
    cy = y + dy[(i+2)%4]
    print(x,y,cx,cy)