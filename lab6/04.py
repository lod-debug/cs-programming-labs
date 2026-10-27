n = int(input())
summ=0
count = 0
if n<0:
    print('ошибка')
elif n == 0:
    print("Цифр: 0")
    print("Сумма цифр: 0")
else:
    while n>0:
        count +=1 
        i = n%10
        n = n//10
        summ += i
    print(f'Цифр: {count}')
    print (f'Сумма цифр: {summ}')


