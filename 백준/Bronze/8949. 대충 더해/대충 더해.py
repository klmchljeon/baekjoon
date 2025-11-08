a,b = input().split()
a = list(map(int,a))
b = list(map(int,b))

res = []
while a and b:
    res.append(str(a.pop()+b.pop()))

while a:
    res.append(str(a.pop()))
    
while b:
    res.append(str(b.pop()))

print(''.join(res[::-1]))