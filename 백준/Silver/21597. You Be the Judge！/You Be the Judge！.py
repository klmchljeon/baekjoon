import sys

def isprime(num):
    for i in range(2,int(num**0.5)+1):
        if num%i == 0:
            return 0
        
    return 1

def isnum(st):
    if not '1'<=st[0]<='9':
        return 0
    
    for i in st:
        if not '0'<=i<='9':
            return 0
        
    return 1

tmp = sys.stdin.read().split()
d = []
for i in tmp:
    if isnum(i):
        d.append(i)
    else:
        print(0)
        exit()

if len(d) != 3:
    print(0)
    exit()

a,b,c = map(int,d)
flag1 = a%2==0 and 3<=a<=10**9
flag2 = a==b+c
flag3 = isprime(b) and isprime(c)

res = flag1 and flag2 and flag3
print(int(res))