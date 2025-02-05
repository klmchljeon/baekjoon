n = int(input())
lst = list(map(int,input().split()))
res = sum(lst)%3==0
print('yes' if res else 'no')