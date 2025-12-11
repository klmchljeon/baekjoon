n = int(input())
lst = [input() for _ in range(n)]
y = lst.index('yonsei')
k = lst.index('korea')
print('Yonsei Won!' if y < k else 'Yonsei Lost...')