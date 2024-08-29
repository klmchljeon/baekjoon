import sys
input = sys.stdin.readline

def check(num,lst):
    cur = cal(num,lst)
    prev = cal(num+1,lst)

    return cur <= prev

def cal(num,lst):
    res = 0
    for i in lst:
        res += abs(num-i)

    return res

n = int(input())
lst1,lst2 = [],[]
for _ in range(n):
    x,y = map(int,input().split())
    lst1.append(x)
    lst2.append(y)

res = 0
for lst in (lst1,lst2):
    lst.sort()

    s,e = -int(1e6)-1,int(1e6)
    while s+1<e:
        mid = (s+e)//2

        if check(mid,lst):
            e = mid

        else:
            s = mid

    res += cal(e,lst)

print(res)