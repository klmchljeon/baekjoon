#나머지 합
from collections import defaultdict

n,mod = map(int,input().split())
d = [0]+list(map(int,input().split()))

dp = [0]*(n+1)
for i in range(1,n+1):
    dp[i] = (dp[i-1]+d[i])%mod

dic = defaultdict(int)
for i in dp:
    dic[i] += 1

res = 0
for i in dic.values():
    res += i*(i-1)//2

print(res)