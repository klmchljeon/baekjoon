a = input()
b = input()

p = abs(ord(a[0])-ord(b[0]))
q = abs(int(a[1])-int(b[1]))
if p > q:
    p,q = q,p

print(p,q)