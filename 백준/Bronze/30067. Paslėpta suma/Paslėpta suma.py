lst = [int(input()) for _ in range(10)]
for i in range(10):
    if lst[i]*2 == sum(lst):
        print(lst[i])
        break