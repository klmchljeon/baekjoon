mod = int(1e9)+7
max_ = int(1e6)

def fpow(C,k):
    if k==1:
        return C

    x = fpow(C,k//2)
    if k%2 == 0:
        return (x*x)%mod
    else:
        return (x*x*C)%mod

f = [1]*(max_+1)
for i in range(2,max_+1):
    f[i] = (f[i-1]*i)%mod

f1 = [0]*(max_+1)

n,m = map(int,input().split())
d = list(map(int,input().split()))

lst = [m-i for i in d]
tmp = m-sum(lst)
if tmp < 0:
    print(0)
    exit()

lst.append(tmp)

up = f[m]
down = 1
for i in lst:
    down = (down*f[i])%mod

res = up*(fpow(down,mod-2))%mod
print(res)