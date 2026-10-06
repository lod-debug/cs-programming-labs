god = int(input())
if 1<=god<=9999:
    if god%400==0 or (god%4==0 and god%100!=0):
        print('Високосный')
    else:
        print('год невисокосный')

else:
    print('ошибка')
