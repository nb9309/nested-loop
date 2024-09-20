n = int(input('enter value: '))

for i in range(1,n+1):
    print('-'*50)
    print('{} table'.format(i))
    print('-'*50)
    for j in range(1,11):
        print('{} x {} = {}'.format(i,j,i*j))
