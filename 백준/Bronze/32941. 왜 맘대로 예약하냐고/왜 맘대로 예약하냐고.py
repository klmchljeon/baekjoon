t,x = map(int,input().split())
res = True
n = int(input())
for _ in range(n):
    k = map(int,input().split())
    lst = list(map(int,input().split()))
    res &= x in lst

print('YES' if res else 'NO')