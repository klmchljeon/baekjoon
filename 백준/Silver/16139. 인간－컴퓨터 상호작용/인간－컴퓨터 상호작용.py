import sys
input = sys.stdin.readline

lst = [ord(i)-ord('a') for i in input().rstrip()]
prefix = [[0] for _ in range(26)]
s = [0]*26
for i in lst:
    s[i] += 1
    for j in range(26):
        prefix[j].append(s[j])

n = int(input())
for _ in range(n):
    st,l,r = input().split()
    l,r = map(int,(l,r))
    idx = ord(st)-ord('a')
    print(prefix[idx][r+1] - prefix[idx][l])