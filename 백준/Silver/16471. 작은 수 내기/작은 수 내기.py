n = int(input())
a = list(map(int,input().split()))
b = list(map(int,input().split()))

if n==1:
    print('YES' if a[0]<b[0] else 'NO')
    exit()

a.sort()
b.sort()

for i in range(n//2):
    if a[i] >= b[n-i-1]:
        print('NO')
        break

else:
    print('YES')