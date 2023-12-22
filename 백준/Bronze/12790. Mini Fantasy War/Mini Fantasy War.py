t = int(input())
for case in range(t):
    d = list(map(int,input().split()))
    hp = max(1,d[0]+d[4])
    mp = max(1,d[1]+d[5])
    atk = max(0,d[2]+d[6])
    df = d[3]+d[7]

    res = hp + 5*mp + 2*atk + 2*df
    print(res)