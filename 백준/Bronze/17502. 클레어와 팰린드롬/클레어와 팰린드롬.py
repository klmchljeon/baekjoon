n = int(input())
lst = list(input())
for i in range(n//2+1):
    if lst[i] == lst[n-1-i]:
        if lst[i] == '?':
            lst[i] = 'a'
            lst[n-1-i] = 'a'
            continue

    if lst[i] != '?':
        lst[n-1-i] = lst[i]
    else:
        lst[i] = lst[n-1-i]

print(''.join(lst))