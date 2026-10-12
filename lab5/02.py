a = int(input())
b = int(input())
summ=0
proizv=1
for s in range(a,b+1):
    summ +=int(s)
    proizv *=int(s)
print(f'сумма: {summ}')
print(f'произведение: {proizv}')