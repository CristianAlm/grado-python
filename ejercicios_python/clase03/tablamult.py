print(' ', end='')
for i in range(10):
    print(f'{i:>4d}', end=' ')
print('')
print('-'*54)

for i in range(10):
    print(i, end=': ')
    s=0
    for j in range(10):
        print(f'{s:^4d}', end=' ')
        s+=i
    print('')