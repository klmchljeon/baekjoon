import sys
input = sys.stdin.readline

alpha = [chr(i + ord('a')) for i in range(26) if chr(i + ord('a')) not in 'auioe']
dic = dict(zip(alpha,range(len(alpha))))

n,m = map(int,input().split())
lst = []
for _ in range(n):
    st = input().rstrip()
    a = 0
    for i in st:
        if i in dic:
            a |= 1<<dic[i]

    lst.append(a)

b = eval("0b" + "1"*len(alpha))
for _ in range(m):
    q,x = input().split()
    if q == '1':
        b &= ~(1<<dic[x])
    else:
        b |= 1<<dic[x]

    cnt = 0
    for a in lst:
        cnt += not (a&(~b))

    print(cnt)