#XOR Sum 2
import sys
input = sys.stdin.readline

def update(num):
    idx = dic[num][-1]
    dic[num].pop()
    lst[idx] = num

    buc[idx//sqn][0] ^= num
    buc[idx//sqn][1] += 1

    return 

def cal(k):
    r = n-1
    res = 0

    while (r+1)%sqn and k:
        if lst[r] != None:
            res ^= lst[r]
            k -= 1

        r -= 1

    while k:
        idx = r//sqn
        if k - buc[idx][1] >= 0:
            res ^= buc[idx][0]
            k -= buc[idx][1]
        else: break

        r -= sqn

    while k:
        if lst[r] != None:
            res ^= lst[r]
            k -= 1

        r -= 1

    return res

t = int(input())
for case in range(t):
    m = int(input())
    query = []
    n = 0

    d = []
    for _ in range(m):
        o,num = input().split()
        num = int(num)

        if o == 'insert':
            n += 1
            d.append(num)
            query.append((1,num))

        else:
            e = min(n,num)
            query.append((2,e))

    d.sort()
    dic = dict()
    cnt = 0
    for i in d:
        if i in dic:
            dic[i].append(cnt)
        else:
            dic[i] = [cnt]

        cnt += 1

    sqn = int(n**0.5) + 1
    lst = [None]*n
    buc = [[0]*2 for _ in range(sqn)]
    for i in range(m):
        q,order = query[i]
        if q == 1:
            update(order)

        else:
            print(cal(order))