case = 1
while True:
    n = int(input())
    if n==0: break

    k = int(input())
    d = [int(input()) for _ in range(k)]

    res = [f'{i*n/1e5:.05f}' for i in d]
    
    print(f'User {case}')
    print(*res,sep='\n')
    case += 1