n = int(input())
for case in range(n):
    a,b,c = map(int,input().split())
    cnt = 0
    for i in (a,b,c):
        cnt += i >= 10

    res = ['zilch','double','double-double','triple-double']
    print(a,b,c)
    print(res[cnt])
    print()