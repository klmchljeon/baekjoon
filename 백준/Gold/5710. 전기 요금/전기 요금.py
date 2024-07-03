def cal(w):
    cost = 0
    if w <= 100:
        cost += w * 2
        return cost
    
    cost += 100 * 2
    if w <= 10000:
        cost += (w - 100) * 3
        return cost
    
    cost += (10000 - 100) * 3
    if w <= 1000000:
        cost += (w - 10000) * 5
        return cost
    
    cost += (1000000 - 10000) * 5
    cost += (w - 1000000) * 7
    return cost

def calr(cost):
    w = 0
    if cost <= 100 * 2:
        w += cost // 2
        return w
    
    w += 100
    cost -= 100 * 2
    if cost <= (10000 - 100) * 3:
        w += cost // 3
        return w
    
    w += (10000 - 100)
    cost -= (10000 - 100) * 3
    if cost <= (1000000 - 10000) * 5:
        w += cost // 5
        return w
    
    w += (1000000 - 10000)
    cost -= (1000000 - 10000) * 5
    w += cost // 7
    return w
 
def check(num):
    my = cal(num)
    ot_w = calr(cal(num) + b)

    sum_ = cal(num + ot_w)

    return sum_ >= a

while True:

    a,b = map(int,input().split())
    if a==0 and b==0: break

    s,e = -1,int(1e9)
    while s+1<e:
        mid = (s+e)//2

        if check(mid):
            e = mid

        else:
            s = mid

    print(cal(e))