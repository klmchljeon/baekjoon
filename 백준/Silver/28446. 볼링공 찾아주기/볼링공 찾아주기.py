import sys
input = sys.stdin.readline

m = int(input())

dic = dict()
for _ in range(m):
    q,*order = map(int,input().split())
    if q==1:
        x,w = order
        dic[w] = x
    else:
        print(dic[order[0]])