#반짝반짝 빛나는 별가루
import sys
input = sys.stdin.readline

n,k,c,r = map(int,input().split())
base = [0]+list(map(int,input().split()))
s = [0]+list(map(int,input().split()))
p = [0]+list(map(int,input().split()))
l = [int(input()) for _ in range(n)]


pi = 0
combo = 0
stardust = 0
skill = [0]*(k+1)
for i in range(n):
    num = l[i]
    if not num:
        pi = max(0,pi-r)
        combo = 0
        continue

    pi += p[num]
    if pi > 100:
        print(-1)
        break

    stardust += base[num]*(100+combo*c)*(100+skill[num]*s[num])//10000
    combo += 1

    skill[num] += 1

else:
    print(stardust)
