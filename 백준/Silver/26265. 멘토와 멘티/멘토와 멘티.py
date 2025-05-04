import sys
from functools import cmp_to_key
input = sys.stdin.readline

def compare(a,b):
    if a[0] < b[0]:
        return -1
    elif a[0] > b[0]:
        return 1

    if a[1] > b[1]:
        return -1
    else:
        return 1

n = int(input())
lst = []
for i in range(n):
    a,b = input().split()
    lst.append((a,b))

lst.sort(key = cmp_to_key(compare))
for i in lst:
    print(*i)
