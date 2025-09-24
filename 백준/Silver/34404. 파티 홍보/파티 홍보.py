#파티 홍보
n = int(input())
lst = []
for _ in range(n):
    tmp = list(map(int,input().split()))
    x = tmp[0] + tmp[2]
    y = tmp[1] + tmp[3]
    lst.append((x,y))
 
a,b = map(int,input().split())
b *= 2
 
cnt = 0
for x,y in lst:
    cnt += y >= a*x + b
 
print(cnt)
