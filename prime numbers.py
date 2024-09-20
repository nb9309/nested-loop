n = int(input('enter value: '))
if n <= 1:
    print('{} is invalid'.format(n))
else:
    for num in range(2,n+1):
        res = True
        for j in range(2,num):
            if num%j == 0:
                res = False
                break
        if res == True:
            print(num,end=' ')