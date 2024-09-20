lst = []
while 9:
    val = input()
    if (not val.isdigit()):
        break
    else:
        lst.append(int(val))
print(lst)

for i in lst:
    print(('-'*50))
    print(i)
    print('-'*50)
    for j in range(1,11):
        print(f'{i} x {j} = {i*j}')
