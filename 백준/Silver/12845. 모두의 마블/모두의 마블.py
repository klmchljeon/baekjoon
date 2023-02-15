#모두의 마블
n = int(input())
d = list(map(int,input().split()))

print(max(d)*(n-2) + sum(d))