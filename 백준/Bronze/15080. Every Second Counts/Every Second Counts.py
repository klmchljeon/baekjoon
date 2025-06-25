def conv(lst):
    return lst[0]*3600 + lst[1]*60 + lst[2]

a = list(map(int,input().split(" : ")))
b = list(map(int,input().split(" : ")))

p = conv(b) - conv(a)
if p < 0:
    p += 86400

print(p)