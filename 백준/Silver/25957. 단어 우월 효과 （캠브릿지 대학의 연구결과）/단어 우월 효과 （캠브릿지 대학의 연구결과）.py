import sys
input = sys.stdin.readline

def conv(st):
    tmp = list(st)
    tmp[1:-1] = sorted(tmp[1:-1])
    return ''.join(tmp)

n = int(input())
dic = dict()
for _ in range(n):
    st = input().rstrip()
    dic[conv(st)] = st

m = int(input())
lst = input().split()
for i in range(m):
    lst[i] = dic[conv(lst[i])]

print(*lst)