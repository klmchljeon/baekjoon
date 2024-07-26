p = [202021, 
     20202021, 
     202002021, 
     202012021, 
     202022021, 
     202032021, 
     202042021, 
     202052021, 
     202062021, 
     202072021, 
     202082021, 
     202092021]

t = int(input())
for case in range(t):
    n = int(input())
    lst = list(map(int,input().split()))

    dic = dict()

    res = 0
    for i in range(n):
        for a in p:
            if a-lst[i] in dic:
                res += dic[a-lst[i]]

        if lst[i] in dic:
            dic[lst[i]] += 1
        else:
            dic[lst[i]] = 1
                

    print(res)