b = map(int,input().split())
d = map(int,input().split())
s = 0
for i,j in zip(b,d):
    s += max(0,j-i)

print(s)