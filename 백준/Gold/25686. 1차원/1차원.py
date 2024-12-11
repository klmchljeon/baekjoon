def gen(p,n):
    gap = 1
    while gap < p:
        gap *= 2

    if p + gap > n: 
        return []

    tmp = []
    while p+gap <= n:
        tmp.append(p+gap)
        gap *= 2

    return tmp

def f(x,n):
    tmp = gen(x,n)
    while tmp:
        nx = tmp.pop()
        lst.append(nx)
        f(nx,n)
        
n = int(input())

lst =[1]
f(1,n)
print(*lst)