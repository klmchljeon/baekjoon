n = int(input())
k = int(input())
cnt = 0
for i in range(1,k):
    print(i)
    cnt += i
    
print(n-cnt)