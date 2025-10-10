n,l,r = map(int,input().split())
lst = list(map(int,input().split()))
tmp = lst[:l-1] + sorted(lst[l-1:r]) + lst[r:]
print(int(sorted(lst) == tmp))