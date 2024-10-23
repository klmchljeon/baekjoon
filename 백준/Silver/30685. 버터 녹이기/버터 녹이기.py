import sys
input = sys.stdin.readline

def cal(x,h,num):
    if h//2 < num:
        return (x-h//2,x+h//2)
    else:
        return (x-num,x+num)

def check(num):
    p = cal(*lst[0],num)[1]
    for i in range(1,n):
        a,b = cal(*lst[i],num)
        if a <= p: 
            return False
        
        p = b

    return True

n = int(input())
lst = []
for i in range(n):
    x,h = map(int,input().split())
    lst.append((x,h))

lst.sort()

s,e = 0,int(1e9)+1
while s+1<e:
    mid = (s+e)//2

    if check(mid):
        s = mid

    else:
        e = mid

print(s if s!=int(1e9) else 'forever')