#행렬 곱셈 순서
m = 2**31-1

n = int(input())
d = []
for _ in range(n):
    a,b = map(int,input().split())
    d.append((a,b))
    
dp = [[0]*n for _ in range(n)]
for i in range(n-1):
    dp[i][i+1] = d[i][0]*d[i][1]*d[i+1][1]
    
for size in range(2,n):
    for i in range(n-size):
        res = m
        for j in range(size):
            tmp = dp[i][i+j] + dp[i+j+1][i+size]
            tmp += d[i][0]*d[i+size][1]*d[i+j][1]
            
            res = min(res, tmp)
        
        dp[i][i+size] = res
        
print(dp[0][n-1])