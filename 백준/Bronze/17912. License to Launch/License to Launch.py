n = int(input())
lst = list(map(int,input().split()))
val = int(1e9)
idx = -1
for i in range(n):
    if val > lst[i]:
        val = lst[i]
        idx = i
        
print(idx)