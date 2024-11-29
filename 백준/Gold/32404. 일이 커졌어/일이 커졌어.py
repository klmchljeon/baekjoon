n = int(input())
c = n//2

a = list(range(1,c+1))
b = list(range(c+1,n+1))[::-1]

lst = []
while a and b:
    lst.append(b.pop())
    lst.append(a.pop())

if b:
    lst.append(b.pop())

print(*lst)