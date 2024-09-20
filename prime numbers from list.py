lst = []
while 9:
    val = input()
    if (not val.isdigit()):
        break
    else:
        lst.append(int(val))
print('-'*50)
print(lst)
print('-'*50)
print('list of prime numbers')
count = 0
for i in lst:
    res = True
    for j in range(2,i):
        if i%j == 0:
            res = False
            break
    if res == True:
        print(i,end=' ')
        count += 1
else:
    print()
    print('numbers of primes are {}'.format(count))

