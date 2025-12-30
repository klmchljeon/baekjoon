n = int(input())
st1 = input()
st2 = input()
if st1 == st2:
    print('Good')
elif sorted(st1) == sorted(st2):
    print('Its fine')
elif st1.count('w') > st2.count('w'):
    print('Oryang')
else:
    print('Manners maketh man')