n = int(input())
lst = []
for _ in range(n):
    x,y = map(int,input().split())
    lst.append((x,y))

lst = tuple(lst)
cnt = 0
for i in range(n-2):
    for j in range(i+1,n-1):
        for k in range(j+1,n):
            a,b,c = lst[i],lst[j],lst[k]
            d1 = (a[0]-b[0])**2 + (a[1]-b[1])**2
            d2 = (a[0]-c[0])**2 + (a[1]-c[1])**2
            d3 = (b[0]-c[0])**2 + (b[1]-c[1])**2

            cnt += 2*max(d1,d2,d3) == d1+d2+d3

print(cnt)