def start(n):
    tmp = int(n**0.5)
    if tmp*tmp != n: 
        tmp += 1

    return tmp//2

def cal(dist,line):
    tmp = min(dist,line)
    dist -= tmp
    loc[1] -= tmp

    tmp = min(dist,line)
    dist -= tmp
    loc[0] += tmp

    tmp = min(dist,line)
    dist -= tmp
    loc[1] += tmp

    tmp = min(dist,line)
    dist -= tmp
    loc[0] -= tmp

t = int(input())
for case in range(t):
    n = int(input())
    
    p = start(n)
    end = (p*2 + 1)
    dist = end**2 - n
    line = end-1

    loc = [-p,p]
    cal(dist,line)

    print(f"({loc[0]},{loc[1]})")