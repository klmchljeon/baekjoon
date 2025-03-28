t = int(input())
for case in range(t):
    lst = list(map(int,input().split()))
    print(f'Case #{case+1}: {max(lst)}')