import sys
input = sys.stdin.readline

def cal(a,b,idx):
    a = (a+idx-1)%n+1
    b = (b+idx-1)%n+1
    res = 0
    if a <= b:
        res += prefix[b]-prefix[a-1]
    else:
        res += prefix[n]-prefix[a-1]
        res += prefix[b]

    return res

n,q = map(int,input().split())
d = list(map(int,input().split()))

prefix = [0]
for i in d:
    prefix.append(prefix[-1]+i)

s = 0
for i in range(q):
    x,*ord = map(int,input().split())
    if x == 1:
        s = (s - ord[0])%n

    elif x == 2:
        s = (s + ord[0])%n

    else:
        print(cal(*ord,s))