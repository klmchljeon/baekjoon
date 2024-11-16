n = int(input())
lst = []
for _ in range(n):
    x,y = map(int,input().split())
    lst.append((x,y))
    
res = 0
for i in range(n):
    res += abs(lst[i][0]-lst[i-1][0]) + abs(lst[i][1]-lst[i-1][1])
    
print(res)