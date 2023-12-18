t = int(input())
n = int(input())
d = list(map(int,input().split()))

res = 'Happy' if t<=sum(d) else 'Cry'
print(f'Padaeng_i {res}')