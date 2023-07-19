n = int(input())
res = 1
for i in range(1,n+1):
    res *= i
    
print(res//(7*24*60*60))