a,b = map(int,input().split())
n = int(input())
for case in range(n):
    k = int(input())
    if k <= 1000:
        print(k,a*k)
    else:
        print(k,1000*a + (k-1000)*b)