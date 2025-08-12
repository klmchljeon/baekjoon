m = lambda i:(i//2+1)*100

lst = list(map(int,input().split()))
for i in range(9):
    if lst[i] > m(i):
        print('hacker')
        break

else:
    print('draw' if sum(lst)>=100 else 'none')