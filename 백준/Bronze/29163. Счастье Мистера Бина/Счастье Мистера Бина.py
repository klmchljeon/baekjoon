n = int(input())
d = list(map(int,input().split()))

cnt = 0
for i in d:
    cnt += -1 if i&1 else 1
    
print('Happy' if cnt > 0 else 'Sad')