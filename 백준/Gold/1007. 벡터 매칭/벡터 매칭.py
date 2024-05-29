#벡터 매칭

def cal(s):
    sumX = sumY = 0
    for i in s:
        sumX += d[i][0]
        sumY += d[i][1]

    return [sumX,sumY]

def dfs():
    if len(s) == n//2+1:
        lst = cal(s)
        dis = ((total[0]-2*lst[0])**2 + (total[1]-2*lst[1])**2 )**0.5
        result[0] = min(result[0],dis)

    else:
        for i in range(s[-1]+1,n+1):
            s.append(i)
            dfs()
            s.pop()

t = int(input())
for case in range(t):
    n = int(input())
    d = [[0,0]]+[list(map(int,input().split())) for _ in range(n)]

    total = cal([i for i in range(1,n+1)])
    result = [100000000]

    s = [0]
    dfs()
    print(result[0])