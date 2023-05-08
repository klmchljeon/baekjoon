#정수 제곱근
def check(num):
    return num**2 >= n

n = int(input())

low,high = -1,2**32
while low + 1 < high:
    mid = (low + high)//2

    if check(mid):
        high = mid

    else:
        low = mid

print(high)