n = int(input())
d = list(map(int,input().split()))

tmp = 0
res = 0
for i in d:
    res = abs(res-i)
    tmp += i

print((tmp+res)//2)