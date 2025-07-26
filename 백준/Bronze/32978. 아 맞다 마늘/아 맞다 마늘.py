n = int(input())
lst = input().split()
d = input().split()
for i in lst:
    if not i in d:
        print(i)
        break