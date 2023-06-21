#수열 (Easy)
mod = 1000000007

n = int(input())
d = list(map(int,input().split()))

res = 0
s = sum(d)
for i in d[:-1]:
    s -= i

    res += i*s
    res %= mod

print(res)