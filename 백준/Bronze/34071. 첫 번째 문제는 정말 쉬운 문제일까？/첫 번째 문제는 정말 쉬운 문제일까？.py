n = int(input())
lst = [int(input()) for _ in range(n)]
if lst[0] == min(lst):
    print('ez')
elif lst[0] == max(lst):
    print('hard')
else:
    print('?')