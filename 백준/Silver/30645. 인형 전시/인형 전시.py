def fill():
    t = 0
    cnt = 0
    for i in range(1,r+1):
        for j in range(c):
            while lst[i-1][j]>=d[t]:
                t += 1
                if t==n: return cnt

            lst[i][j] = d[t]
            cnt += 1
            t += 1
            if t==n: return cnt

    return cnt

r,c = map(int,input().split())
n = int(input())
d = list(map(int,input().split()))
d.sort()

lst = [[0]*c for _ in range(r+1)]
print(fill())
