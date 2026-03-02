import sys
input = sys.stdin.readline

n = int(input())
dic = dict()
for _ in range(n):
    a,b = input().rstrip().split('.')
    if not b in dic:
        dic[b] = 0

    dic[b] += 1

for a,b in sorted(dic.items()):
    print(a,b)