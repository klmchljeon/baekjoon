import sys
input = sys.stdin.readline

lst = ['Y','F','O']
dic = dict(zip(lst,range(1,4)))

n,s = input().split()
n = int(n); s = dic[s]
st = set([input().rstrip() for _ in range(n)])

print(len(st)//s)