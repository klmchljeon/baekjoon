t = int(input())
for case in range(t):
    n,m = map(int,input().split())
    d = [list(map(int,input().split())) for _ in range(n)]

    res = 0
    for j in range(m):
        tmp = 0
        cnt = 0
        for i in range(n-1,-1,-1):
            if d[i][j] == 1:
                tmp += n-1-i - cnt
                cnt += 1

        res += tmp
    
    print(res)