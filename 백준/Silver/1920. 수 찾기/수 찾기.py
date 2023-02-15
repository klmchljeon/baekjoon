n = int(input())
d = set(map(int,input().split()))
x = int(input())
m = list(map(int,input().split()))
for i in m:
	if i in d:
		print(1)
	else:
		print(0)