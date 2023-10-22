#WA
n = int(input())
a = list(map(int,input().split()))
b = list(map(int,input().split()))

if n==1:
    print('YES' if a[0]<b[0] else 'NO')
    exit()

a.sort()
b.sort()

half = n//2
for i in range(half):
    if a[i] >= b[half+i]:
        print('NO')
        break

else:
    print('YES')