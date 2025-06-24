n = int(input())
flag = True
for _ in range(3):
    lst = list(map(int,input().split()))
    tmp = False
    for i in lst:
        tmp |= i == 7
        
    flag &= tmp
    
print(777 if flag else 0)