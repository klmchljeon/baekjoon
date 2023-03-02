#친구 친구
import sys
input = sys.stdin.readline

n,m = map(int,input().split())
cnt = [0]*(n+1)
for _ in range(m):
    a,b = map(int,input().split())
    cnt[a] += 1
    cnt[b] += 1
    
print(*cnt[1:],sep='\n')