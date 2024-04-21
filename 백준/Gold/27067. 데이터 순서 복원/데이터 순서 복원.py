#데이터 순서 복원
n = int(input())
a = list(map(int,input().split()))
b = list(map(int,input().split()))
c = list(map(int,input().split()))

for i in range(n):
    if a[i]==b[i] and b[i]==c[i]:
        continue

    if a[i]==b[i]:
        c[i],c[i+1] = c[i+1],c[i]
        continue

    if b[i]==c[i]:
        a[i],a[i+1] = a[i+1],a[i]
        continue

    if a[i]==c[i]:
        b[i],b[i+1] = b[i+1],b[i]
        continue

    if a[i+1]==b[i+1] and b[i+1]==c[i+1]:
        a[i],a[i+1] = a[i+1],a[i]
        b[i],b[i+1] = b[i+1],b[i]
        c[i],c[i+1] = c[i+1],c[i]
        continue

    if a[i+1]==b[i+1]:
        a[i],a[i+1] = a[i+1],a[i]
        b[i],b[i+1] = b[i+1],b[i]
        continue

    if b[i+1]==c[i+1]:
        b[i],b[i+1] = b[i+1],b[i]
        c[i],c[i+1] = c[i+1],c[i]
        continue

    if a[i+1]==c[i+1]:
        a[i],a[i+1] = a[i+1],a[i]
        c[i],c[i+1] = c[i+1],c[i]
        continue

print(*a)