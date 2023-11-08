#호반우가 학교에 지각한 이유 3
import sys
input = sys.stdin.readline

n = int(input())
query = []
for _ in range(n):
    a,b = map(int,input().split())
    query.append((a,b))

res = 0
t = 10**9
tmp = 0
for a,b in query[::-1]:
    if a==1:
        t = min(t,max(b-tmp,0))
        res += min(b,t)
        tmp = 0
    else:
        tmp += b

print(res)