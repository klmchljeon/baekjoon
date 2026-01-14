t = int(input())
for case in range(t):
    lst = list(input())
    n = len(lst)
    for i in range(n):
        tmp = lst + lst[:i][::-1]

        if tmp == tmp[::-1]:
            print(''.join(tmp))
            break
