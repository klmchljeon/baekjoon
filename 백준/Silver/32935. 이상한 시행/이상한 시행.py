n = int(input())
lst = list(map(int,input().split()))

s = sum(lst)
a = min(lst)
if -s > a:
    s += -s-a

print(s)