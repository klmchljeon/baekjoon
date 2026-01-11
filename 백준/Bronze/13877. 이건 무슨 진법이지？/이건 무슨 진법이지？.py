t = int(input())
for case in range(t):
    k,num = input().split()
    res = [k,0,int(num,10),int(num,16)]
    
    if not ('8' in num or '9' in num):
        res[1] = int(num,8)

    print(*res)