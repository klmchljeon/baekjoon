lst = list(input())
p = int(lst.pop())

tmp = 0
for i in range(12):
    k = 1 if i%2==0 else 3
    
    if lst[i] != '*':
        tmp += int(lst[i])*k

    else:
        m = k

for i in range(10):
    if (tmp + i*m + p)%10 == 0:
        print(i)
        break