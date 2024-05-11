n,*d = input().split()
n = int(n)
d = [int(i[::-1]) for i in d]

while len(d) < n:
    a = input().split()
    for i in a:
        d.append(int(i[::-1]))

d.sort()
print(*d,sep='\n')