pokupki = 0
stoimost = 0

while True:
    n = input()
    if n =='stop':
        break
    pokupki +=1
    stoimost +=int(n)
if pokupki ==0:
    print('нет покупок')
else:
    print(f'покупок: {pokupki}')
    print(f'Общая стоимость: {stoimost}')
    print(f'Средняя стоимость: {(stoimost/pokupki):.02f}')
