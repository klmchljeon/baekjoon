n = int(input())
res = 1
for i in range(1,n+1):
    if i%6 == 1:
        res += i//6
    
    elif i%6 == 0:
        res += i//6 + 1

    else:
        res += i//6 + 1

print(res)