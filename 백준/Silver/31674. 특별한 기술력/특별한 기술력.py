mod = int(1e9)+7

n = int(input())
d = list(map(int,input().split()))
d.sort()

tmp = 0
while d:
    tmp = (tmp + tmp + d.pop())%mod

print(tmp)