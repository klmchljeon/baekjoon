import sys
input = sys.stdin.readline

n,m,t = map(int,input().split())

dic = dict()
for i in range(t):
    y,k = map(int,input().split())
    if not y in dic:
        dic[y] = 0

    dic[y] = min(dic[y]+k,m)

    dic2 = dict()
    for y in dic:
        k = dic[y]//5
        for i in (-1,0,1):
            ny = y + i
            if not (1<=ny<=n): continue
            if not ny in dic2:
                dic2[ny] = 0

            dic2[ny] = min(dic2[ny]+k,m)

    res = 0
    for y in dic2:
        res += dic2[y]

    print(res)

    dic = dic2