prime = []
for p in range(2,119):
    cnt = 0
    for i in range(1,p+1):
        cnt += p%i == 0

    if cnt == 2:
        prime.append(p)

n = int(input())
for case in range(n):
    a = int(input())
    for i in prime:
        if a-i in prime:
            print('Yes')
            break

    else:
        print('No')