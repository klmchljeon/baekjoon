n = int(input())
m = None
for _ in range(n):
    a,b = map(int,input().split())
    if m == None or m > a+b:
        m = a+b
        
print(m)