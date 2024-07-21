import sys
input = sys.stdin.readline

def conv(d):
    d_index = sorted(set(d))
    dic = {d_index[i]:i for i in range(len(d_index))}
    return tuple([dic[i] for i in d])

n,m = map(int,input().split())
dic = dict()
for _ in range(n):
    lst = list(map(int,input().split()))
    tp = conv(lst)
    if not tp in dic:
        dic[tp] = 0

    dic[tp] += 1

res = 0
for i in dic:
    k = dic[i]
    res += k*(k-1)//2

print(res)