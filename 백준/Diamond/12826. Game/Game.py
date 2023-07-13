import sys
input = sys.stdin.readline

def cal(x,y):
    x = x//y
    if y&1:
        return x%2

    tmp = x%(y+1)
    return tmp%2

t = int(input())
for case in range(t):
    a,b = map(int,input().split())
    if a<b: a,b = b,a

    lst = [(a,b)]
    while b:
        a,b = b,a%b
        lst.append((a,b))

    lst.pop()
    lst.pop()

    res = 1
    while lst:
        a,b = lst.pop()
        if res == 0:
            res = 1
            continue

        if cal(a,b):
            res = 0

    print('Mirek' if res else 'Kamil')