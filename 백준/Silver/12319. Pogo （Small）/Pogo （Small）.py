t = int(input())
for case in range(t):
    x,y = map(int,input().split())
    
    res = ''
    for i,j in zip((x,y),("WE","SN")):
        if i == 0: continue
        res += j[::i//abs(i)]*abs(i)

    print(f'Case #{case+1}: {res}')