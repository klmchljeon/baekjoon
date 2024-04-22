n = int(input())
d = list(map(int,input().split()))

m = max(d)
s = sum(d) - m

if m <= s+1:
    res = m+s

else:
    res = 2*s+1

print(res)