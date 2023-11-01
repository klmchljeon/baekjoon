import sys
from collections import defaultdict
input = sys.stdin.readline

f = lambda x:(-x[1],-len(x[0]),x[0])

n,m = map(int,input().split())

dic = defaultdict(int)
for _ in range(n):
    st = input().rstrip()
    if len(st) < m: continue

    dic[st] += 1

lst = list(dic.items())
lst.sort(key = f)

for i in lst:
    print(i[0])