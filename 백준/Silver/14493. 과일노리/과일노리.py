n = int(input())
cur = 0
for i in range(n):
    a,b = map(int,input().split())
    tmp = cur%(a+b) 
    if tmp < b:
        cur += b-tmp

    cur += 1

print(cur)