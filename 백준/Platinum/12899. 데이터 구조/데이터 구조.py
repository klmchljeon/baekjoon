#데이터 구조
import sys
input = sys.stdin.readline
t = 2000000

def cal(target,s,e,node=1):
    if s==e:
        update(s,-1,1,t)
        return s
    
    m = (s+e)//2
    temp = tree[node*2]
    if target <= temp:
        return cal(target,s,m,node*2)
    else:
        return cal(target-temp,m+1,e,node*2+1)

def update(idx,val,s,e,node=1):
    if s==e:
        tree[node] += val
        return val

    m = (s+e)//2
    if idx <= m:
        temp = update(idx,val,s,m,node*2)
        tree[node] += temp
        return temp

    else:
        temp = update(idx,val,m+1,e,node*2+1)
        tree[node] += temp
        return temp

tree = [0]*(t*4)

n = int(input())
for _ in range(n):
    q,x = map(int,input().split())
    if q == 2:
        print(cal(x,1,t))
        
    else:
        update(x,1,1,t)