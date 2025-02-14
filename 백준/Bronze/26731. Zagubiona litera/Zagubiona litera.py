st = input()
print(next(iter(set([chr(i + ord('A')) for i in range(26)])-set(st))))