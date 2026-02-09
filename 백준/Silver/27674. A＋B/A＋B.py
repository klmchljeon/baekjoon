n = int(input())
for case in range(n):
    input()
    lst = list(input())
    lst.sort(reverse = True)

    a = int(lst.pop())
    b = int(''.join(lst))
    print(a+b)