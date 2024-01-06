t = int(input())
for case in range(t):
    n = int(input())
    tmp = n%100
    if (n+1)%tmp:
        print('Bye')
    else:
        print('Good')