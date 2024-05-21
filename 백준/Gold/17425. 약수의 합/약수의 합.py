import sys
input = sys.stdin.readline
max_ = 1000000

lst = [0]*(max_+1)
for i in range(1,max_+1):
    for j in range(i,max_+1,i):
        lst[j] += i

prefix = [0]*(max_+1)
for i in range(1,max_+1):
    prefix[i] = prefix[i-1] + lst[i]

t = int(input())
for case in range(t):
    n = int(input())
    print(prefix[n])