import datetime as d

yd = map(int,input().split())
bl = map(int,input().split())

day = (d.date(*bl) - d.date(*yd)).days

t,n = map(int,input().split())
dp = [0]*(t+1)
for i in range(n):
    q,c,v = map(int,input().split())
    val = v*(30 if q==3 else 1)
    
    for w in range(c,t+1)[::-1]:
        dp[w] = max(dp[w], dp[w-c] + val)

print(abs(day-dp[t]))