#할로윈의 사탕
t = int(input())
for case in range(t):
    a,b = map(int,input().split())
    p,q = divmod(a,b)
    res = f'You get {p} piece(s) and your dad gets {q} piece(s).'
    print(res)