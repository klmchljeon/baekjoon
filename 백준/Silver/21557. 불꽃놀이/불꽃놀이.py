n = int(input())
lst = list(map(int,input().split()))
a,b = lst[0],lst[-1]
a-=1;b-=1;
if a < b:
    a,b = b,a

for i in range(n-3):
    a -= 1
    if a < b:
        a,b = b,a

print(a)