n = int(input())
d = list(map(int,input().split()))
res = 0
odd = []
for i in d:
    if i&1:
        odd.append(i)
    else:
        res += i
        
odd.sort(reverse = 1)
m = len(odd)
for i in range(m-m%2):
    res += odd[i]
    
print(res)