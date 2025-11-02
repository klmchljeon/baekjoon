n = int(input())
m = int(input())
if n > m:
    n,m = m,n

if n == 1:
    print(m)
else:
    print(2*(n+m-2))