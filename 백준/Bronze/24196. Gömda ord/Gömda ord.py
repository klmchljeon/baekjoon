st = input()
idx = 0

res = ''
while idx < len(st):
    res += st[idx]
    idx += ord(st[idx]) - ord('A') + 1

print(res)